# dict_data = {1: {"name": "Izah", "age":"29"}, 2:{"name":"Joi","age":"15"}}

# for i in dict_data.values():
#     print(i["name"])

# for num in list_data:
#     if num == 3:
#         print("i found 3")
#     elif num < 3:
#         print("too far")


# list_data = [1,2,3,4,5,6,7,8,9,10]
#
#
#
# for num in list_data:
#     if num % 3 == 0:
#         print(num)


# count = 0
# for num in range(0,1000):
#     if num % 3 == 0 or num % 5 == 0:
#         count += num
#         print(count)



# a,b = 1,1
# seq = 0
# while a < 4000000:
#     if a % 2 == 0:
#         seq+= a
#     a,b = b, a+b
# print (seq)



# def largest_prime_factor(n):
#     i = 2
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#     return n
#
# print(largest_prime_factor(129))



# user = True
#
# while user:
#     age = input("What is your age?: ")
#     if age.isdigit() and int(age) < 117:
#         user = False
#     else:
#         print("Enter your age in digits or you are too old")
#

#
# def gcd(x,y): return y and gcd(y, x % y) or x
# def lcm(x,y): return x * y / gcd(x,y)
#
# n = 1
# for i in range(1, 21):
#      n = lcm(n, i)
# print(n)

#
# n = 2
# for i in range(1, 11):
#     product = n * i
#     print(product)


numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

