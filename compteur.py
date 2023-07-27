


start = 1000
end = 600
listNumber = ''
for number in range(start, end, -1):
    decomposedNumber = [int(d) for d in str(number)[::-1]]
    realNumber = ''
    
    unit = ''
    tens = ''
    hundreds = ''
    thousands = ''
    for i, digit in enumerate(decomposedNumber):
        decomposedNumber[i] = digit * 10**i
        if i == 0:
            if decomposedNumber[i] % 5 == 0 and decomposedNumber[i] != 0:
                unit = 'wah'
            elif decomposedNumber[i] % 7 == 0 and decomposedNumber[i] != 0:
                unit = 'wahwah'
            else:
                unit = str(digit)
        elif i == 1:
            if decomposedNumber[i] % 50 == 0 and decomposedNumber[i] != 0:
                tens = 'wah-quante'
            elif decomposedNumber[i] % 70 == 0 and decomposedNumber[i] != 0:
                tens = 'wahwah-quante'
            else:
                tens = str(digit)
        elif i == 2:
            if decomposedNumber[i] % 500 == 0 and decomposedNumber[i] != 0:
                hundreds = 'wah-cent'
            elif decomposedNumber[i] % 700 == 0 and decomposedNumber[i] != 0:
                hundreds = 'wahwah-cent'
            else:
                hundreds = str(digit)
        elif i == 3:
            if decomposedNumber[i] % 5000 == 0 and decomposedNumber[i] != 0:
                thousands = 'wah-mille'
            elif decomposedNumber[i] % 7000 == 0 and decomposedNumber[i] != 0:
                thousands = 'wahwah-mille'
            else:
                thousands = str(digit)


    listNumber += (thousands + hundreds  + tens  + unit + '\n')
print(listNumber)
    
   