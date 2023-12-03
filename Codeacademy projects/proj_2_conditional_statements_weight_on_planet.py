print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  relative_gravity = 0.91
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

elif planet == 2:
  relative_gravity = 0.38
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

elif planet == 3:
  relative_gravity = 2.34
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

elif planet == 4:
  relative_gravity = 1.06
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

elif planet == 5:
  relative_gravity = 0.92
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

elif planet == 6:
  relative_gravity = 1.19
  weight_on_planet = relative_gravity * weight
  print("You weigh " + str(weight_on_planet) + "kg on planet number " + str(planet))

else:
  print("Unknown planet")


