def calculateAge (currYear, yearOfBirth):
    age = yearOfBirth - currYear
    return age

def userInputDates():
    yearOfBirth = int(input("What year were you born??"))
    currYear = int(input("What year are we in?"))
    return calculateAge(yearOfBirth, currYear)

print (userInputDates())

    