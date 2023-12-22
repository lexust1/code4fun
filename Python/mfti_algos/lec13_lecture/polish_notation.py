# Алгоритм обратной польской нотации (постфиксная нотация,
# reverse polish notation).
import a_stack


def evaluate_rpn(expression):
    """
    Вычисляет значение выражения, записанного в обратной польской
    нотации.

    Args:
        expression: Строка, содержащая выражение в ОПН.

    Returns:
        Результат вычисления выражения.
    """
    a_stack.clear()
    for token in expression.split():
        # Проверяем, является ли токен числом
        if token.isnumeric():
            a_stack.push(float(token))
        # Выполняем операцию, если токен - оператор
        else:
            # Вытаскиваем из стека два числа (аккуратно с нумерацией
            # operand - важно при вычитании и делении).
            operand2 = a_stack.pop()
            operand1 = a_stack.pop()
            # Делаем операцию (одни из) с отправкой в стек.
            if token == '+':
                a_stack.push(operand1 + operand2)
            elif token == '-':
                a_stack.push(operand1 - operand2)
            elif token == '*':
                a_stack.push(operand1 * operand2)
            elif token == '/':
                a_stack.push(operand1 / operand2)
    return a_stack.pop()


def main():
    # (2 + 7) * 5
    print(evaluate_rpn("2 7 + 5 *"))
    # 2 + 7 * 5
    print(evaluate_rpn("2 7 5 * +"))
    # (2 - 7) * 5
    print(evaluate_rpn("2 7 - 5 *"))


if __name__ == "__main__":
    main()
