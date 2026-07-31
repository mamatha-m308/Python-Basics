#Fnction (fnc is a reusable code)

def details(name,address):           #parameters
    print(f"{name} from {address}")
details("mamatha","chamarajanagar")   #positional arguments
details("spoorthi","mysore")

details(name="hema",address="mandya") #keyword argument



#print table using function

def table(num):
    for i in range(1,11):
         print(f"{num}X*{i}={num*i}")
table(5)
table(6)

#default parameter in function
def detail(name,address="delhi"):
    print(f"{name} from {address}")
detail("mamatha")


#return value from function
def func(num):
    return int(str(num)*3)
d=func(2)
print(d)
a=100
print(a+d)