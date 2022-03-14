from typing import List
from file_read_fn import input_comma_separated_line_to_int_list

test_fish = [3, 4, 3, 1, 2]
puzzle_fish = input_comma_separated_line_to_int_list('/Users/jamesgrant/code/advent_2021/src/inputs/day6_input.txt')


def advance_fish_one_day(fish_list: List[int]) -> List[int]:
    temp_fish = fish_list.copy()
    new_fish_count = 0
    for i, fish_age in enumerate(temp_fish):
        if fish_age == 0:
            temp_fish[i] = 6
            new_fish_count += 1
            continue
        temp_fish[i] -= 1
    if new_fish_count > 0:
        temp_fish.extend([8]*new_fish_count)
    return temp_fish


def fish_list_after_days(starting_fish: List[int], days: int) -> List[int]:
    temp_fish = starting_fish.copy()
    for _ in range(days):
        temp_fish = advance_fish_one_day(temp_fish)
    return temp_fish


print(len(fish_list_after_days(test_fish, 80)))
print(len(fish_list_after_days(puzzle_fish, 80)))
