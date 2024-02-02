import json
import timeit


def modify_size(data):
    for record in data:
        record['size'] = 35


def reverse_and_save(data):
    reversed_data = list(reversed(data))
    with open("output.2.5.json", 'w') as output_file:
        json.dump(reversed_data, output_file, indent=2)


file_path = "large-file.json"


with open(file_path, 'r') as file:
    data = json.load(file)

# Set up the timeit functions with the modify_size and reverse_and_save functions
timeit_setup = "from __main__ import modify_size, reverse_and_save, data"

# Measure the time it takes to modify the size value 10 times
total_time = timeit.timeit(stmt="modify_size(data)", setup=timeit_setup, number=10)

# Calculate the average time across the 10 repetitions
average_time = total_time / 10

print(f"Average time to modify size value: {average_time} seconds")

# Time the reverse_and_save function separately
time_to_reverse_and_save = timeit.timeit(stmt="reverse_and_save(data)", setup=timeit_setup, number=1)

print(f"Time to reverse and save: {time_to_reverse_and_save} seconds")
