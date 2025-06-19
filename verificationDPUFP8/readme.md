in this script i just plot the Absolute Difference between the simulated value from the fp8DPU and the actual golden value result. against the B0, B1, B2, B3 (which are kept the same and vary in the same manner in between tests), while the A0, A1, A2, A3 and C0 values are fixed always at 2.75. in essence the dpu formula respective of this plot is the following:

= (2.75 * B0) + (2.75 * B1 ) + (2.75 * B2 ) + (2.75 *B3) + 2.75  and B0 = B1 = B2 = and B3

This test is to see more better the best range of values that the operands should more or less be in order for the current DPU FP8 results to be as accurate as possible.


