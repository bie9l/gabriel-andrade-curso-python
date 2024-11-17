num1 = 10

num2= 20



def print_message(num1,num2):
    if(num1 >= 15):
        num2 += 15
    else:
        num1 += 40
    return f"numero 1 = {num1}, numero 2 = {num2}"

print(print_message(num1, num2))