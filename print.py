string = "Hello world"
print(string)
for i in string:
    print(i)

#to print per 2 character
for i, s in enumerate(string):
    if i % 2 == 0:
        print(string[i-1:i+1])

