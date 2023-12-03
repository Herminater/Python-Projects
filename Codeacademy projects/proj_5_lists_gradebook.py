last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[5][1] = 98

print(gradebook)

gradebook[2].remove(85)
gradebook[2].append("Pass")

print(gradebook)

last_semester_gradebook = [["Math", 92], ["English", 93], ["Drawing", 87], ["Pe", 89]]

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)