import math



DEBUG = False

def get_box_number(pokemon_number: int):
  return math.ceil(pokemon_number / 30)

def get_box_location(pokemon_number: int):
  #box_row = (math.ceil((pokemon_number % 30) / 6)) + 1
  #box_col = (pokemon_number % 6) + 1
  box_row = math.ceil((pokemon_number % 30) / 6)
  if box_row == 0:
    box_row = 5
  box_col = pokemon_number % 6
  if box_col == 0:
    box_col = 6
  box_location = [
    [" ", "1", "2", "3", "4", "5", "6"],
    ["1", "-", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-", "-"]
  ]
  box_location[box_row][box_col] = "*"
  return box_row, box_col, box_location

def print_pokemon_location(pokemon_number):
  box_number = get_box_number(pokemon_number)
  box_row, box_col, box_location = get_box_location(pokemon_number)
  print(f"\nBox: {box_number}\nRow: {box_row}\nCol: {box_col}\n")
  for line in box_location:
    for char in line:
      print(f"{char} ", end='')
    print("")
  print("\n-------------------------------------\n")

if not DEBUG:
  while(True):
    try:
      pokemon_number_input = int(input("Enter pokemon number:\n"))
    except Exception as e:
      print(e)
    print_pokemon_location(pokemon_number_input)
else:
  for i in range(10):
    print(f"Pokemon Number:\n{i+1}")
    print_pokemon_location(i+1)