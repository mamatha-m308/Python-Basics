# Dictionary(collection of key value pair,mutable,unorder)
dictionary={"name":"mamatha", "gender":"F"}

#accesing dictionary element(2 ways)
print(dictionary["name"])
print(dictionary.get("name12","not found"))

#adding and updating dictionary and removing from dictionary
dictionary["age"]=21                 #adding
dictionary["name"]="Mamatha M"       #updating
dictionary.pop("gender")             #removing
print(dictionary)

#print only keys and values and items
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())


#In dictionary we can store different datatypes
dictitems={
"name":"mamatha",
"age":20,
"weight":45.6,
"is_student":True
}
    

#simple addition operation
item1={
    "name":"sugar",
    "weight": 2,
    "price":200
}

item2={
    "name":"onion",
    "weight": 5,
    "price":500
}

item=(item1,item2)
print(item)

print(f" total weight is {item1["weight"]+item2["weight"]}")





