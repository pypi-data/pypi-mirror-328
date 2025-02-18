from collections import OrderedDict
from math import ceil, log2
from typing import Dict

import numpy as np
from npf.expdesign.fullexp import FullVariableExpander
from npf.models.dataset import Run
from npf.models.variables.variable import Variable

class OptVariableExpander(FullVariableExpander):
    def __init__(self, vlist:Dict[str,Variable], results, overriden, input, margin, all=False):
        if input not in vlist:
            raise Exception(f"{input} is not in the variables, please define a variable in the %variable section.")

        self.results = results
        self.input = input
        self.input_values = vlist[input].makeValues()
        if len(self.input_values) <= 2:
            print(  f"WARNING: Doing zero-loss-throughput search on the variable {input} that has only {len(self.input_values)} values. This is useless."
                    f"You must define a range to search with a variable like {input}=[0-100#5].")
        del vlist[input]
        self.current = None
        self.n_done = 0
        self.n_it = 0
        self.n_tot_done = 0
        self.margin = margin
        self.all = all
        super().__init__(vlist, overriden)

    def __iter__(self):
        self.it = self.expanded.__iter__()
        self.current = None
        self.n_it = 0
        self.n_tot_done = 0
        return self

    def strlen(self):
        approx = int(len(self.expanded) * ceil(log2(len(self.input_values)) if (self.n_it <= 1) else self.n_tot_done/(self.n_it - 1)))
        max = len(self.expanded) * len(self.input_values)
        return f"~{approx}(max {max})"

class ZLTVariableExpander(OptVariableExpander):

    def __init__(self, vlist:Dict[str,Variable], results, overriden, input, output, margin, all=False, perc=False, monotonic=False):
        self.output = output
        self.perc = perc
        self.monotonic = monotonic
        super().__init__(vlist, results, overriden, input, margin, all)

    def need_run_for(self, next_val):
        self.next_val = next_val
        copy = self.current.copy()
        copy.update({self.input : next_val})
        self.n_done += 1
        return copy

    def ensure_monotonic(self, max_r, vals_for_current):
        if not self.monotonic and \
            (max_r is not None and max_r < max(self.executable_values) or (max_r is None)):
            # If the function is not monotonic, we now have to try rates between the max acceptable and the first dropping rate
            if max_r is not None:
                after_max = next(iter(filter(lambda x : x > max_r, self.executable_values)))
            else:
                after_max = min(self.executable_values)

            if after_max not in vals_for_current:
                return self.need_run_for(after_max)

        #Else we're finished
        self.validate_run()
        return self.__next__()

    def validate_run(self):
        """ Mark this run as the best ZLT one
        """
        #self.results[self.current][IS_ZLT] = 1
        self.current = None

    def __next__(self):
        if self.current is None:
            self.current = self.it.__next__()
            if self.current is None:
                return None
            self.n_it += 1
            self.n_tot_done += self.n_done
            self.n_done = 0
            self.next_val = None
            self.executable_values = self.input_values.copy()
        elif not self.executable_values:
            #There's no more points to try, we could never find a ZLT
            self.current = None
            return self.__next__()


        # get all outputs for all inputs
        vals_for_current = {}
        acceptable_rates = []

        # max_r is the maximal rate (tried or not) that we tried but still dropped some packets
        max_r = max(self.executable_values)
        for r, vals in self.results.items():
            if Run(self.current).inside(r):
                try:
                    if self.output:
                        r_out = np.mean(vals[self.output])
                        r_in = r.variables[self.input]
                        if self.perc:
                            r_out = r_out/100 * r_in
                        vals_for_current[r_in] = r_out
                        if r_out >= r_in/self.margin:
                            acceptable_rates.append(r_in)
                        else:
                            max_r = min(max_r, r_out)
                except KeyError as e:
                    #raise Exception(
                     print(   f"{self.output} is not in the results. Sample of last result : {vals}"
                    )
                    #from e

        #Step 1 : try the max input rate first
        if not vals_for_current:
            next_val = max_r
        elif len(vals_for_current) == 1:
            #If we're lucky, the max rate is doable

            if len(acceptable_rates) == 1 and not self.all:
                return self.ensure_monotonic(max(acceptable_rates), vals_for_current)


            #Step 2 : go for the rate below the output of the max input
            maybe_achievable_inputs = list(filter(lambda x : x <= max_r, self.executable_values))
            if len(maybe_achievable_inputs) == 0:
                print(f"WARNING: No achievable for {self.input}! Tried {max_r} and it did not work.")
                return self.ensure_monotonic(None, vals_for_current)
            else:
                next_val = max(maybe_achievable_inputs)
        else:

            maybe_achievable_inputs = list(filter(lambda x : x <= max_r*self.margin, self.executable_values))
            left_to_try = set(maybe_achievable_inputs).difference(vals_for_current.keys())
            if len(left_to_try) == 0: #No more values left to try
                if len(acceptable_rates) > 0: #Nothing left to try but we have a ZLT, should try the next value in non-monotonic
                    return self.ensure_monotonic(max(acceptable_rates), vals_for_current)
                else:
                    #We could never find a zlt, and there's nothing left to try... no value can handle the input
                    self.validate_run()
                    return self.__next__()


            #Step 3...K : try to get an acceptable rate. This step might be skipped if we got an acceptable rate already
            if left_to_try and not acceptable_rates:
                #Try the rate below the min already tried rate - its drop count. For instance if we tried 70 last run but got 67 of throughput, try the rate below 64
                min_input = min(vals_for_current.keys())
                min_output = vals_for_current[min_input]
                target = min_output - (min_input - min_output)
                #We look for the rate below the target
                next_vals = list(filter(lambda x : x < target,left_to_try))
                #Maybe there's no rate as low as that so next_vals might be empty. In that case we take the minimal rate
                if len(next_vals) > 0:
                    next_val = max(next_vals)
                else:
                    next_val = min(left_to_try)
            else:
                #Step K... n : we do a binary search between the maximum acceptable rate and the minimal rate observed
                max_acceptable = -1 if self.all else max(acceptable_rates)
                #Consider we tried 100->95 (max_r=95), 90->90 (acceptable) we have to try values between 90..95
                left_to_try_over_acceptable = list(filter(lambda x: x > max_acceptable, left_to_try))
                if not left_to_try_over_acceptable:
                    return self.ensure_monotonic(max(acceptable_rates), vals_for_current)
                #Binary search
                if self.all:
                    next_val = max(left_to_try_over_acceptable)
                else:
                    next_val = left_to_try_over_acceptable[int(len(left_to_try_over_acceptable) / 2)]

        if next_val == self.next_val:
            self.executable_values.remove(next_val)
            #Loop : this value is not running for some reasons
            return self.__next__()

        return self.need_run_for(next_val)


