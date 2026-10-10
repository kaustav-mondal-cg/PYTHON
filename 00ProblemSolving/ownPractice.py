#Seating arrangement

arr = [ "Ram", "Sharma", "Aditya", "Shivam", "Virat", "Varun", "Kaustav"]
day = 1
while day <= 7:
    print(f"Day {day} seating arrangement: ")
    c = 0
    while c < len(arr):
        print(arr[c], end=" ")
        arr[c] = arr[c + 1] if c + 1 < len(arr) else arr[0]
        c += 1
    print()
    day += 1
