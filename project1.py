print("welcome i cant talk sorry")
fields = [["🌳","🌳","🌳"],["🌳","🌳","🌳"],["🌳","🌳","🌳"]]
print(f"{fields[0]}\n{fields[1]}\n{fields[2]}")
row_column = input("enter your row and column:")
row = int(row_column[0]) -1
column = int(row_column[1]) -1
fields[row][column] = "🐇"
print(f"{fields[0]}\n{fields[1]}\n{fields[2]}")