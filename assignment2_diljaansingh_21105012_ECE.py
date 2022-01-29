print("program1a")
ourstr="Python is a case sensitive language"
print(len(ourstr))

print("program1b")
ourstr="Python is a case sensitive language"
print(ourstr[::-1])

print("program1c")
ourstr="Python is a case sensitive language"
mystr=ourstr[10:26]
print(mystr)

print("program1d")
ourstr="Python is a case sensitive language"
print(ourstr.replace("a case sensitive","object oriented"))

print("program1e")
ourstr="Python is a case sensitive language"
print(ourstr.find("a"))

print("program1f")
ourstr="Python is a case sensitive language"
print(ourstr.replace(" ","")

print("program2")
x=input("enter your name \n")
y=input("your SID \n")
z=input("department name\n")
p=input("YOUR CGPA\n")
print("Hey",x, "here!")
print("MY SID IS",y)
print("I am from",z,"department and CGPA IS",p)

a=56
b=10
print("program3a")
print(a&b)

print("program3b")
print(a|b)

print("program3c")
print(a^b)

print("program3d")
print(a<<2)
print(b<<2)

print("program3e")
print(a>>2)
print(b>>4)

print("program4")
x=int(input("numb1"))
y=int(input("numb2"))
z=int(input("numb3"))
if x>y:
    if x>z:
        print(x,"is the greatest no")
    else:
        print(z,"is the greatest number")
else:
    if y>z:
        print(y,"is the greatest number")
    else:
        print(z,"is the greatest number")

print("program5")
x=input("enter your str \n")
if "name" in x:
    print("yes")
else:
    print("no")

print("program6")
x=int(input("length of first side\n"))
y=int(input("length of second side\n"))
z=int(input("length of third side\n"))
if x+y<=z or y+z<=x or x+z<=y:
    print("no")
else:
    print("yes")
