import random

# Open file for writing
with open("output.txt", "w") as file:
    
    file.write(f"# widthSeld, typeSel, A0_8, A1_8, A2_8, A3_8, B0_8, B1_8, B2_8, B3_8, C0_8, A0_16, A1_16, A2_16, A3_16, B0_16, B1_16, B2_16, B3_16, C0_16, A0_32, A1_32, A2_32, A3_32, B0_32, B1_32, B2_32, B3_32, C0_32  \n" )
    
    for _ in range(10000):
        widthSel = random.randint(0, 2)  # integer between 0 and 2 inclusive
        typeSel = random.randint(0, 1)  # integer between 0 and 1 inclusive
        
        
        #random A,B,C0 (8 bits)
        A0_8 = random.randint(0, 255) 
        A1_8 = random.randint(0, 255) 
        A2_8 = random.randint(0, 255)
        A3_8 = random.randint(0, 255)
        B0_8 = random.randint(0, 255)
        B1_8 = random.randint(0, 255) 
        B2_8 = random.randint(0, 255) 
        B3_8 = random.randint(0, 255)
        C0_8 = random.randint(0, 255)
        
        #random A,B,C0 (16 bits)
        A0_16 = random.randint(0, 65535) 
        A1_16 = random.randint(0, 65535) 
        A2_16 = random.randint(0, 65535)
        A3_16 = random.randint(0, 65535)
        B0_16 = random.randint(0, 65535)
        B1_16 = random.randint(0, 65535) 
        B2_16 = random.randint(0, 65535) 
        B3_16 = random.randint(0, 65535)
        C0_16 = random.randint(0, 65535)
        
        #random A,B,C0 (32 bits)
        A0_32 = random.randint(0, 4294967295) 
        A1_32 = random.randint(0, 4294967295) 
        A2_32 = random.randint(0, 4294967295)
        A3_32 = random.randint(0, 4294967295)
        B0_32 = random.randint(0, 4294967295)
        B1_32 = random.randint(0, 4294967295) 
        B2_32 = random.randint(0, 4294967295) 
        B3_32 = random.randint(0, 4294967295)
        C0_32 = random.randint(0, 4294967295)
        
        hex_A0_8 = format( A0_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_A1_8 = format( A1_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_A2_8 = format( A2_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_A3_8 = format( A3_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_B0_8 = format( B0_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_8 = format( B1_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_8 = format( B1_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_B2_8 = format( B2_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_B3_8 = format( B3_8, '02X') #2-digit upper case hex without the 0x prefix
        hex_C0_8 = format( C0_8, '02X') #2-digit upper case hex without the 0x prefix
        
        hex_A0_16 = format( A0_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_A1_16 = format( A1_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_A2_16 = format( A2_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_A3_16 = format( A3_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_B0_16 = format( B0_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_16 = format( B1_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_16 = format( B1_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_B2_16 = format( B2_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_B3_16 = format( B3_16, '02X') #2-digit upper case hex without the 0x prefix
        hex_C0_16 = format( C0_16, '02X') #2-digit upper case hex without the 0x prefix
        
        hex_A0_32 = format( A0_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_A1_32 = format( A1_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_A2_32 = format( A2_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_A3_32 = format( A3_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_B0_32 = format( B0_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_32 = format( B1_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_B1_32 = format( B1_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_B2_32 = format( B2_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_B3_32 = format( B3_32, '02X') #2-digit upper case hex without the 0x prefix
        hex_C0_32 = format( C0_32, '02X') #2-digit upper case hex without the 0x prefix
        
        file.write(f"{widthSel} {typeSel} {hex_A0_8} {hex_A1_8} {hex_A2_8} {hex_A3_8} {hex_B0_8} {hex_B1_8} {hex_B2_8} {hex_B3_8} {hex_C0_8} {hex_A0_16} {hex_A1_16} {hex_A2_16} {hex_A3_16} {hex_B0_16} {hex_B1_16} {hex_B2_16} {hex_B3_16} {hex_C0_16} {hex_A0_32} {hex_A1_32} {hex_A2_32} {hex_A3_32} {hex_B0_32} {hex_B1_32} {hex_B2_32} {hex_B3_32} {hex_C0_32}\n")


