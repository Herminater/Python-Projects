letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(len(letters)-1):
  letters.append(letters[i].lower())
print(letters)

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0

print(letter_to_points)

def score_word(word):
  points_total = 0
  for letter in word:
    points_total += letter_to_points.get(letter, 0)
  return points_total

brownie_points = score_word("BROWNIE")

print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
  player_to_points[player] = str(player_points)


print(player_to_points)

def play_word(player, word):
  player_to_words["player1"].append(word)
play_word("player1", "Hay")
print(player_to_words)