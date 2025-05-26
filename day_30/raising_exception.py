height = float(input("Height (m): "))
weight = int(input("Weight (kg): "))

if height > 3:
    raise ValueError("Height shouldn't be more than 3 meters.")

bmi = weight / height ** 2
print(f"BMI: {bmi}")
