from file_read_fn import input_text_to_array

instructions = input_text_to_array('src/inputs/day2_input.txt')

testInst = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

x_1, y_1 = 0, 0

for inst in instructions:
    direction, dist = inst.split(' ')
    if (direction == 'forward'):
        x_1 += int(dist)
    if (direction == 'down'):
        y_1 += int(dist)
    if (direction == 'up'):
        y_1 -= int(dist)

print(x_1 * y_1)
