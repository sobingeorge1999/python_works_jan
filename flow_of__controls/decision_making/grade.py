# totalscore
# 90 100 a+
# 80 90 a
#
# below 50 fail
totalscore =int(input("enter the total score"))
if totalscore<=100:
    if totalscore>=90:
        print("A+")
    elif totalscore>=80:
        print("A")
    elif totalscore>=70:
        print("B+")
    elif totalscore>=60:
        print("B")
    elif totalscore>=50:
        print("C+")
    else:
        print("fail")
else:
    print("invalid")