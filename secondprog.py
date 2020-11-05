#Input
input=input("Input:  ")
input=input.upper() #uppercasing the string
letter = {} #dictionaries
alpha=0
space=0
digit=0
for i in input:
    if i in letter:
        letter[i] += 1
    #Excluding space and digit
    elif i==" " or i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        if i==" ":
            space+=1
        else:
            digit+=1 #calcuting number of digit
    else:
        letter[i] = 1
length=len(input)
alpha=length-(space+digit) #calcuting number of alphabet
print("Number of occurence of each letter:\n"+str(letter))
print("Number of alphabet= "+str(alpha))
print("Number of digit= "+str(digit))

#Biswarup Roy
