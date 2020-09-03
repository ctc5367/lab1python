temp = input("Enter temperature: ")
temp = float (temp)
unit = input("Enter unit in F/f or C/c: ")
if unit == "C" or unit == "c":
  print(f"{temp}° in Celsius is equivalent to {(temp*9/5)+32}° Fahrenheit.")
elif unit == "F" or unit == "f":
  print(f"{temp}° in Fahrenheit is equivalent to {(temp-32)*5/9}° Celsius.")
else:
  print(f"Invalid unit({unit}).");