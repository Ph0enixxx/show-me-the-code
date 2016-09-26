import redis
from data import Data

def gen(head="CX",endtime="2016.10.1",amount=200):
    salt = endtime + endtime + endtime
    for i in range(1,amount+1):
        yield head + str(abs(hash(str(i) + salt + str(i))))

x = gen()
d = Data(hashName = "0003")

print(123)
for i in list(x):
    d.set(i,i)


for i in list(x):
    print(d.get(i))
    print(1)
    
def check(f,code):
    x = f()
    if code in list(x):
        return True
    return False

print(check(gen,"CX4380371458663503116"))
d.set("asd","111")
print(d.get("CX3871706864350190952"))
