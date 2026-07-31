#For loop


for i in range(1,11):    #print 1 to 10 using for loop
    print(i)



for  i in range(1,11):   #print 10 to 10 only odd number
    if i%2!=0:
        print(i)
        i=i+1


bag=["red","blue","green"]   # for loop in  list
for ball in bag:
    print(ball)


name="mamatha"             # for loop in  string
for letter in name:
    print(letter*2)
my_name="mamatha"                         #print letter based on position
for index,letter in enumerate(my_name):
    print(letter*index)


l=[21,43,45,454,47]
for index, num in enumerate(l):
    print(f"number {num} in {index} th index")


#using else with for loop

num=[1,2,3,4,5]
for nbr in num:
    print(nbr)
    if nbr==4:
        break
else:
    print("all printed")

#for loop in dictionary
d={"name":"mamatha","gender":"female"}
for key, value in d.items():
    print(key,value)

#print table using for loop

for i in range(1,11):
    print(f"2X{i}={2*i}")
    

#print table from 2 to 10(nesting of loops)
for i in range(2,11):
    for j in range(1, 11):
        print(f"{i}X{j}={i*j}")

#PRACTICE QSNS
for i in  range(1,31):
    print(f"{3*i}")


sum=0
for i in range(0,11):
    sum=i+sum
    print(sum)


count=0
v='aeiou'
name="mamathi"
for i in name:
    for j in v:
        if i==j:
            count=count+1
print(count)
            
    


