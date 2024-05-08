def calculate_minutes(a, b, c):
    # Starting time: November 11, 11:11
    start_d, start_h, start_m = 11, 11, 11

    # End time provided by the input
    end_d, end_h, end_m = a, b, c

    # If the given end time is before the start time, return -1
    if (end_d < start_d) or (end_d == start_d and end_h < start_h) or (end_d == start_d and end_h == start_h and end_m < start_m):
        return -1

    # Calculate the total minutes between the two times
    minutes_from_start_to_midnight = (23 - start_h) * 60 + (59 - start_m) + 1
    minutes_from_midnight_to_end = end_h * 60 + end_m
    days_between = (end_d - start_d - 1) * 24 * 60

    # Total minutes calculation
    if end_d == start_d:
        # Same day calculation
        total_minutes = (end_h - start_h) * 60 + (end_m - start_m)
    else:
        # Different days calculation
        total_minutes = minutes_from_start_to_midnight + days_between + minutes_from_midnight_to_end

    return total_minutes

# Input
a, b, c = map(int, input().split())

# Calculate and print result
result = calculate_minutes(a, b, c)
print(result)