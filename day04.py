#ASSIGNING OPERATOR
x=5   #assigning 5 to x
x+=3  #equal to x=x+3
x-=2 #equal to x=x-2
x*=4 #equal to x=x*4
x/=2 #equal to x=x\2

#COMPARISSION OPERATOR

a=10
b=20
print(a==b)   #False
print(a!=b)   #True
print(a>b)    #False
print(a<b)    #True
print(a>=10)   #True
print(a<=25)   #True

#LOGICAL OPEARATOR
print(1>3 or 5>2)    # or operator

print(3>1 and 2<5)   # and opearator

print(not(5>2))      #not opearator it will return the complementary 

#MEMBERSHIP OPERATOR(TYPES  1-> in  2-> not)

my_list={1,2,3,4,5}
my_string="python"
print(2 in my_list)
print(8 not in my_list)
print("p" in my_string)
print("z" not in my_string )

#BITWISE OPERATOR

a=5   #in binary 101
b=3   # in binary 011

print(a & b)    #bitwise AND,  output:1(001)
print(a | b)    #bitwise OR ,  output:7 (111)
print(~a)       #bitwise NOT,  output:-6
print(a << 1)   #left shift,   output:10(1010)
print(a >> 1)   #Right shift,  output:2(010)



