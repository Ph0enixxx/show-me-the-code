def gen(head="CX",endtime="2016.10.1",amount=200):
    salt = endtime + endtime + endtime
    for i in range(1,amount+1):
        yield head + str(abs(hash(str(i) + salt + str(i))))

x = gen()
print(list(x))

def check(f,code):
    x = f()
    if code in list(x):
        return True
    return False
