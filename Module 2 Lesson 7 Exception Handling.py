# Generate A Random Weather Forecast

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

temp_type = input("Enter 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ").upper()
temp = float(input("Enter the temperature to convert: "))

if temp_type == 'C':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
elif temp_type == 'F':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
else:
    print("Invalid temperature type. Please enter 'C' or 'F'.")

try:
    number = int(input("Enter a number: "))
    print("The number is:", number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


finally:
    if 'file' in locals():
        file.close()
    print("Thank you for using this weather application.") 
