def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = ""
  for letter in range(0, len(user_name)):
    password = password + user_name[letter-1]

  return password
 