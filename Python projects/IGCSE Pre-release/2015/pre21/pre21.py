midday = []
midnight = []
day = int(input("Please enter the number of days in the month:"))
for days in range(0, day):
    midnight.append(int(input(f"Please enter the midnight temperature for day {days + 1}:")))
    midday.append(int(input(f"Please enter the midday temperature for day {days + 1}:")))

print("Day\tMidday\tMidnight")
for i in range(day):
    print(f"{i + 1}\t{midday[i]}\t{midnight[i]}")
