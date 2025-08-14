def arithmetic_arranger(problems, display_answers=False):
    # 1. Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first, operator, second = parts

        # 2. Error: Operator check
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 3. Error: Digits only
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # 4. Error: Max 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width
        width = max(len(first), len(second)) + 2

        # Build lines
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        dash_line.append('-' * width)

        if display_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            answer_line.append(result.rjust(width))

    # Join all lines with 4 spaces
    arranged = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dash_line)
    )

    if display_answers:
        arranged += '\n' + '    '.join(answer_line)

    return arranged
