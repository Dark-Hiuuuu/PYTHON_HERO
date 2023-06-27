# a = int(input("enter a:"))
# b = int(input("enter b:"))
# dem = [] 
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if a % i == 0 and b % j == 0 and i == j:
#             dem.append(j)
# print(dem)

# s = 0
# for i in dem:
#     if i > s:
#         s = i
# print(s)


#  check số nguyên tố không 
n = int(input("enter n:"))
s = 0 
for i in range(1,n+1):
    if n % i  == 0:
        s += 1
if s == 2:
    print("so nguyen to")
else:
    print("khong phai so nguyen to")