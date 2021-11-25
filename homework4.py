print("Input number a:")
a = int(input())
print("Input number b:")
b = int(input())
print("Input number c:")
c = int(input())

print("Results of comparison:")
while a <= b:
    print a, "<", b
    a += c

if a > b:
    print a, ">", b
