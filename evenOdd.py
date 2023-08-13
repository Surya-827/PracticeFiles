num = int(input("Enter the number : "))
print(*[f"Entered number {num} is Even" if num%2==0 else f"Entered number {num} is Odd"])