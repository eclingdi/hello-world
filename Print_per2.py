string="Hello World"
#use end=“” to hold on and print to create enter
def print_per_2(s):
    for n, i in enumerate(s):
        #print(n, i)
        if n  % 2 == 0:
            print(s[n:n+2], end= "")
        print()
print_per_2(string)
