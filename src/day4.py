import re
from typing import List
from file_read_fn import input_text_to_array_ignore_empty_lines


input_text = input_text_to_array_ignore_empty_lines('src/inputs/day4_input.txt')
num_order_str = input_text.pop(0)
draw_numbers = num_order_str.split(',')
test = ['22 13 17 11  0', ' 8  2 23  4 24', '21  9 14 16  7', '6 10  3 18  5', '1 12 20 15 19']
bingo_nums = [re.findall('[0-9]+', item) for item in input_text]


def chunks(items: List[str], chunk_length: int):
    return (items[i:i+chunk_length] for i in range(0, len(items), chunk_length))


cards = list(chunks(bingo_nums, 5))
for card in cards:
    columns = []
    for i in range(0, 5):
        column = []
        for j in range(0, 5):
            column.append(card[j][i])
        columns.append(column)
    card.extend(columns)


def get_winning_card_and_drawn_nums(bingo_cards, draw_numbers):
    drawn_nums = draw_numbers[:4]
    for num in draw_numbers[4:]:
        drawn_nums.append(num)
        for card in bingo_cards:
            for dimension in card:
                bingo = all(elem in drawn_nums for elem in dimension)
                if bingo:
                    return (card, drawn_nums)


def get_score_from_card_and_drawn_numbers(card, drawn_numbers):
    card_numbers = list(set([item for dimension in card for item in dimension]))
    unmarked_numbers = [int(num) for num in card_numbers if num not in drawn_numbers]
    sum_of_unmarked = sum(unmarked_numbers)
    return sum_of_unmarked * int(drawn_numbers[-1])


winning_card, drawn_numbers = get_winning_card_and_drawn_nums(cards, draw_numbers)
print(get_score_from_card_and_drawn_numbers(winning_card, drawn_numbers))


def get_last_card_and_drawn_nums(bingo_cards, draw_numbers):
    drawn_nums = draw_numbers[:4]
    for num in draw_numbers[4:]:
        drawn_nums.append(num)
        for card in bingo_cards:
            for dimension in card:
                bingo = all(elem in drawn_nums for elem in dimension)
                if bingo:
                    if len(bingo_cards) > 1:
                        bingo_cards.remove(card)
                        break
                    return (card, drawn_nums)


losing_card, drawn_numbers = get_last_card_and_drawn_nums(cards, draw_numbers)
print(get_score_from_card_and_drawn_numbers(losing_card, drawn_numbers))
