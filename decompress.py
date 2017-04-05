file = open("exam.bz2","r")

char_count = [0 for i in range(256)] #initial list records character position in line and numbered them
last_column=[None]
for line in file:
    line=line.split()
    unicode = ord(line[1])

    for j in range(int(line[0])):
        char_count[unicode]+=1
        last_column.append([line[1],char_count[unicode]]) #create the last column

file.close()
first_column=[None]

rank = [0 for i in range(256)]
count = 0

for i in range(len(char_count)):

    if char_count[i] > 0:
        count+=1
        rank[i]=count
        for k in range(char_count[i]):
            count+=1
            first_column.append(chr(i))
        count-=1



row= 1
str=""

for i in range(1,len(last_column)-1):
    c=last_column[row][0]
    unicode=ord(c)

    if c == "*":
        c = " "
    if c == "-":
        c = "\n"

    str= c+str
    row= rank[unicode]+ last_column[row][1] - 1

print(str)
str = "$" + str

