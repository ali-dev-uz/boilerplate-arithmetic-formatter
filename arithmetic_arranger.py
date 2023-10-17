def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    dash_line = ""
    result_line = ""

    for problem in problems:
        elements = problem.split()
        operand1, operator, operand2 = elements[0], elements[1], elements[2]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'"

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits"

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits"

        width = max(len(operand1), len(operand2)) + 2  # 2 for the operator and a space

        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + operand2.rjust(width - 1) + "    "
        dash_line += '-' * width + "    "

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:  # operator == '-'
                result = str(int(operand1) - int(operand2))
            result_line += result.rjust(width) + "    "

    arranged_problems += top_line.rstrip() + '\n'
    arranged_problems += bottom_line.rstrip() + '\n'
    arranged_problems += dash_line.rstrip() + '\n'

    if show_answers:
        arranged_problems += result_line.rstrip()

    return arranged_problems
