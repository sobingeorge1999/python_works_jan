def findgrade(totalscore):
    if totalscore <= 100:
        if totalscore >= 90:
            return ("A+")
        elif totalscore >= 80:
            return ("A")
        elif totalscore >= 70:
            return ("B+")
        elif totalscore >= 60:
            return ("B")
        elif totalscore >= 50:
            return ("C+")
        else:
            return ("fail")
    else:
        return ("invalid")
n=int(input("enter the mark"))
print(findgrade(n))
print(findgrade(44))