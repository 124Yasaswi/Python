data = ['ajay', 1001, 25000]
choice1 = input("Enter your first choice: ")
choice2 = input("Enter your second choice: ")
if choice1.isdigit():
    choice1 = int(choice1)
if choice2.isdigit():
    choice2 = int(choice2)
if choice1 in data or choice2 in data:
    print("Full list:", data)
else:
    print("No match found.")
data.clear()
print("List after clearing:", data)


N = [11, 12, 14, 15, 17]
result = []
for num in N:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            num += 10
    result.append(num)

print("Resulting list:", result)
