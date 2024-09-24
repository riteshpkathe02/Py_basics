def print_pattern(n):
    for i in range(n):
        s=''
        for j in range(i+1):
            s = s + "*"
        print(s)

n = int(input("Enter no. of lines/stars you want to print : "))

print(print_pattern(n))