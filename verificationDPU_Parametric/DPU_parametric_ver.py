from sfpy import Posit8
from sfpy import Posit16
from sfpy import Posit32
from ml_dtypes import float8_e4m3
from sfpy import Float16
from sfpy import Float32
from fxpmath import Fxp

import numpy as np

DEBUG_FP8 = False 
DEBUG_FP16 = True 
DEBUG_FP32 = False
DEBUG_POSIT8 = False
DEBUG_POSIT16 = False
DEBUG_POSIT32 = False
DEBUG_FIXP8_16 = False
DEBUG_FIXP16_32 = False


with open("DPUrel0_parametric_results.txt", 'r') as f:
    
    mismatch_count_fp8 = 0 
    mismatch_count_fp16 = 0
    mismatch_count_fp32 = 0 
    mismatch_count_p8 = 0
    mismatch_count_p16 = 0
    mismatch_count_p32 = 0 
    mismatch_count_fixp8_16 = 0
    mismatch_count_fixp16_32 = 0

    fp8_nonNANresultTests = 0
    fp16_nonNANresultTests = 0
    fp32_nonNANresultTests = 0
    p8_nonNANresultTests = 0
    p16_nonNANresultTests = 0
    p32_nonNANresultTests = 0

    fp8_16_TotalTests = 0
    fp16_32_TotalTests = 0
    
    
    for line_num, line in enumerate(f, 1):
        try:
            parts = line.strip().split()

            widthSel, typeSel = int(parts[0]), int(parts[1])

            if (widthSel == 0 and typeSel == 0):
                #print(f"the format considered is float8_e4m3 ")
                
                def f8(hex_str):
                    return np.frombuffer(
                        np.array([int(hex_str, 16)], dtype=np.uint8).tobytes(),
                        dtype=float8_e4m3
                    )[0]

                A0 = f8(parts[2]) 
                A1 = f8(parts[3])
                A2 = f8(parts[4])
                A3 = f8(parts[5])
                B0 = f8(parts[6])
                B1 = f8(parts[7])
                B2 = f8(parts[8])
                B3 = f8(parts[9])
                C0 = f8(parts[10])
                resFromCircuit = f8(parts[29])

                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0
                #print(f" Vivado:{resFromCircuit} sim: {result}")

                #if( result != resFromCircuit and DEBUG_FP8):
                if DEBUG_FP8:
                    if not ( np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ): #considero solo test che non yieldano nan nel loro risultat
                        fp8_nonNANresultTests += 1
                        if not np.isclose(result, resFromCircuit, equal_nan=True):
                            print(f"FP8 case: Line {line_num}: Mismatch in float8 result: {result} != {resFromCircuit}")
                            mismatch_count_fp8 +=1 

            
            elif ( widthSel == 1 and typeSel == 0):
                #print(f" the format considered is float16 ")
                A0, A1, A2, A3 = Float16.from_bits(int(parts[11],16)), Float16.from_bits(int(parts[12],16)), Float16.from_bits(int(parts[13],16)), Float16.from_bits(int(parts[14],16))
                B0, B1, B2, B3 = Float16.from_bits(int(parts[15],16)), Float16.from_bits(int(parts[16],16)), Float16.from_bits(int(parts[17],16)), Float16.from_bits(int(parts[18],16))
                C0 = Float16.from_bits(int(parts[19],16))
                resFromCircuit = Float16.from_bits(int(parts[30],16))

                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 
                if DEBUG_FP16:
                    #if not np.isclose(float(result), float(resFromCircuit), equal_nan=True):
                    #    print(f"FP16 case: Line {line_num}: Mismatch in float16 result: {result} != {resFromCircuit}")
                    #    mismatch_count_fp16 +=1 
                    if not (np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ) :
                        fp16_nonNANresultTests +=1
                        if (result != resFromCircuit) :
                            print(f"FP16 case: Line {line_num}: Mismatch in float32 result: {result} != {resFromCircuit}")
                            mismatch_count_fp16 +=1

            elif ( widthSel == 2 and typeSel == 0):
                #print(f" the format considered is float32 ")
                A0, A1, A2, A3 = Float32.from_bits(int(parts[20],16)), Float32.from_bits(int(parts[21],16)), Float32.from_bits(int(parts[22],16)), Float32.from_bits(int(parts[23],16)) 
                B0, B1, B2, B3 = Float32.from_bits(int(parts[24],16)), Float32.from_bits(int(parts[25],16)), Float32.from_bits(int(parts[26],16)), Float32.from_bits(int(parts[27],16))
                C0 = Float32.from_bits(int(parts[28],16))
                resFromCircuit = Float32.from_bits(int(parts[31],16))

                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 
                if DEBUG_FP32:
                    #if not np.isclose(float(result), float(resFromCircuit), equal_nan=True):
                    #    print(f"FP32 case: Line {line_num}: Mismatch in float32 result: {result} != {resFromCircuit}")
                    #    mismatch_count_fp32 +=1
                    
                    if not ( np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ): #considero solo tests che non yieldano nan nel loro risultato
                        fp32_nonNANresultTests +=1
                        if (result != resFromCircuit):
                            print(f"FP32 case: Line {line_num}: Mismatch in float32 result: {result} != {resFromCircuit}")
                            mismatch_count_fp32 +=1

            elif ( widthSel == 0 and typeSel == 1):
                #print(f" the format considered is posit8 ")
                A0, A1, A2, A3 = Posit8.from_bits(int(parts[2],16)), Posit8.from_bits(int(parts[3],16)), Posit8.from_bits(int(parts[4],16)), Posit8.from_bits(int(parts[5],16))
                B0, B1, B2, B3 = Posit8.from_bits(int(parts[6],16)), Posit8.from_bits(int(parts[7],16)), Posit8.from_bits(int(parts[8],16)), Posit8.from_bits(int(parts[9],16))
                C0 = Posit8.from_bits(int(parts[10],16))
                resFromCircuit = Posit8.from_bits(int(parts[29],16))

                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0

                if DEBUG_POSIT8:
                    #if not np.isclose(float(result), float(resFromCircuit), equal_nan=True):
                    #    print(f"Posit8 case: Line {line_num}: Mismatch in posit8 result: {result} != {resFromCircuit}")
                    #    mismatch_count_p8 +=1
                    if not (np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ):#considero solo tests che non yieldano nan nel loro risultato
                        p8_nonNANresultTests +=1 
                        if ( result != resFromCircuit ):
                            print(f"Posit8 case: Line {line_num}: Mismatch in posit8 result: {result} != {resFromCircuit}")
                            mismatch_count_p8 +=1
                        
            elif ( widthSel == 1 and typeSel == 1):
                #print(f" the format considered is posit16 ")
                
                A0= Posit16.from_bits(int(parts[11], 16))
                #print(f"{int(parts[11],16)} {A0}")                
                A1= Posit16.from_bits(int(parts[12],16)) 
                A2= Posit16.from_bits(int(parts[13],16)) 
                A3= Posit16.from_bits(int(parts[14],16)) 
                B0, B1, B2, B3 = Posit16.from_bits(int(parts[15],16)), Posit16.from_bits(int(parts[16],16)), Posit16.from_bits(int(parts[17],16)), Posit16.from_bits(int(parts[18],16))
                C0 = Posit16.from_bits(int(parts[19],16))
                resFromCircuit = Posit16.from_bits(int(parts[30],16))
                
                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 
                
                if DEBUG_POSIT16:
                    
                    #if not np.isclose(result, resFromCircuit, equal_nan=True):
                    #        print(f"Posit16 case: Line {line_num}: Mismatch in posit16 result: {result} != {resFromCircuit}")
                    #        mismatch_count_p16 +=1
                    if not (np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ): #considero solo tests che non yieldano nan nel loro risultato
                        p16_nonNANresultTests +=1
                        if (result != resFromCircuit):
                            print(f"Posit16 case: Line {line_num}: Mismatch in posit16 result: {result} != {resFromCircuit}")
                            mismatch_count_p16 +=1
                        
            
            elif ( widthSel == 2 and typeSel == 1 ):
                #print(f" the format considered is posit32 ")
                A0, A1, A2, A3 = Posit32.from_bits(int(parts[20],16)), Posit32.from_bits(int(parts[21],16)), Posit32.from_bits(int(parts[22],16)), Posit32.from_bits(int(parts[23],16))
                B0, B1, B2, B3 = Posit32.from_bits(int(parts[24],16)), Posit32.from_bits(int(parts[25],16)), Posit32.from_bits(int(parts[26],16)), Posit32.from_bits(int(parts[27],16))
                C0 = Posit32.from_bits(int(parts[28],16))
                resFromCircuit = Posit32.from_bits(int(parts[31],16))

                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 

                if DEBUG_POSIT32:
                    #if not np.isclose(result, resFromCircuit, equal_nan=True):
                    #    print(f"Posit32 case: Line {line_num}: Mismatch in posit32 result: {result} != {resFromCircuit}")
                    #    mismatch_count_p32 +=1 
                    if not (np.isnan(float(result)) or np.isnan(float(resFromCircuit)) ): #considero solo tests che non yieldano nan nel loro risultato
                        p32_nonNANresultTests +=1
                        if (result != resFromCircuit):
                            print(f"Posit32 case: Line {line_num}: Mismatch in posit32 result: {result} != {resFromCircuit}")
                            mismatch_count_p32 +=1
            
            elif ( widthSel == 0 and typeSel == 2): #corresponds to interpreting them as the fixedpoint8_16 format
            
            #print(f" entrato line : {line_num} in fixedpoint8_16")
                A0 = Fxp(signed=True, n_word=8, n_frac=5)
                A0.set_val( "0x" + parts[2], raw=True)

                A1 = Fxp(signed=True, n_word=8, n_frac=5)
                A1.set_val( "0x" + parts[3], raw=True)

                A2 = Fxp(signed=True, n_word=8, n_frac=5)
                A2.set_val( "0x" + parts[4], raw=True)

                A3 = Fxp(signed=True, n_word=8, n_frac=5)
                A3.set_val( "0x" + parts[5], raw=True)

                B0 = Fxp(signed=True, n_word=8, n_frac=5)
                B0.set_val( "0x" + parts[6], raw=True)

                B1 = Fxp(signed=True, n_word=8, n_frac=5)
                B1.set_val( "0x" + parts[7], raw=True)
                
                B2 = Fxp(signed=True, n_word=8, n_frac=5)
                B2.set_val( "0x" + parts[8], raw=True)
                
                B3 = Fxp(signed=True, n_word=8, n_frac=5)
                B3.set_val( "0x" + parts[9], raw=True)
                
                C0 = Fxp(signed=True, n_word=16, n_frac=10)
                C0.set_val( "0x" + parts[19], raw=True)
                
                resFromCircuit =  Fxp(signed=True, n_word=16, n_frac=10)
                resFromCircuit.set_val( "0x" + parts[30], raw=True)
                
                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 #here we recompute the result in simulation time to confront it with what obtained with the circuit 
                
                if DEBUG_FIXP8_16:
                    fp8_16_TotalTests +=1
                    if (result != resFromCircuit):
                        print(f"FixedPoint8_16 case: Line {line_num}: Mismatch in fixedpoint8_16 result: simulatedRes:{result} != resFromCircuit:{resFromCircuit}")
                        mismatch_count_fixp8_16 +=1


            elif ( widthSel == 1 and typeSel == 2): # corresponds to interpreting them as the fixedpoint16_32 format
                                
                #print(f" entrato line : {line_num} in fixedpoint16_32")
                A0 = Fxp(signed=True, n_word=16, n_frac=10)
                A0.set_val( "0x" + parts[11], raw=True)
                
                #print(f"A0: {A0.hex()} | {A0}")
                A1 = Fxp(signed=True, n_word=16, n_frac=10)
                A1.set_val( "0x" + parts[12], raw=True)
                
                A2 = Fxp(signed=True, n_word=16, n_frac=10)
                A2.set_val( "0x" + parts[13], raw=True)
                
                A3 = Fxp(signed=True, n_word=16, n_frac=10)
                A3.set_val( "0x" + parts[14], raw=True)
                
                B0 = Fxp(signed=True, n_word=16, n_frac=10)
                B0.set_val( "0x" + parts[15], raw=True)
                
                B1 = Fxp(signed=True, n_word=16, n_frac=10)
                B1.set_val( "0x" + parts[16], raw=True)
                
                B2 = Fxp(signed=True, n_word=16, n_frac=10)
                B2.set_val( "0x" + parts[17], raw=True)
                
                B3 = Fxp(signed=True, n_word=16, n_frac=10)
                B3.set_val( "0x" + parts[18], raw=True)
                
                C0 = Fxp(signed=True, n_word=32, n_frac=20)
                C0.set_val( "0x" + parts[28], raw=True)
                
                resFromCircuit =  Fxp(signed=True, n_word=32, n_frac=20)
                resFromCircuit.set_val( "0x" + parts[31], raw=True)
                
                result = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0 #here we recompute the result in simulation time to confront it with what obtained with the circuit 
                
                if DEBUG_FIXP16_32:
                    fp16_32_TotalTests +=1
                    if (result != resFromCircuit):
                        print(f"FixedPoint16_32 case: Line {line_num}: Mismatch in fixedpoint16_32 result: {result} != {resFromCircuit}")
                        mismatch_count_fixp16_32 +=1

            #else:
            #    print(f"Line {line_num}: Invalid value combination: {widthSel}, {typeSel}")

        except ValueError:
            print(f"Line {line_num}: Couldn't convert values to integers.")

    if( DEBUG_FP8 == True ):
        print(f"number of mismatches: {mismatch_count_fp8}, total non-NAN result tests: {fp8_nonNANresultTests}")

    if( DEBUG_FP16 == True ):
        print(f"number of mismatches: {mismatch_count_fp16}, total non-NAN result tests: {fp16_nonNANresultTests}")

    if( DEBUG_FP32 == True ):
        print(f"number of mismatches: {mismatch_count_fp32}, total non-NAN result tests: {fp32_nonNANresultTests}")

    if( DEBUG_POSIT8 == True):
        print(f"number of mismatches: {mismatch_count_p8}, total non-NAN result tests: {p8_nonNANresultTests}")

    if( DEBUG_POSIT16 == True):
        print(f"number of mismatches: {mismatch_count_p16}, total non-NAN result tests: {p16_nonNANresultTests}")

    if( DEBUG_POSIT32 == True):
        print(f"number of mismatches: {mismatch_count_p32}, total non-NAN result tests: {p32_nonNANresultTests}")
    
    if( DEBUG_FIXP8_16 == True):
        print(f"number of mismatches: {mismatch_count_fixp8_16}, total tests: {fp8_16_TotalTests} ")
    
    if( DEBUG_FIXP16_32 == True):
        print(f"number of mismatches: {mismatch_count_fixp16_32}, total tests: {fp16_32_TotalTests} ")

# Example usage:
# process_input("DPUrel0_parametric_results.txt")

