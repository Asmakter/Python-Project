#check prime number
# n = int(input("Enter a Number: "))
# flag = 0
# for i in range(2,n):
#     if n%i == 0:
#         flag = 1
#         break
# if flag == 0:
#     print("prime")
# else:
#     print("Not Prime")
# s = input("Enter a number: ")
# sum = 0
# for i in s:
#     sum = sum + int(i)
# print(sum)

# convert integer to string

# n = int(input("Enter a number: "))
# sum = 0
# while n != 0:
#     r = n%10
#     n = int(n/10)
#     sum = sum + r
# print(sum)
sum = 0
n = int(input("Enter a number: "))
if n<0:
    n = (-1)*n
while n != 0:
    r = n%10
    n = int(n/10)
    sum = sum + r
print(sum)