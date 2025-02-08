def convert_cel_to_far(temperature_in_celsius):
    """Return a float representing the provided Celsius temperature converted in Fahrenheit."""
    temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
    print(f"{temperature_in_celsius} degrees C = {temperature_in_fahrenheit} degrees F.")
    return temperature_in_fahrenheit
    

def convert_far_to_cel(temperature_in_fahrenheit):
    """Return a float representing the provided Fahrenheit temperature converted in Celsius."""
    temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5/9
    print(f"{temperature_in_fahrenheit} degrees F = {temperature_in_celsius} degrees C.")
    return temperature_in_celsius

temperature_in_celsius = float(input("Enter a temperature in Celsius: "))
convert_cel_to_far(temperature_in_celsius)
temperature_in_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
convert_far_to_cel(temperature_in_fahrenheit)
