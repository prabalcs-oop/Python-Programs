# Program to check a number is palindrome or not
text= input("Enter a word or number:").strip()

if text.lower()==text[::-1].lower():
    print("It is a palindrome:")
else:
    print("It is not palindrome:")    