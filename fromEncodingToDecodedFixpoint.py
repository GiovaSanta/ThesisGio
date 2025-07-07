from fxpmath import Fxp

import fxpmath, inspect

x = Fxp(signed=True, n_word=8, n_frac=5)
x.set_val('0xDB', raw=True)   # <- this is the correct way in v0.4.9

print("binary :", format(0xDB, '08b'))   # 11011011
print("as int:", int(x))                # -37
print("as float:", float(x))            # -1.15625


print(fxpmath.__version__)
print(inspect.signature(fxpmath.Fxp))