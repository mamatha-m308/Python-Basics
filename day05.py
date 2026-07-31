#list
list=["banana","papaya","orange"]
print(list[0])
list.pop()    #remove last element in list
print(list)
     
list1=[1,2,3,4]
list1.pop(1)    #remove particular element
print(list1)     

list3=["a","b","C","d"]
list3.remove("b")  #remove particular element           
print(list3)      


list4=["mamatha","soorthi","nandu"]
list4.append("hema")   #add element to last
print(list4)      

list5=["mamatha","spoorthi","nandu"]
list5.insert(2,"hema")  #add element in a particular index
print(list5)    

list6=[1,2,3,4]
list6.clear()    #to delete the entire list

print(list6)            

list7=["mysore","hasan"]
list7[0]="gova"            #to update the particular values
print(list7)


#Slicing list
items=["a","b","c","d"]
print(items[0:2])    #a c
print(items[1:3])    #b c 
print(items[1: ])    #b c d 
print(items[0: :2])  #a c

#list functions
mylist=[14,16,12,11,11]
print(len(mylist))
print(sorted(mylist))
print(sum(mylist))
print(mylist.index(12))
print(mylist.count(11))

mylist.reverse()
print(mylist)
#or
mylist[::-1]
print(mylist)

#2D Matrix
matrix=[
    [1,2,3],          #nesting
    [4,5,6],
    [7,8,9]
]

print(matrix[0])      #[1,2,3]
print(matrix[1][1])   #[5]