class MinAcceptableVariableExpander(OptVariableExpander):

    def __init__(self, vlist:Dict[str,Variable], results, overriden, input, output, margin):
        self.output = output
        super().__init__(vlist, results, overriden, input, margin, False)

    def need_run_for(self, next_val):
        self.next_val = next_val
        copy = self.current.copy()
        copy.update({self.input : next_val})
        self.n_done += 1
        return copy

    def ensure_monotonic(self, max_r, vals_for_current):
        self.validate_run()
        return self.__next__()

    def validate_run(self):
        """ Mark this run as the best ZLT one
        """
        #self.results[self.current][IS_ZLT] = 1
        self.current = None

    def __next__(self):
        if self.current is None:
            self.current = self.it.__next__()
            if self.current is None:
                return None
            self.n_it += 1
            self.n_tot_done += self.n_done
            self.n_done = 0
            self.next_val = None
            self.executable_values = self.input_values.copy()
        elif not self.executable_values:
            #There's no more points to try, we could never find a ZLT
            self.current = None
            return self.__next__()


        # get all outputs for all inputs
        vals_for_current = {}
        acceptable_rates = []
        min_r = min(self.executable_values)
        for r, vals in self.results.items():
            if Run(self.current).inside(r):
                try:
                    if self.output:
                        r_out = np.mean(vals[self.output])
                        r_in = r.variables[self.input]
                        vals_for_current[r_in] = r_out
                        if r_out >= 100/self.margin:
                            acceptable_rates.append(r_in)
                except KeyError as e:
                    raise Exception(
                        f"{self.output} is not in the results. Sample of last result : {vals}"
                    ) from e

        #Step 1 : try the min value first
        if not vals_for_current:
            next_val = min_r
        elif len(vals_for_current) == 1:
            #If we're lucky, the min rate is doable

            if len(acceptable_rates) == 1:
                    return self.ensure_monotonic(min(acceptable_rates), vals_for_current)

            #Step 2 : go for the value abouve the undoable value
            maybe_achievable_inputs = list(filter(lambda x : x >= min_r, self.executable_values))
            next_val = max(maybe_achievable_inputs)
        else:

            max_r = max(self.executable_values)
            if vals_for_current[max_r] < 100/self.margin:
                #Undoable
                self.current = None
                return self.__next__()

            min_acceptable = min(acceptable_rates)
            maybe_achievable_inputs = list(filter(lambda x : x >= min_r/self.margin, self.executable_values))
            left_to_try = set(maybe_achievable_inputs).difference(vals_for_current.keys())

            left_to_try_below_acceptable = list(filter(lambda x: x < min_acceptable, left_to_try))
            if not left_to_try_below_acceptable:
                return self.ensure_monotonic(min_acceptable, vals_for_current)

            #Binary search
            next_val = left_to_try_below_acceptable[int(len(left_to_try_below_acceptable) / 2)]

        if next_val == self.next_val:
            self.executable_values.remove(next_val)
            #Loop : this value is not running for some reasons
            return self.__next__()

        return self.need_run_for(next_val)
