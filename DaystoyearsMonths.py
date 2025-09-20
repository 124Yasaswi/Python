#days to years , moths ,days



days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365

months = remaining_days // 30
days_left = remaining_days % 30

print(f"{years} years {months} months {days_left} days")



    