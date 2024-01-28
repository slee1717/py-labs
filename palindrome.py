x = input("Enter a string: ")

x = x.replace(" ", "").lower()

if x == x[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

