#variable length arguments(*args , **kwargs)

#*args
def add(*numbers):           
    return sum(numbers)
print(add(1,2,3,4))

#**kwargs
def stu_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
stu_info(name="mamatha", marks=100)

#*args
def avrg(*a):
    cnt=0
    ttl=0
    for i in a:
        ttl=ttl+i
        cnt+=1
    return ttl/cnt
print(avrg(1,2,3))



#lamda function(its a anonymous function. i can take any nbr of arguments but only one expression)
double_num= lambda x:x*2
print(double_num(5))

#assending order
students=[
        {"name":"mamatha","marks":100},
          {"name":"spoorthi","marks":50}
          ]
students.sort(key=lambda x:x["marks"])
print(students)

#descending order
students=[
        {"name":"mamatha","marks":100},
          {"name":"spoorthi","marks":50}
          ]
students.sort(key=lambda x:x["marks"],reverse=True)
print(students)

#Recursion(Recursion occurs when a function calls itself)

def factorial(n):             #example 1
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))

def sum(n):                    #example 2
    if n==1:
        return 1
    return n+sum(n-1)
print(sum(3))

#Nested function(function inside a function)
def calc(a,b):
    def sum():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    sum()
    sub()
    mul()
calc(2,4)




