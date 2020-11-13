def listParameter():
    parameterName = []
    while True:   
        print('Enter a list value or enter nothing to stop')
        name = input()
        if name == '':
            break
        parameterName = parameterName + [name]  # list concatenation
    parameterName.insert(-1, ' and')

    joinedString = ', '.join(parameterName[:-2])
    joinedSecond = ' '.join(parameterName[-2:])
    print(joinedString + joinedSecond)

listParameter()
