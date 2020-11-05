#Funtion return the closing bracket
def closebracket(c):
	if c == '(':
		return ')'
	elif c == '{':
		return '}'
	elif c == '[':
		return ']'
	return -1


def expression(input,le):

    if le==0:
        return True
    if le==1:
        return False
    if input[0] == ')' or input[0] == '}' or input[0] == ']':  #If beginning of the string start with close bracket
        return False

    #calling the Funtion
    closebrac = closebracket(input[0])

    count = 0
    for i in range(1, le):
        if input[i] == input[0]:  #checking if consecutive string character is same
            count += 1
        if input[i] == closebrac:  #checking if consecutive string character is opening and closing bracket
            if count == 0:
                break
            count -= 1


    if i == le:
        return False


    if i == 1:
        return expression(input[2:],le-2)  #recursion Funtion call for rest of the string if consecutive two character opening
                                           #closing bracket of same type

    #recursion funtion dividing string between two bracket and rest of the string
    return expression(input[1:],i-1) and expression(input[i + 1:],le-i-1)



input = input("Input: ")
le=len(input)#length of the expression
if expression(input,le):
    print("Output: True")
else:
    print("Output: False")

#Biswarup Roy
