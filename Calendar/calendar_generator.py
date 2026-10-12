# CALENDAR

# Import modules
import calendar
from datetime import date

# Generate calendar
def generate_calendar():

    # Get today's date
    today = date.today()

    print("Calendar Generator")
    print("---------------------")
    print(f"Today: {today}")

    # Get user input
    year = int(input("\nEnter year: "))
    month = int(input("Enter month: "))

    # Validate month
    if month < 1 or month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
        return

    # Display calendar
    print("\n" + calendar.month(year, month))

# Run program
generate_calendar()
