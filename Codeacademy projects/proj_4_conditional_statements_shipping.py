#Wight lb's
weight = 25

#Ground shipping
if weight <= 2:
  price_per_pound = 1.5
  flat_charge = 20
  ground_shipping_price = weight *      price_per_pound + flat_charge
elif 2 < weight <= 6:
  price_per_pound = 3
  flat_charge = 20
  ground_shipping_price = weight *      price_per_pound + flat_charge
elif 6 < weight <= 10:
  price_per_pound = 4
  flat_charge = 20
  ground_shipping_price = weight *      price_per_pound + flat_charge
elif weight >= 10:
  price_per_pound = 4.75
  flat_charge = 20
  ground_shipping_price = weight *      price_per_pound + flat_charge
else:
  print("Weight is not supported")

print("Price for a " + str(weight) + "lb ground shipment is " + str(ground_shipping_price) + " dollars")

#Premium ground shipment
premium_ground_shipping_price = 125
print("Price for premium ground shipment is " + str(premium_ground_shipping_price) + " dollars")

#Drone shipping 
if weight <= 2:
  price_per_pound = 4.5
  drone_shipping_price = weight * price_per_pound
elif 2 < weight <= 6:
  price_per_pound = 9
  drone_shipping_price = weight * price_per_pound
elif 6 < weight <= 10:
  price_per_pound = 12
  drone_shipping_price = weight * price_per_pound
elif weight >= 10:
  price_per_pound = 14.25
  drone_shipping_price = weight * price_per_pound

else:
  print("Weight is not supported")

print("Price for a " + str(weight) + "lb drone shipment is " + str(drone_shipping_price) + " dollars")

#Find cheapest shipment
if drone_shipping_price < ground_shipping_price and drone_shipping_price < premium_ground_shipping_price:
  print("Drone shipment is cheapest")

elif ground_shipping_price < drone_shipping_price and ground_shipping_price < premium_ground_shipping_price:
  print("Ground shipment is cheapest")
else:
  print("Premium ground shipment is cheapest")
