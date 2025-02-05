math=int(input("enter math marks: "))
reading=int(input("enter reading marks: "))
science=int(input("enter the marks in science: "))
total=math+reading+science
print("youre total marks is...",total)
bob=total/3
if bob<=100 and bob>=90:
    print("youre grade is A1")
elif bob>=80 and bob <90:
    print("youre grade is A2")
elif bob>=70 and bob<80:
    print("you get a B1")
elif bob>=60 and bob<70:
    print("you get a B2")
elif bob>=50 and bob<60:
    print("you get a C")
elif bob<50:
    print("YOU FAILED")
else:
    print("please enter valid input")