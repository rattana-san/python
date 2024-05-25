# converts farenheit to celcius 
print("")
print("")
print("press 1 for farenheit")
print("press 2 for celius")
settings = int(input("Is your current unit farenheit or celcius? "))

if settings == 1:
  print("")
  farenheit = int(input("Enter the temperature in farenheit: "))  #temp in farenheit
  c = (farenheit - 32)/1.8  #formula for celcius
  print("In celcius that would be:")
  print(c) 

if settings == 2:
  print("")
  celcius = int(input("Enter temperature in celcius: "))
  f = (9/5 * celcius) + 32
  print("In farenheit that would be:")
  print(f)