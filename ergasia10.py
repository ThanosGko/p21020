def binaryToDecimal(binary_list):
    decimal_list = []
    for binary in binary_list:
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        decimal_list.append(decimal)
    return decimal_list
    
text = open("textfile.txt").read()
text_list = [char for char in text]

number_list = []
for i in text_list:
    number_list.append(bin(ord(i))[2:])

txt = ""
for i in number_list:
    txt += i[:2]+i[-2:]

numbers = []
while txt != '':
    numbers.append((int(txt[:16])))
    txt = txt[16:]

dec_numbers = binaryToDecimal(numbers)

answers = [0,0,0,0]

for i in dec_numbers:
    number = int(i)
    if number%2==0:
        answers[0]+=1
    if number%3==0:
        answers[1]+=1
    if number%5==0:
        answers[2]+=1
    if number%7==0:
        answers[3]+=1

for i in range(len(answers)):
    answers[i] = int((answers[i]/len(dec_numbers))*100)
    if i==0:
        print("Το ποσοστό ζυγών είναι {}%".format(answers[i]))
    elif i==1:
        print("Το ποσοστό που διαιρείται ακριβώς με το 3 είναι {}%".format(answers[i]))
    elif i==2:
        print("Το ποσοστό που διαιρείται ακριβώς με το 5 είναι {}%".format(answers[i]))
    elif i==3:
        print("Το ποσοστό που διαιρείται ακριβώς με το 7 είναι {}%".format(answers[i]))