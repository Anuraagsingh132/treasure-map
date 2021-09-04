import random

row1 = ["⬜️"," ️⬜️","️⬜️"]
row2 = ["⬜️"," ⬜️ ","️⬜️"]
row3 = ["⬜️"," ⬜️","⬜️"]

Row1 = ["⬜️"," ️⬜️","️⬜️"]
Row2 = ["⬜️"," ⬜️ ","️⬜️"]
Row3 = ["⬜️"," ⬜️","⬜️"]

map = [row1, row2, row3]
map2 = [Row1, Row2, Row3]
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1] = "X"

Ranndom_1 = str(random.randint(1,3))
Ranndom_2 = str(random.randint(1,3))
num2 = Ranndom_1 + Ranndom_2
num3 = int(Ranndom_1)
num4 = int(Ranndom_2)
main = str(num2)

print("Your position is "+position)
print("Computer Position is"+main)
print("Your Map is")
print(f"{row1}\n{row2}\n{row3}")

if position == main: 
  print("You Win")
  print("Your Computer map is") 
  map2[num4 - 1] = '@' 
  print(f"{Row1}\n{Row2}\n{Row3}")
else: 
  print("You Lose") 
  print("Your Computer map is") 
  map2[num4 - 1] = '@' 
  print(f"{Row1}\n{Row2}\n{Row3}")