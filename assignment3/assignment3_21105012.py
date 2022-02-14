"""1. Write a Python program to count the number of occurrences of each word or
character in the string entered by the user. (Count the Number of Occurrences
of each character only if the single word is entered by the user)."""
print("program1")

#take input string
input_str = input("Enter text here\n")
if (" " not in input_str):
    word_count = {}

    for i in input_str:
        word_count[i] = input_str.count(i)
    print(word_count)
else:
    print("The input should not start with space.")

"""2. Write a python script to print next date of input date. It must meet following
conditions(use if-elif)
C1:1<=month<=12
C2:1<=day<=31
C3:1800<=year<=2025
E.g.:
Input: Day - 28
Month -02
Year -1999
Output: Next Date is: 1/03/1999"""

print("program2")
dt = int(input("Day-"))
mnth = int(input("Month-"))
yr = int(input("Year-"))

if (yr%4==0):
    if (yr%400==0):
        leap_yr = True
    elif (yr%100!=0):
        leap_yr = True
else:
    leap_yr = False

def last_date(month):
    if (month%2==1):
        if (month<=7):
            lst_dt = 31
        if (month>7):
            lst_dt = 30
    if (month%2==0 and month!=2):
        if (month<=7):
            lst_dt = 30
        if (month>7):
            lst_dt = 31
    if (month==2):
        if leap_yr==True:
            lst_dt = 29
        if leap_yr==False:
            lst_dt = 28
            if dt==29:
                print("Invalid Input. Please try again!")
    return lst_dt

if (1<=mnth and mnth<=12 and 1<=dt and dt<=31 and 1800<=yr and yr<=2025):
    if (dt<=last_date(mnth)):
        if (dt==last_date(mnth) and mnth!=12):
            dt = 1
            mnth = mnth+1
        elif (dt==31 and mnth==12):
            dt = 1
            mnth = 1
            yr = yr+1
        else:
            dt = dt+1
        print(f"Next date is: {dt}/{mnth}/{yr}")
else:
    print("Error!! Not in Range.")

"""3. Write a Python program to create a list of tuples with the first element as the
number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""

print("program3")
my_list = [3, 9, 10]
sq_list = []
for i in my_list:
    sq_tup = (i, i**2)
    sq_list.append(sq_tup)
print(sq_list)

"""4. Write a program to prompt the user for a grade between 4 and 10. If the grade
is out of range print error message. If the grade is between 4 and 10 Print the
grade and the performance using the following:
Letter Grade Performance Grade Points
A+    Outstanding 10
A     Excellent 9
B+    Very Good 8
B     Good 7
C+    Average 6
C     Below Average 5
D     Poor 4

E.g.: For Grade 9 Output is:
Your Grade is ‘A’ and Excellent Performance."""

print("program4")
grd_pt = int(input("Grade:- "))
print("For Grade", grd_pt, "Output is:")
if (grd_pt>=4 and grd_pt<=10):
    if (grd_pt == 4):
        ltr_grd = "D"
        perf = "poor"
    elif (grd_pt == 5):
        ltr_grd = "C"
        perf = "below average"
    elif (grd_pt == 6):
        ltr_grd = "C+"
        perf = "average"
    elif (grd_pt == 7):
        ltr_grd = "B"
        perf = "good"
    elif (grd_pt == 8):
        ltr_grd = "B+"
        perf = "very good"
    elif (grd_pt == 9):
        ltr_grd = "A"
        perf = "excellent"
    elif (grd_pt == 10):
        ltr_grd = "A+"
        perf = "outstanding"
    print(f"Your Grade is '{ltr_grd}' and {perf} performance.")

else:
    print("Error!! Grade is out of range.")

"""5. Write a python program to print following pattern.
ABCDEFGHIJK
ABCDEFGHI
ABCDEFG
ABCDE
ABC
A"""

print("program5")
n = int(input("number:"))

a2z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    if 2*i<n:
        j = a2z[:n-2*i]

        print(" "*i, j)


"""6. Write a python script that repeatedly ask user to enter name and SID of
students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and
values are student’s name. Perform the following operations on Dictionary :
a. Print students details stored in the dictionary.
b. Sort dictionary using student names.
c. Sort dictionary using SID.
d. Search a student details with SID and print name of that student."""

print("Program6")
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
list_sid=[]
#List containing Y or N
liste=["Y","y","n","N"]
#Main code
while repeat=="Y" or repeat=="y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    while sid in list_sid:
        print("\nThis SID is already entered:\nPlease enter unique SID\n")
        sid=int(input("Enter student SID:"))
    list_sid.append(sid)
    while sid<0:
        print("\nError\nSID can't be negative\n")
        sid=int(input("Enter student SID:"))
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'(will be helpful while sorting)
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    while (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")

"""7. Write a python program to print Fibonacci sequence also print average of the
resultant Fibonacci series."""

print("program7")
def fibo(n):
    if n==1 or n==2:
        return 1

    return fibo(n-1)+fibo(n-2)

n = int(input("Enter n\n"))

j = 0

for i in range(1, n+1):
    print(f"{fibo(i)}", end = ",")
    j = j+fibo(i)

print(end = "\n")
print(j/n)

"""8. Given the sets below, write python statement to:
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
a. Create a new set of all elements that are in Set1 and Set2 but not both.
b. Create a new set of all elements that are in only one of the three sets Set1,
Set2 and Set3.
c. Create a new set of elements that are exactly two of the sets Set1, Set2
and Set3.
d. Create a new set of all integers in the range 1 to 10 that are not in Set1.
e. Create a new set of all integers in the range 1 to 10 that are not in Set1,
Set2 and Set3."""

print("Program8")
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

set_a = (set1 | set2) - (set1 & set2)
print("part a:", set_a)

set_b = (set1 | set2 | set3) - (set1 & set2) - (set2 & set3) - (set3 & set1)
print("part b:", set_b)

set_c  =(set1 & set2) | (set2 & set3) | (set3 & set1) | (set1 & set2 & set3)
print("part :", set_c)

set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Elements in Range (1, 10) but not in Set1
set_d = set4 - set1
print("part d:", set_d)

# Elements in Range (1, 10) but not in Set1, Set2 and Set3
set_e = set4 - (set1 | set2 | set3)
set_esorted = sorted(set_e)
print("part e:", set_esorted)
