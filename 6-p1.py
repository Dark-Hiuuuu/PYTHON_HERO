def check_number(n):
    if n % 5 == 0 and n not in (20,70):
        return "True"
    else:
        return "False"
    
def main():
    n = int(input("enter n:"))
    print(check_number(n))
main()