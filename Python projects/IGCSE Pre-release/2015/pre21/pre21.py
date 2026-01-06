
middayTotal = 0
midnightTotal = 0


midday = [None]*day
midnight = [None]*day


try:
    day = int(input("Please enter the number of days in the month:"))
    while day < 28 or day > 31:
        day = int(input("Invalid input. Please enter a number between 28 and 31:"))
except:
    print("Invalid input. Please enter a valid integer.")
    exit()



for days in range(0, day):
    try:
        middays=int(input(f"Please enter the midday temperature for day {days + 1}:"))
        while middays < -30 or middays > 50:
            middays=int(input(f"Invalid input. Please enter the midday temperature for day {days + 1} between -30 and 50:"))   
    except:
        print("Invalid input. Please enter a valid integer.")
        exit() 
    try:
        midnights=int(input(f"Please enter the midnight temperature for day {days + 1}:"))
        while midnights < -30 or midnights > 50:
            midnights=int(input(f"Invalid input. Please enter the midnight temperature for day {days + 1} between -30 and 50:"))
    except:
        print("Invalid input. Please enter a valid integer.")
        exit()


    middayTotal += middays
    midnightTotal += midnights

    midnight[days] = midnights
    midday[days] =middays


print("Day\tMidday\tMidnight")
for i in range(day):
    print(f"{i + 1}\t{midday[i]}\t{midnight[i]}")

print(f"Average midday temperature: {middayTotal/day}")
print(f"Average midnight temperature: {midnightTotal/day}")
