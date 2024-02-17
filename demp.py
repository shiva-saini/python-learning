import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Shivathoth@123",database="shiva1")

mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()

for i in result:
    print(i)












































# //strings are immutatble in python
#
# course = "My Dsa journey"
# newCourse = print(course.replace('a','b'))
# print(course,newCourse)
# print('a' in course)
# print(10/3)
# print(10//3)
# print(10**3)
#
# temperature = 18
# if temperature > 19 :
#     print("its hot day")
# else :
#     print("cool")
#     print("not cool?")


# weight = int(input("enter your weight : "))
# ans = input("(K)g or (L)bs : ")
# ans.lower()
# if ans == 'k':
#     converted = weight / 0.45
#     print("weight is " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Wight is " + str(converted))


# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers[0:3])
# numbers.insert(2,10)
# print(numbers)
# for x in numbers:
#     print(x)
# i = 0;
# while i < len(numbers):
#     print(numbers[i])
#     i+=1

# nums = range(5)
# i = 0
# while i < len(nums):
#     print(nums[i])
# for i in nums:
#     print(i)

# import pandas as pd



