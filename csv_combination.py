import csv
from datetime import datetime, timedelta

# Let's create a fun travel plan!
def plan_travel_dates():
    today = datetime.now().date()  # Let's start planning from today

    travel_dates = []

    # Plan 25 different travel adventures
    for _ in range(25):
        # We're planning a 7-day trip every time
        start_date = today + timedelta(days=7)
        end_date = start_date + timedelta(days=3)  # Our trips are 3 days long

        travel_dates.append((start_date, end_date))
        today = end_date  # Update for the next adventure

    return travel_dates

# Generate our travel dates
adventurous_dates = plan_travel_dates()

# List of our favorite destinations (replace with your dream destinations!)
dream_destinations = ['Paris', 'Tokyo', 'New York', 'Bora Bora', 'Sydney']

travel_plans = []

# Let's create travel plans for each dream destination
for destination in dream_destinations:
    for start_date, end_date in adventurous_dates:
        # Convert dates to string format
        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date_str = end_date.strftime('%Y-%m-%d')

        # Our travel plan is ready!
        travel_plans.append([destination, start_date_str, end_date_str])

# Our travel diary file
travel_diary_path = 'dream_travel_plans.csv'

# Let's write our travel plans to a CSV file
with open(travel_diary_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write a friendly header
    csv_writer.writerow(['Destination', 'Start Date', 'End Date'])

    # Write our exciting travel adventures
    csv_writer.writerows(travel_plans)

# Yay! We've created our dream travel plans
print(f"Congratulations! Your dream travel plans are ready. Check them out in '{travel_diary_path}'. Happy travels!")
