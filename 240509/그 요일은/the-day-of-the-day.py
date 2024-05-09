# Receives m1, d1, m2, d2 as input
m1, d1, m2, d2 = tuple(map(int, input().split()))

# Enter the day to be counted
target_day = input()

# Days in each month for a leap year 2024
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Days of the week starting from Monday (since Jan 1, 2024 is a Monday)
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Calculate starting weekday index
def calculate_starting_weekday(m, d):
    days = sum(days_in_month[:m]) + d - 1
    return week_days[days % 7]  # Jan 1 is Monday, no offset needed for 2024

# Count occurrences of target_day from (m1, d1) to (m2, d2)
def count_target_day_occurrences(m1, d1, m2, d2, target_day):
    # Find starting weekday for m1, d1
    start_day = calculate_starting_weekday(m1, d1)
    start_index = week_days.index(start_day)
    target_index = week_days.index(target_day)

    # Calculate the total number of days between the two dates
    total_days = sum(days_in_month[m1:m2]) + d2 - d1 + 1
    if m1 == m2:
        total_days = d2 - d1 + 1

    # Adjust if the start month is the same as the end month
    current_day_index = start_index
    count = 0
    for _ in range(total_days):
        if week_days[current_day_index] == target_day:
            count += 1
        current_day_index = (current_day_index + 1) % 7

    return count

# Calculate and print the result
result = count_target_day_occurrences(m1, d1, m2, d2, target_day)
print(result)