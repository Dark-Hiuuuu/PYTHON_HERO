def check_number(n,m):
    if (n or m) % 2 == 0:
        return "True"
    else: 
        return "False"
    
def main():
    n = int(input("enter n:"))
    m = int(input("enter m:"))
    print(check_number(n,m))
main()