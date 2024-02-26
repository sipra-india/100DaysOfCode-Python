def format_name(fName,lName):
    fName = fName.title()
    lName = lName.title()
    return fName+" "+lName

firstNm = input("Enter your first name...")
lastNm = input("Enter your last name...")

print()

print("Hell0,", format_name(firstNm, lastNm))
