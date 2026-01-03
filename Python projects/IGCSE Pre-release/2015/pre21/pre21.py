day = int(input("Please enter the number of days in the month:"))
while day < 28 or day > 31:
    day = int(input("Invalid input. Please enter a number between 28 and 31:"))
midday = [None]*day
midnight = [None]*day

for days in range(0, day):
    middays=int(input(f"Please enter the midday temperature for day {days + 1}:"))
    while middays < -30 or middays > 50:
        middays=int(input(f"Invalid input. Please enter the midday temperature for day {days + 1} between -30 and 50:"))    

    midnights=int(input(f"Please enter the midnight temperature for day {days + 1}:"))
    while midnights < -30 or midnights > 50:
        midnights=int(input(f"Invalid input. Please enter the midnight temperature for day {days + 1} between -30 and 50:"))
    middayTotal += middays
    midnight[days] = midnights
    midday[days] =middays
    # Today distracted me so I could not finish the last part of the code.

print("Day\tMidday\tMidnight")
for i in range(day):
    print(f"{i + 1}\t{midday[i]}\t{midnight[i]}")

average =
