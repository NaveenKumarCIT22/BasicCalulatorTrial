# Calulator program

print("Welcome to the Calculator Program!")
while True:
    print("Enter your expression: ")
    inp = input(">> ")
    if inp.lower()=="q":
        break
    ans = eval(inp)
    print("Answer: ",ans)
    

    