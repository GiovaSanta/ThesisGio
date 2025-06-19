import sys
import random
import numpy as np
from sfpy import Posit8, Posit16, Posit32, Float32, Float16
from ml_dtypes import float8_e4m3

special_values = [0x00, 0x80, 0xFF, 0x40, 0xC0, 0x01, 0x7F]

formats = {
    "posit8": {
        "class": Posit8,
        "bit_width": 8,
        "max_val": 255,
    },
    "posit16": {
        "class": Posit16,
        "bit_width": 16,
        "max_val": 65535,
    },
    "posit32": {
        "class": Posit32,
        "bit_width": 32,
        "max_val": 4294967295,
    },
    "ieeefp16": {
        "class": np.float16,
        "bit_width": 16,
        "max_val": None,
    },
    "float8_e4m3": {
        "class": float8_e4m3,
        "bit_width": 8,
        "max_val": None,
    },
    "ieeefp32": {
        "class": np.float32,
        "bit_width": 32,
        "max_val": None,
    },
    "int8_int16out": {
        "bit_width": 8,
        "input_type": "int8",
        "acc_type": "int16",
        "max_val": 127,
        "min_val": -128,
    }
}

def generate_test_vector(fmt):
    fmt_info = formats[fmt]
    bw = fmt_info["bit_width"]

    # Floating point and ML float8 formats
    if fmt.startswith("ieeefp") or fmt == "float8_e4m3" or fmt.startswith("posit"):
        dtype = fmt_info["class"]
        ops = [dtype(np.random.uniform(-10, 10) ) for _ in range(9)]
        print('ops: {}'.format( ops ) )

        try:
            result = ops[0]*ops[4] + ops[1]*ops[5] + ops[2]*ops[6] + ops[3]*ops[7] + ops[8]
            #print(result)
            
            if fmt == "ieeefp16" :
                result_bits = format((Float16(result)).bits, '04X')
                #print('-')
                
            elif fmt == "ieeefp32" :
                result_bits = format((Float32(result)).bits, '08X')
                #print('.')
                
            elif fmt == "float8_e4m3" :
                #print('+')
                
                encoded = np.array([result], dtype)
                print(encoded)  
                #print('+')
                result_bits = format(encoded.view(np.uint8)[0], '02X')
                print('{}'.format(result_bits))
           
            elif fmt == "posit32" :
                result_bits = format((Posit32(result)).bits, '08X')
               
            elif fmt == "posit16" :
                result_bits = format((Posit16(result)).bits, '04X')
               
            elif fmt == "posit8" :
                result_bits = format((Posit8(result)).bits, '02X')
                
        except:
            result_bits = "FF" * (bw // 8)
       
        if fmt == "ieeefp32" :
            hex_ops = [ format((Float32(x)).bits, '08X') for x in ops]
        elif fmt == "ieeefp16" :
            hex_ops = [format((Float16(x)).bits, '04X') for x in ops ]
        elif fmt == "float8_e4m3" :
            hex_ops = [format( (np.array([x], dtype) ).view(np.uint8)[0]  , '02X') for x in ops ]
            print(hex_ops)
        elif fmt == "posit32" :
            hex_ops = [ format((Posit32(x)).bits, '08X') for x in ops]
        elif fmt == "posit16" :
            hex_ops = [format((Posit16(x)).bits, '04X') for x in ops ]
        elif fmt == "posit8" :
            hex_ops = [format((Posit8(x)).bits, '02X') for x in ops ]

        return " ".join(hex_ops + [result_bits])

    elif fmt == "int8_int16out":
        # Generate random inputs
        a_vals = [np.random.randint(-50, 50, dtype=np.int8) for _ in range(4)]
        b_vals = [np.random.randint(-50, 50, dtype=np.int8) for _ in range(4)]
        c0     = np.random.randint(-32768, 32768, dtype=np.int16)
        
        print('a_vals : {}'.format( a_vals) )
        print('b_vals : {}'.format( b_vals) )
        print('c0 : {}'.format( c0) )

        # Do the computation in int16
        products = [np.int16(a_vals[i]) * np.int16(b_vals[i]) for i in range(4)]
        print(products)
        result = np.int16(sum(products) + c0)
        
        print('result :{}'.format( result ) )

        def to_hex(val, width):
            val = int(val)  # <-- cast to Python int
            if width == 8:
                return val.to_bytes(1, byteorder='big', signed=True).hex().upper()
            elif width == 16:
                return val.to_bytes(2, byteorder='big', signed=True).hex().upper()

        hex_ops = [to_hex(x, 8) for x in a_vals + b_vals]
        #print(hex_ops)
        hex_ops.append( to_hex(c0, 16) )
        hex_ops.append( to_hex(result ,16) )
        
       	print(hex_ops)

        return " ".join(hex_ops)

    # Posit formats
    #else:
    #    fmt_class = fmt_info["class"]
    #    ops = [random.choice(special_values) if random.random() < 0.1 else random.randint(0, fmt_info["max_val"]) for _ in range(9)]
    #    ps = [fmt_class.from_bits(x) for x in ops]
    #    try:
    #        result = ps[0]*ps[4] + ps[1]*ps[5] + ps[2]*ps[6] + ps[3]*ps[7] + ps[8]
    #        result_bits = f"{fmt_class(result).bits:0{bw//4}X}"
    #    except:
    #        result_bits = "FF" * (bw // 8)
    #    return " ".join(f"{x:0{bw//4}X}" for x in ops) + f" {result_bits}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python dotproduct_generator.py <format>")
        print(f"Supported formats: {', '.join(formats.keys())}")
        return
    fmt = sys.argv[1]
    if fmt not in formats:
        print(f"Unknown format: {fmt}")
        return
    filename = f"dotproduct_{fmt}_tests.txt"
    with open(filename, "w") as f:
        for _ in range(10000):
            f.write(generate_test_vector(fmt) + "\n")
    print(f"✅ Generated 10000 test vectors in '{filename}'.")

if __name__ == "__main__":
    main()

