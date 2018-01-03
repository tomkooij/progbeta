n = int(input("hoeveel? "))
if n < 24:
    for i in range(1, n+1):
        print((n-i)*'  '+i*'# '+'#')
