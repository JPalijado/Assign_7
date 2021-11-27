def InputPassword():
    password = str(input("Enter Password: "))
    return password

def VerifyPwLenght(password):
    pwlength = len(password)
    return pwlength

def VerifyCapitalLetter(password):
    countCapitalLetter = 0
    for capitalLetter in password:
        if capitalLetter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            countCapitalLetter = countCapitalLetter + 1
            totalCapitalLetter = countCapitalLetter
    if countCapitalLetter == 0:
        totalCapitalLetter = 0
    return totalCapitalLetter

def VerifyNumber(password):
    countNumber = 0
    for number in password:
        if number in "1234567890":
            countNumber = countNumber + 1
            totalNumber = countNumber
    if countNumber == 0:
        totalNumber = 0
    return totalNumber

def VerifySpecialCharacter(password):
    countSpecialCharacter = 0
    for specialCharacter in password:
        if specialCharacter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ":
            countSpecialCharacter = countSpecialCharacter + 1
            totalSpecialCharacter = countSpecialCharacter
    if countSpecialCharacter == 0:
        totalSpecialCharacter = 0
    return totalSpecialCharacter    

def DisplayOuput(pwlength,totalCapitalLetter, totalNumber, totalSpecialCharacter):
    if pwlength > 15 and totalCapitalLetter >= 1 and totalNumber >= 1 and totalSpecialCharacter >= 1:
        print("Verdict: Valid Password")
    else:
        print("Verdict: Invalid Password\n\nThe password must have the following:")
        if pwlength <= 15:
            print("- More than fifteen (15) characters")
        if totalCapitalLetter == 0:
            print("- At least one (1) capital letter")
        if totalNumber == 0:
            print("- At least one (1) number")
        if totalSpecialCharacter == 0:
            print("- At least one (1) special character (!@#$%^&*,etc.)")

password = InputPassword()

pwlength = VerifyPwLenght(password)
totalCapitalLetter = VerifyCapitalLetter(password)
totalNumber = VerifyNumber(password)
totalSpecialCharacter = VerifySpecialCharacter(password)

DisplayOuput(pwlength,totalCapitalLetter, totalNumber, totalSpecialCharacter)


