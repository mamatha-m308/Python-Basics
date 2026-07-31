list=[1,2,3,4,5]  #sum of all the numbers in list
sum=0
for i in list:
    sum=sum+i
print(sum)


list1=[1,2,3,4,5]   #append double values to the list2
list2=[]
for i in list1:
    list2.append(i*2)
print(list2)
#OR
listt1=[1,2,3,4,5]
listt2=[item*2 for item in listt1]
print(listt2)


l=[x for x in range(1,11)]
dl=[x**2 for x in l if x%2==0]
print(dl)



d={"name":"spoorthi", "age":20}
for key,value in d.items():
    print(f"{key}- {value}")



stu=["mamatha","spoorthi","hema"]          #for loop  in list
marks=[32,34,35]
stu_marks={}
for index,students in enumerate(stu):
    stu_marks[students]=marks[index]
print(stu_marks)

#or

stu=["mamatha","spoorthi","hema"]
marks=[32,34,35]
stu_marks={}
for i in range(1,len(stu)):
    stu_marks[stu[i]]=marks[i]
print(stu_marks)


#list comprehension
l=[1,2,3,4,5]
dl=[item*2 for item in l]         #dl=[exp for item in collection]
print(dl)                           


#create list 
l=[x for x in range(1,11)]
print(l)

#do square for only even numbers
edl=[x**2 for x in l if x%2==0]
print(edl)


#print the 2nd letter in string
str=["mamatha","spoorthi"]
stltr=[x[1] for x in str]
print(stltr)

#print name and length of the name in dictionary
names=["mamatha","spoorthi","hema"]
d={name:len(name) for name in names}
print(d)

#print large city if population is grater then 10
cp={"banglore":70,"mysore":60,"hasan":40}
d={city:pop for city,pop in cp.items() if pop>50}
print(d)

#splitting strings to create a list
s="this is a word"
l=s.split()
print(l)

st="this-is-word"
ls=st.split("-")
print(ls)

#take integer input for list
x=input("enter list of nbrs").split()
d=[int(num) for num in x ]
print(d)
print(type(d))


#print list in decending order
l=[1,2,3,4]
print(l.sort(reverse=True))