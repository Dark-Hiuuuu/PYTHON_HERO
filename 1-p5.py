import re

# def count_words(input_string):
#     # Xóa bỏ các ký tự đặc biệt, số, và dấu câu
#     cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
#     # Tách chuỗi thành danh sách các từ
#     word_list = cleaned_string.split()
#     print(word_list)
#     # word_count = len(word_l)
#     # Đếm số từ trong danh sách 
#     return word_list[0]


# # Nhập chuỗi từ người dùng
# input_string = input("Nhập chuỗi: ")
# # Đếm số từ trong chuỗi
# result = count_words(input_string)
# # print(result)



# n = input("enter: ")
# s = 0
# n = re.sub(r'[,\;]', '',n)
# print(n)
# number_string = n.split(",")    
# for i in number_string:
#     s += int(i)
# print(s)





# def count_characters(string):
#     uppercase_count = 0
#     lowercase_count = 0
#     digit_count = 0

#     for char in string:
#         if char.isupper():
#             uppercase_count += 1
#         elif char.islower():
#             lowercase_count += 1
#         elif char.isdigit():
#             digit_count += 1

#     return uppercase_count, lowercase_count, digit_count

# input_string = input("Nhập chuỗi: ")
# uppercase, lowercase, digits = count_characters(input_string)
# print("Số ký tự in hoa:", uppercase)
# print("Số ký tự in thường:", lowercase)
# print("Số ký tự số:", digits)

# stringInput = input("enter:")
# lst = []
# s = 0
# for i in stringInput:
#     if i.isdigit():
#         lst.append(i)
# for i in lst:
#     s = s + int(i)
# print(s)

# def checkPassword(passwordUser):
#     if len(passwordUser) < 6:
#         return False
#     if not re.search(r"[!@#$%^&*(),.?\":{}<>]",passwordUser):
#         return False
#     if not re.search(r"[A-Z]",passwordUser):
#         return False
#     if not re.search(r"\d",passwordUser):
#         return False
#     if not re.search(r"[a-z]",passwordUser):
#         return False
#     return True
# while True:
#     passwordUser = input("please again:")
#     if checkPassword(passwordUser):
#         print("your password is very strong")
#         break
#     else:
#         print("you should set again password")
# n = int(input(""))
# n = str(n)
# stringEmpty = ""
# for i in range(len(n)-1,-1,-1):
#     stringEmpty += n[i]
#     if len(stringEmpty) % 3 == 0 


n = int(input("enter element's number:"))
lst = []
for i in range(1,n+1):
    lst.append(int(input(f"number {i} is:")))
print(lst)
a = int(input("enter a to compare:"))
b = int(input("enter b to compare:"))
while (a and b) >= len(lst):
    a = int(input("please enter a again:"))
    b = int(input("please enter b again:"))
lstAftercompare = []
for i in lst: 
    if (a<=i<=b):
        lstAftercompare.append(i)
varcompare = lstAftercompare[0] 
for i in lstAftercompare:
    if i <= varcompare:
        varcompare = i
print(varcompare)