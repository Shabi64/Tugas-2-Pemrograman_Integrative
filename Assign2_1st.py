import datetime

# Read the number of days from the user
days = int(input("Enter the number of days: "))

# Get the current date
current_date = datetime.date.today()

# Calculate the future date
future_date = current_date + datetime.timedelta(days=days)

# Format the future date as "Saturday, February 06, 2021"
formatted_date = future_date.strftime("%A, %B %d, %Y")

# Print the formatted date
print(formatted_date)