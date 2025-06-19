from sfpy import Posit8
from sfpy import Posit16
from sfpy import Float16
from sfpy import Float32
from ml_dtypes import float8_e4m3
import numpy as np

# Create a few test values
a = Posit8(1.0)
b = Posit8(2.0)
c = Posit8(4.0)
d = Posit8(8.0)
e = Posit8(16.0)
f = Posit8(32.0)
g = Posit8(64.0)
h = Posit8(128.0)
i = Posit8(256.0)


print('1.0 -> {}'.format(hex(a.bits) ) )
print('2.0 -> {}'.format(hex(b.bits) ) )
print('4.0 -> {}'.format(hex(c.bits) ) )
print('8.0 -> {}'.format(hex(d.bits) ) )
print('16.0 -> {}'.format(hex(e.bits) ) )
print('32.0 -> {}'.format(hex(f.bits) ) )
print('64.0 -> {}'.format(hex(g.bits) ) )
print('128.0 -> {}'.format(hex(h.bits) ) )
print('256.0 -> {}'.format(hex(i.bits) ) )

#chat gpt says that posit8 with es equal to 0 means that all scaling is  done via the regime
#the range when es field is 0 is roughly: min normal = ~2^-6, MAX IS AROUND ~64.0
#BEyond 64.0 it saturates to max value 0x7F.
#posits are symmetric - same rules for negatives, just mirrored.

#on the other hand, with es= 1 more bits are used for the exponent and fewwe bits are left for the fraction 
#this  changes where the boundaries are between scale levels (powers of 2)
#the encoding of values like 2.0, 4.0, 8.0, etc...
#the maximum value increases a bit (up to ~256 instead of ~64)
#you get more steps between powers of two due to the extra es bit.



op1 = Posit8.from_bits(0x05)
print(op1)
op2 =  op1 = Posit8.from_bits(0x02)
print(op2)
res = Posit8.from_bits(0x07)
print(res)  



op1 = Posit8.from_bits(0xbe)
print(op1)
op2 =  op1 = Posit8.from_bits(0x0d)
print(op2)
res = Posit8.from_bits(0xc9)
print(res)  


op1ForMul= Posit8.from_bits(0xF0)
op2ForMul= Posit8.from_bits(0xF4)
productRes= Posit8.from_bits(0x03)
print('{} * {} = {}'.format(op1ForMul, op2ForMul, productRes))


a0 = Posit8.from_bits(0x26)
a1 = Posit8.from_bits(0xc4)
a2 = Posit8.from_bits(0x6d)
a3 = Posit8.from_bits(0x7c)
b0 = Posit8.from_bits(0xde)
b1 = Posit8.from_bits(0x6e)
b2 = Posit8.from_bits(0x69)
b3 = Posit8.from_bits(0x22)
c0 = Posit8.from_bits(0x7f)
res = Posit8.from_bits(0x71)

print( '########## DPU sample test softPosit8 ########## ' ) 

print ( ' ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + {} = {} '.format(a0,b0,a1,b1,a2,b2,a3,b3,c0,res ) )

print('ACTUAL value: {}'.format( (float(a0)*float(b0)) + (float(a1)*float(b1)) + (float(a2)*float(b2)) + (float(a3)*float(b3)) + float(c0)  ) ) 


a0 = Posit16.from_bits(0x8000)
a1 = Posit16.from_bits(0x5d55)
a2 = Posit16.from_bits(0x05f1)
a3 = Posit16.from_bits(0xc973)
b0 = Posit16.from_bits(0x96e8)
b1 = Posit16.from_bits(0x0080)
b2 = Posit16.from_bits(0x549d)
b3 = Posit16.from_bits(0x9215)
c0 = Posit16.from_bits(0xc375)
res = Posit16.from_bits(0x2699)
#res2 = Posit16.from_bits(0x63f2)

print( '########## DPU sample test softPosit16 ########## ' ) 

#print ( ' ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + {} = fromSimulator: {} , fromGoldenVal : {} '.format( a0, b0, a1, b1, a2, b2, a3, b3, c0, res, res2 ) )

