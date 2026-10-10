# day = int(input("Enter your day (1-7) : "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")
#     case _:
#         print("Invalid input")


# marks = int(input("Enter your score out of 100 : "))

# match marks:
#     case x if x >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case _:
#         print("Fail")


# Gas Booking & Customer Care System using match-case

booking_status = False
customer_name = ""
booking_id = 0

while True:
    print("--- Gas Booking System ---")
    print("1. Book Gas")
    print("2. Check Booking Status")
    print("3. Cancel Booking")
    print("4. Customer Care")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            if booking_status:
                print("You have already booked a gas cylinder.")
            else:
                customer_name = input("Enter your name: ")
                booking_id += 1
                booking_status = True
                print(f"Booking successful! Your Booking ID is {booking_id}")

        case 2:
            if booking_status:
                print(f"Booking is confirmed for {customer_name}. Booking ID: {booking_id}")
            else:
                print("No active booking found.")

        case 3:
            if booking_status:
                confirm = input("Do you want to cancel booking? (yes/no): ")
                if confirm.lower() == "yes":
                    booking_status = False
                    print("Booking cancelled successfully.")
                else:
                    print("Cancellation aborted.")
            else:
                print("No booking to cancel.")

        case 4:
            print("--- Customer Care ---")
            print("1. Delivery Issue")
            print("2. Payment Issue")
            print("3. Other Queries")

            issue = int(input("Select your issue: "))

            match issue:
                case 1:
                    print("Your delivery will arrive within 2-3 days.")
                case 2:
                    print("Please contact bank or try payment again.")
                case 3:
                    print("Call 1800-000-000 for support.")
                case _:
                    print("Invalid issue choice.")

        case 5:
            print("Thank you for using Gas Booking System!")
            break

        case _:
            print("Invalid choice. Try again.")