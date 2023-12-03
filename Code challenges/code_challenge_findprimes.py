def prime_finder(n):
  # Write your code here
  prime_numbers = []
  for number in range(1,n+1):
    for sec_number in range(1, number+1):
      if sec_number == 1:
        continue
      elif sec_number == number:
        prime_numbers.append(number)

      elif number % sec_number != 0:
        continue
      elif number % sec_number == 0:
        break
        

  return prime_numbers
print(prime_finder(11))