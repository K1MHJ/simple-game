import ctypes

PATH_TO_LIB = "./libDyn/libDyn.so"
libc = ctypes.CDLL(PATH_TO_LIB)
ret = libc.Add(1,3)
print(ret)
