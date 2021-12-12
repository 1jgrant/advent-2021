from file_read_fn import input_text_to_array

instructions = input_text_to_array('src/inputs/day2_input.txt')

testInst = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

x_1, y_1 = 0, 0

for inst in instructions:
    direction, dist = inst.split(' ')
    dist = int(dist)
    if direction == 'forward':
        x_1 += dist
    if direction == 'down':
        y_1 += dist
    if direction == 'up':
        y_1 -= dist

print(x_1 * y_1)

x_2, y_2, aim = 0, 0, 0

for inst in instructions:
    cmd, dist = inst.split(' ')
    dist = int(dist)
    if cmd == 'down':
        aim += dist
    if cmd == 'up':
        aim -= dist
    if cmd == 'forward':
        x_2 += dist
        y_2 += aim * dist

print(x_2 * y_2)
