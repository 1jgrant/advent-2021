def input_text_to_array(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as text:
        lines = text.read().splitlines()
        array_of_values = [int(depth) for depth in lines]
        return array_of_values
