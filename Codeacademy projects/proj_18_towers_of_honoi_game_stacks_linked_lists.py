from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)
#Set up the Game
num_disks = input("\nHow many disks do you want to play with?\n")
while int(num_disks) < 3:
  num_disks = input("\nEnter a number greater than or equal to 3\n")

for num in range(int(num_disks), 0, -1):
  left_stack.push(num)

num_optimal_moves = 2**int(num_disks)-1

print("\nThe fastest you can solve this game is in {num_optimal_moves} moves".format(num_optimal_moves = num_optimal_moves))

#Get User Input
def get_input():
  choices = [stack.get_name()[:1] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter = letter, name = name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
#Play the Game
num_user_moves = 0 

while right_stack.get_size() != int(num_disks):
  print(right_stack.get_size())
  print(num_disks)
  print("\n\n\... Current Stacks...")
  for stack in stacks: 
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.is_empty():
      print("\nInvalid Move. Try Again")

    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1 
      break
    else:
        print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {num_user_moves}, and the optimal number of moves is {num_optimal_moves}".format(num_user_moves = num_user_moves, num_optimal_moves = num_optimal_moves))
      


