#STRING DATA TYPE

#CONCATINATION
a="mamatha"
b="bm"
c=a+" "+b
print(c)

#REPEATATION
a="error! "
print(a*4)

#STRING METHOD
name=" Mamatha "
print(name.upper())
print(name.lower())
print(name.replace("Mamatha","spoorthi"))
print(name.strip())


#STRING LENGTH
name="Mamatha"
print("length of the string is",len(name))

#printing sentence with double quotes and print multiple line 
sentence='Hello "mamatha"! How are you..'
print(sentence)

sentence2='''Hii mamatha how are you    
what are you studing '''                #instead of ''' this we can use \n in first line end 
print(sentence2)

#ACCESSING STRING CHARACTER
s_name="Hemashre"
print(s_name[2])
print(s_name[1:5])     #it will not consider 5th index values
print(s_name[0: ])      #it will print all the character start from 0th index
print(s_name[ :5])      #it will print from index 0 to index 4

print(s_name[ : :2])     #to print alternative characters

#accesing from reverse index value
print(s_name[-1])   #reverse index start from -1 not -0







































