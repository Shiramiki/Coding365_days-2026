
middayTotal = 0
midnightTotal = 0


def dayInMonth():
    global day, midday, midnight
    try:
        day = int(input("Please enter the number of days in the month:"))
        while day < 28 or day > 31:
            day = int(input("Invalid input. Please enter a number between 28 and 31:"))
    except:
        print("Invalid input. Please enter a valid integer.")
        exit()

    else:
        midday = [None]*day
        midnight = [None]*day


def tempMiddayValues():
    try:
            middays=int(input(f"Please enter the midday temperature for day {days + 1}:"))
            while middays < -30 or middays > 50:
                middays=int(input(f"Invalid input. Please enter the midday temperature for day {days + 1} between -30 and 50:"))   
    except:
        print("Invalid input. Please enter a valid integer.")
        exit() 
        tempMiddayValues()
        
    else:
        
        midnights =tempMidnightValues()
        temp =[middays, midnights]
        return temp

def tempMidnightValues():
    try:
        midnights=int(input(f"Please enter the midnight temperature for day {days + 1}:"))
        while midnights < -30 or midnights > 50:
            midnights=int(input(f"Invalid input. Please enter the midnight temperature for day {days + 1} between -30 and 50:"))
    except:
        print("Invalid input. Please enter a valid integer.")
        exit()
        tempMidnightValues()
    else:
        return midnights





for days in range(0, day):
    temp = tempMiddayValues()
    midnight[days] = temp.pop()  # Get the last element which is
    midday[days] = temp.pop()    # Get the first element which is
    middayTotal += midday[days]
    middayAvg = middayTotal / day
    midnightTotal += midnight[days]
    midnightAvg = midnightTotal / day


print("Day\tMidday\tMidnight")
for i in range(day):
    print(f"{i + 1}\t{midday[i]}\t{midnight[i]}")

print(f"Average midday temperature: {middayAvg}")
print(f"Average midnight temperature: {midnightAvg}")