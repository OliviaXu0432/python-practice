S = input()
result = " "
for i in range (len(S)):
    if S[i] == " ":
        if result == " ":
            result = str(i)
        else:
            result = result + ", " + str(i)
if result == "":
    print("no spaces found")
else:
    print(result)
    


