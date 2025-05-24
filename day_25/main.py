import pandas

# Load CSV data
data = pandas.read_csv("weather_data.csv")

# Access specific column
print(data["temp"])

# Convert to dictionary
data_dict = data.to_dict()
print(data_dict)

# Convert temp column to list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculate average temperature
average = sum(temp_list) / len(temp_list)
print(f"Average temp: {average}")

# OR use pandas' built-in method
print(f"Average (pandas): {data['temp'].mean()}")
print(f"Max temp: {data['temp'].max()}")

# Get data in a row
print(data[data.day == "Monday"])

# Get row with max temp
print(data[data.temp == data.temp.max()])

# Convert Monday's temp to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp_C = int(monday.temp)
monday_temp_F = monday_temp_C * 9/5 + 32
print(f"Monday's temp in F: {monday_temp_F}")
