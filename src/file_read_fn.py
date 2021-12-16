def input_text_to_array(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as text:
        lines = text.read().splitlines()
        array_of_values = list(lines)
        return array_of_values


def input_text_to_array_ignore_empty_lines(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as text:
        lines = text.read().splitlines()
        array_of_values = [line for line in lines if line != '']
        return array_of_values
