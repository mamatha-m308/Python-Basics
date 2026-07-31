#TUPLE
gender=("male","female","others")
print(len(gender))
print(gender[0])
print(gender[0:2])


tuple1=("mamatha","spoorthi")       #tuple concatination
tuple2=("hema","nandu")
combinetuple=tuple1+tuple2
print(combinetuple)

print("mamatha" in tuple1)   #membership 

repeat_tuple=(1,2)*3         #repeatation
print(repeat_tuple)

#tuple methods
tup_1=("banana","gova","orange","banana")   
print(tup_1.count("banana"))      #count nbr of accurance
print(tup_1.index("gova"))        #to print index values

tuple_t=("mamatha","spoorthi",(1,2,3))   #matrics in tuple
print(tuple_t)

# SETS IN PYTHON
set_1={1,2,3}
print(set_1)

#set operation
s1={1,2,3}
s2={3,4,5}
print(s1 | s2)        #return union
print(s1 & s2)        #return intersection
print(s1 - s2)        #difference output:1,2

#set methods
s={1,2,3,4}
s.add(10)     #add item to tuple
print(s)

s.remove(1)   #remove item from tuple 
print(s)

s.discard(10)  #remove item from tuple 
print(s)

s.pop()
print(s)
