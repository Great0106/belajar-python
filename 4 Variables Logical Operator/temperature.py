# Start Code Here
print("Temperature Conversion")
print("\n")
print("Please choose the following conversions. (1, 2, 3, 4)")
print("1 = Celcius to Farenheit")
print("2 = Celcius to Kelvin")
print("3 = Farenheit to Celcius")
print("4 = Kelvin to Celcius")
conversion = int(input(""))
if conversion == 1:
  celcius = int(input("Input Celcius here."))
  ninefifth = 9 / 5
  farenheit = celcius * ninefifth + 32
  print(farenheit)
elif conversion == 2:
  celcius = int(input("Input Celcius here."))
  kelvin = celcius + 273,15
  print(kelvin)
elif conversion == 3:
  farenheit = int(input("Input Farenheit here."))
  fifthnine = 5 / 9
  celcius = (farenheit - 32) * fifthnine
  print(celcius)
elif conversion == 4:
  kelvin = int(input("Input Kelvin here."))
  celcius = kelvin - 273,15
  print(celcius)
