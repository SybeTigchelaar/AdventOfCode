import re

#Import txt in list
password_list = []
password_file = open("02.txt", "r")
for line in password_file:
    word = re.split(" |-",line.strip())
    word[2] = word[2].replace(':','')
    password_list.append(word)

total_password_count = 0
total_secondpassword_count = 0
for line in password_list:
    Minlen = int(line[0])
    Maxlen = int(line[1])
    Letter = line[2]
    Password = line[3]
    
    #Part1
    count = 0
    for l in Password:
        if l == Letter:
            count += 1
    if(count >= Minlen and count <= Maxlen):
        total_password_count += 1

    #Part2
    if (Letter == Password[Minlen-1] and Letter != Password[Maxlen-1]) or (Letter != Password[Minlen-1] and Letter == Password[Maxlen-1]):
        total_secondpassword_count +=1

    

   
print(total_password_count)
print(total_secondpassword_count)