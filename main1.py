# activity 1 character occurance
string = str(input("Enter the string:"))
char = (input("Enter the character that you want to find:"))
caount = 0
i = 0
while i < len(string):
    if char == string[i]:
        caount += 1
    i += 1
print(caount)