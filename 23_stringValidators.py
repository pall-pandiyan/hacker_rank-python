if __name__ == '__main__':
    string = input()

    isAlphanumeric = False
    isAlphabet = False
    isNumeric = False
    isLower = False
    isUpper = False

    for charactor in string:
        if not isAlphanumeric:
            isAlphanumeric = charactor.isalnum()
        if not isAlphabet:
            isAlphabet = charactor.isalpha()
        if not isNumeric:
            isNumeric = charactor.isdigit()
        if not isLower:
            isLower = charactor.islower()
        if not isUpper:
            isUpper = charactor.isupper()

        if (isAlphanumeric and isAlphabet and isNumeric and isLower and isUpper):
            break

    print(isAlphanumeric)
    print(isAlphabet)
    print(isNumeric)
    print(isLower)
    print(isUpper)
