from fxpmath import Fxp

#x = Fxp(-7.25) 
#x.info()

A0 = Fxp(1.5, signed=True, n_word=8, n_frac=5)
#print(f"A0: {A0.hex()}")
#x.info()

A1 = Fxp(-2.75, signed=True, n_word=8, n_frac=5)
#print(f"A1: {A1.hex()}")

A2 = Fxp(0.25, signed=True, n_word=8, n_frac=5)
#print(f"A2: {A2.hex()}")

A3 = Fxp(-3.5, signed=True, n_word=8, n_frac=5)
#print(f"A3: {A3.hex()}")

B0 = Fxp(-1, signed=True, n_word=8, n_frac=5)
#print(f"B0: {B0.hex()}")

B1 = Fxp(0.5, signed=True, n_word=8, n_frac=5)
#print(f"B1: {B1.hex()}")

B2 = Fxp(2, signed=True, n_word=8, n_frac=5)
#print(f"B2: {B2.hex()}")

B3 = Fxp(-.75, signed=True, n_word=8, n_frac=5)
#print(f"B3: {B3.hex()}")

C0 = Fxp(3.125, signed=True, n_word=16, n_frac=10)    
#print(f"C0: {C0.hex()}")    

result1 = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0

#print(f"result:{result1.hex()}")

# Example: 0xA8 as raw 8-bit signed fixed-point in Q2.5

raw_value = '0x1504'                
A0 = Fxp(signed=True, n_word=16, n_frac=10)
A0.set_val(raw_value, raw=True)
print(f"A0: {A0.hex()} | {A0} ")

raw_value = '0x1909' #DEVE ESSERE STRINGA quindi metto i " '' " in mezzo al numero             
A1 = Fxp(signed=True, n_word=16, n_frac=10)
A1.set_val(raw_value, raw=True)
print(f"A1: {A1.hex()} | {A1}")

raw_value = '0xd741'                
A2 = Fxp( signed=True, n_word=16, n_frac=10)
A2.set_val(raw_value, raw=True)
print(f"A2: {A2.hex()} | {A2}")

raw_value = '0x27d4'                
A3 = Fxp( signed=True, n_word=16, n_frac=10)
A3.set_val(raw_value, raw=True)
print(f"A3: {A3.hex()} | {A3}")

raw_value = '0x110e'                
B0 = Fxp(signed=True, n_word=16, n_frac=10)
B0.set_val(raw_value, raw=True)
print(f"B0: {B0.hex()} | {B0}")

raw_value = '0x8fc9'                
B1= Fxp(signed=True, n_word=16, n_frac=10)
B1.set_val(raw_value, raw=True)
print(f"B1: {B1.hex()} | {B1}")

raw_value = '0xea08'                
B2 = Fxp(signed=True, n_word=16, n_frac=10)
B2.set_val(raw_value, raw=True)
print(f"B2: {B2.hex()} | {B2}")

raw_value = '0x236f'               
B3 = Fxp(signed=True, n_word=16, n_frac=10)
B3.set_val(raw_value, raw=True)
print(f"B3: {B3.hex()} | {B3}")

raw_value = '0xe0ef10fe'                
C0 = Fxp(signed=True, n_word=32, n_frac=20)
C0.set_val(raw_value, raw=True)
print(f"C0: {C0.hex()} | {C0}")

raw_value = '0xe05e8f3b'
resultFromCircuit= Fxp(signed=True, n_word=32, n_frac=20)
resultFromCircuit.set_val(raw_value, raw=True) 
print(f"resultFromCircuit: {resultFromCircuit.hex()} | {resultFromCircuit}")

print(f"resultFromSimulation: { (float(A0) * float(B0)) + (float(A1) * float(B1)) + (float(A2) * float(B2)) + (float(A3) * float(B3)) + float(C0)}")

supposedTOBE = Fxp(-33.44921875, signed=True, n_word=16, n_frac=10)  
print(f"{supposedTOBE.hex()}")

#print(f"result1: {result1}")

print(f"Real values used: A0={float(A0)} A1={float(A1)} A2={float(A2)} A3={float(A3)} B0={float(B0)} B1={float(B1)} B2={float(B2)} B3={float(B3)} C0={float(C0)}")    