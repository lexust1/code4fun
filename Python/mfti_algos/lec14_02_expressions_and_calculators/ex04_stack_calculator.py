# Упражнение №4
# Реализовать стековый калькулятор на python. Написать программу,
# которая читает выражение в обратной польской нотации и считает его
# значение или пишет, что выражение составлено не корректно (если оно
# некорректно).
def evaluate_rpn(expression):
    """
    Вычисляет значение выражения, записанного в обратной польской
    нотации.

    Args:
        expression: Строка, содержащая выражение в ОПН.

    Returns:
        Результат вычисления выражения.
    """
    _stack = []
    for token in expression.split():
        # Проверяем, является ли токен числом, если да - добавляем в стек.
        if token.isnumeric():
            _stack.append(float(token))
        # Выполняем операцию, если токен - оператор
        else:
            if len(_stack) < 2:
                return "Выражение некорректно: недостаточно операндов для операции."
            # Вытаскиваем из стека два числа (аккуратно с нумерацией
            # operand - важно при вычитании и делении).
            operand2 = _stack.pop()
            operand1 = _stack.pop()
            # Делаем одну из операции, результат отправляем в стек.
            if token == '+':
                _stack.append(operand1 + operand2)
            elif token == '-':
                _stack.append(operand1 - operand2)
            elif token == '*':
                _stack.append(operand1 * operand2)
            elif token == '/':
                _stack.append(operand1 / operand2)
            else:
                return "Выражение некорректно: неизвестная операция."
    if len(_stack) != 1:
        return "Выражение некорректно: ожидается один результат, получено несколько."
    return _stack.pop()


def main():
    # (2 + 7) * 5
    print(evaluate_rpn("2 7 + 5 *"))
    # 2 + 7 * 5
    print(evaluate_rpn("2 7 5 * +"))
    # (2 - 7) * 5
    print(evaluate_rpn("2 7 - 5 *"))
    # 3 4 2 1 - * + 5 /
    print(evaluate_rpn("3 4 2 1 - * + 5 /"))
    print(evaluate_rpn("3 4 2 1 - * + 5"))
    print(evaluate_rpn("3 4 2 1 - * + /"))
    print(evaluate_rpn("3 4 2 1 - * + 5 ^"))


if __name__ == "__main__":
    main()
