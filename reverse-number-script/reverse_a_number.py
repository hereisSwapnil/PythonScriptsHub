def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return reversed_num

# Test the function
input_num = int(input("Enter a number: "))
reversed_num = reverse_number(input_num)
print(f"The reversed number is: {reversed_num}")
