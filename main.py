row1 = ["boo", "boo", "boo"]
row2 = ["boo", "boo", "boo"]
row3 = ["boo", "boo", "boo"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the tresure ? ")

horizontal=int(position[0])
vertical=int(position[1]) 

selected_row=map[horizontal-1]
selected_row[vertical-1] = "X"







print(f"{row1}\n{row2}\n{row3}")
 
