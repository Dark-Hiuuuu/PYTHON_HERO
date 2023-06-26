def check_number(n):
    if n % 3 == 0 and (50 <n< 100):
        return "True"
    else:
        return "False"


def main():
    n = int(input("enter n:"))
    print(check_number(n))
main()