op1ForMul_16= Posit16.from_bits(0x7e88)
op2ForMul_16= Posit16.from_bits(0x0f01)
productRes_16= Posit16.from_bits(0x79be)
productRes2_16= Posit16.from_bits(0x79b9)
print('{} * {} = from simulator: {}, from golden : {}'.format(op1ForMul_16, op2ForMul_16, productRes_16, productRes2_16))

testingPosit16 = Posit16.from_bits(0xc973)
print('{}'.format(  testingPosit16  ) )


print( '########## DPU sample test FP 16 IEEE 754 ########## ' ) 

a0 = Float16.from_bits(0x44e8)
a1 = Float16.from_bits(0xbf33)
a2 = Float16.from_bits(0x488c)
a3 = Float16.from_bits(0x419d)
b0 = Float16.from_bits(0xc05e)
b1 = Float16.from_bits(0xc04b)
b2 = Float16.from_bits(0xc5b1)
b3 = Float16.from_bits(0xc888)
c0 = Float16.from_bits(0x474c)
res = Float16.from_bits(0xd4cc)
#res2 = Float16.from_bits(0xd4cb)

#print ( ' ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + {} = fromSimulator: {} , fromGoldenVal : {} '.format( a0, b0, a1, b1, a2, b2, a3, b3, c0, res, res2 ) )

print (' actual value: {} '.format( (a0*b0) + (a1*b1) + (a2*b2) + (a3*b3)  + c0 ) )

print( '########## DPU sample test FP 8 , sign 1 exponent 4 mantissa 3 ########## ' ) 


a0 = np.frombuffer(np.uint8(0xBA).tobytes(), dtype=float8_e4m3)[0]
a1 = np.frombuffer(np.uint8(0xC2).tobytes(), dtype=float8_e4m3)[0]
a2 = np.frombuffer(np.uint8(0xCE).tobytes(), dtype=float8_e4m3)[0]
a3 = np.frombuffer(np.uint8(0x39).tobytes(), dtype=float8_e4m3)[0]
b0 = np.frombuffer(np.uint8(0xCC).tobytes(), dtype=float8_e4m3)[0]
b1 = np.frombuffer(np.uint8(0xD0).tobytes(), dtype=float8_e4m3)[0]
b2 = np.frombuffer(np.uint8(0x3E).tobytes(), dtype=float8_e4m3)[0]
b3 = np.frombuffer(np.uint8(0xBB).tobytes(), dtype=float8_e4m3)[0]
c0 = np.frombuffer(np.uint8(0x48).tobytes(), dtype=float8_e4m3)[0]
res = np.frombuffer(np.uint8(0x59).tobytes(), dtype=float8_e4m3)[0]
res2 = np.frombuffer(np.uint8(0x59).tobytes(), dtype=float8_e4m3)[0]

print ( ' ( a0={} * b0={} ) + ( a1={} * b1={} ) + ( a2={} * b2={} ) + ( a3={} * b3={} ) + c0={} = fromSimulator: {} , fromGoldenVal : {} '.format( a0, b0, a1, b1, a2, b2, a3, b3, c0, res, res2 ) )

print (' actual value: {} '.format( (a0*b0) + (a1*b1) + (a2*b2) + (a3*b3)  + c0 ) )


print( '########## DPU sample test FP 32 IEEE 754 ########## ' ) 

a0 = Float32.from_bits(0xbee480be)
a1 = Float32.from_bits(0xbf508b56)
a2 = Float32.from_bits(0x3ef861be)
a3 = Float32.from_bits(0x3f292788)
b0 = Float32.from_bits(0xbe8f28d5)
b1 = Float32.from_bits(0xbf281115)
b2 = Float32.from_bits(0x3f070ec7)
b3 = Float32.from_bits(0x3f16dda3)
c0 = Float32.from_bits(0x3f27b357)
res = Float32.from_bits(0x3ffae1aa)
res2 = Float32.from_bits(0x3ffae1ab)

print ( ' ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + ( {} * {} ) + {} = fromSimulator: {} , fromGoldenVal : {} '.format( a0, b0, a1, b1, a2, b2, a3, b3, c0, res, res2 ) )

print (' actual value: {} '.format( (a0*b0) + (a1*b1) + (a2*b2) + (a3*b3)  + c0 ) )






