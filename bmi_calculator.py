def calculate_bmi(weight, height):
    """Calculate BMI = weight (kg) / height^2 (m^2)."""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def bmi_category(bmi):
    """Return BMI category based on WHO standards."""
    if bmi is None:
        return "Invalid height"
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("⚖️ BMI Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    if bmi:
        print(f"\n✅ Your BMI is: {bmi}")
        print(f"📌 Category: {category}")
    else:
        print("❌ Could not calculate BMI (invalid data).")

if _name_ == "_main_":
    main()
