from Crypto.Util.number import *
from gmpy2 import *

p=getPrime(1024)   # Modify the bit number of p and q
q=getPrime(1024)
N=p*q*p*q  #N=p^2 q^2

import time
from random import *
rs=[randrange(1,p*q) for i in range(1000)] # Generate 1000 indices
#r^n mod n^2
r=randrange(1,p*q) # 产生一个随机底数

start_time=time.time()
for i in rs:
    pp=powmod(r,i,N)  #calculate r^i mod N
end_time=time.time()
all_time=end_time-start_time
print("{:.4f}".format(all_time/1000))  #divide 1000
