# Armstrong Number 

num = 3
num_str = str(num)
power = len(num_str) 
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** power
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
    
