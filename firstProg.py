#Taking Input
input=input("Input:  ");
arr=[]
arr=input.split()
for i in range(len(arr)):
    str=arr[i]
    str1=""
    #Reverseing String
    for j in str:
        str1=j+str1
    arr[i]=str1 #Putting string back in list

output=" "

print("Output: "+output.join(arr)) #converting list to string

#Biswarup Roy
