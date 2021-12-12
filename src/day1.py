from file_read_fn import input_text_to_array

depths = input_text_to_array('src/inputs/day1_input.txt')
depths = [int(depth) for depth in depths]

testDepths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

count_1 = 0
for index, depth in enumerate(depths):
    if index < 1:
        continue
    if depth > depths[index-1]:
        count_1 += 1

print(count_1)

count_2 = 0
for index in range(1, len(depths)-2):
    window = depths[index:index+3]
    previous_window = depths[index-1:index+2]
    if sum(window) > sum(previous_window):
        count_2 += 1

print(count_2)
