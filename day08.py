#Conditional statements (if, elif, else)

signal=input("whats the signal color: ")

if signal=="green":
    print("GO")
elif signal=="yellow":
    print("ready")
elif signal=="red":
    print("stop")
else:
    print("invalid signal light")

#Logical operator
#example 1
if 5>3 and 10<20:
    print("accept")
else:
    print("reject")

#example 2
att=40
tea_frnd=True
if att>75 or tea_frnd:
    print("exam is given")
else:
    print("exam is not given")

#Nested if statement
gender="female"
age=22

if gender=="female":
    print("ticket is free")
else:
    if age <5:
        print("ticket is free")

    elif age<=12:
        print("half ticket")
    elif age>=60:
        print("senior citizen")
    else:
        print("full ticket")


#loop

#example 1
is_failed=True
i=1
while is_failed:
    if i%2 !=0:
        i=i+1
        continue
    print(f"attempt {i}")
    i=i+1
    if i>=10:
        break

    #Nestead while loop
    i=0
    while i<=10:
        x=0
        while x<i:
            print("mamatha", end=" ")
            x+=1
        print(" ")
        i+=1

        #example 2

        pin=1234
        trial=0
        while trial<3:
            pin_input=int(input("enter ATM pin"))
            trial+=1

            if pin_input==pin:
                print
                ("correct")
                break
            else:
                print("Not correct")
             


