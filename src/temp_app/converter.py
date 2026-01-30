"""
Temperature Converter Module 
Provides functions to convert between Celcius, Fahrenheit and Kelvin. 
"""
def celsius_to_fahrenheit(celsius): 
	"""
	Converts temperature from Celcius to Fahrenheit.
	"""
	return (celsius*9/5)+32


def fahrenheit_to_celsius(fahrenheit):
	"""Converts temperature from Fahrenheit to Celcius.
	"""
	return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
	"""
	Converts temperture from Celsius to Kelvin
	"""
	return celsius + 273.15


def kelvin_to_celsius(kelvin):
	"""
	Converts temperture from Kelvin to Celsius.
	"""
	return kelvin - 273.15

if __name__ == "__main__":

    print("Temperature Converter Tests") 
    print(f'40°C = {celsius_to_fahrenheit(40)}°F')
    print(f'105°F = {round(fahrenheit_to_celsius(105),2)}°C')
    print(f'200°K = {round(kelvin_to_celsius(200),2)}K')


