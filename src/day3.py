from collections import Counter
from typing import List
from file_read_fn import input_text_to_array

testBins = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

bin_nums = input_text_to_array('src/inputs/day3_input.txt')

gamma_bin, epsilon_bin = '', ''
bin_length = len(bin_nums[0])
for pos in range(bin_length):
    digits = [num[pos] for num in bin_nums]
    most_common = Counter(digits).most_common(1)[0][0]
    if most_common == '1':
        gamma_bin += '1'
        epsilon_bin += '0'
    if most_common == '0':
        gamma_bin += '0'
        epsilon_bin += '1'

gamma_int = int(gamma_bin, 2)
epsilon_int = int(epsilon_bin, 2)
print(gamma_int * epsilon_int)


def nums_to_rating(num_list: List[str], target_bit: int, index: int = 0) -> str:
    if len(num_list) == 1:
        return num_list[0]
    digits = [num[index] for num in num_list]
    counts = Counter(digits).most_common(2)
    if counts[0][1] == counts[1][1]:
        target_value = str(target_bit)
    else:
        target_index = 1 - target_bit
        target_value = counts[target_index][0]
    filtered_list = [num for num in num_list if num[index] == target_value]
    return nums_to_rating(filtered_list, target_bit, index + 1)


o2_int = int(nums_to_rating(bin_nums, 1), 2)
co2_int = int(nums_to_rating(bin_nums, 0), 2)
print(o2_int * co2_int)
