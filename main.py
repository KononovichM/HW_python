# Напишите программу, которая бы работала следующим образом - находила символ "#"
# и если этот символ найден - удаляла предыдущий символ из строки.
# Ваша задача обработать строки с "#" символом.

def solution(text):
    result = []

    for char in text:
        if char == "#":
            if result:  # Удаляем последний символ, если стек не пуст
                result.pop()
        else:
            result.append(char)  # Добавляем символ в стек

    return "".join(result)  # Собираем строку обратно


# Проверка с выводом результатов
test_cases = [
    ("a#bc#d", "bd"),
    ("abc#d##c", "ac"),
    ("abc##d######", ""),
    ("#######", ""),
    ("", ""),
]

for input_text, expected_output in test_cases:
    output = solution(input_text)
    print(f"Вход: '{input_text}' → Выход: '{output}' (Ожидалось: '{expected_output}')")