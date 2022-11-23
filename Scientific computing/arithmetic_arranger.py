def arithmetic_arranger(list, answer=False):
    #   Variable Declaration
    answer_list = []
    numerators = []
    denominators = []
    lines = []

    # Error checking
    if len(list) > 5:
        return "Error: Too many problems."

    for item in list:
        split = item.split()

        if split[1] != "+" and split[1] != "-":
            return "Error: Operator must be '+' or '-'."

        if split[0].isdigit() == False or split[2].isdigit() == False:
            return "Error: Numbers must only contain digits."

        if len(split[0]) > 4 or len(split[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Finding longest Digit
        if len(split[0]) > len(split[2]):
            long_digit = len(split[0])

        else:
            long_digit = len(split[2])
        # len_count.append(long_digit)

        # Making numerator
        numerator = split[0].rjust(long_digit + 2)
        numerators.append(numerator)

        # Making denominator
        denminator = split[1] + " " + split[2].rjust(long_digit)
        denominators.append(denminator)
        # Making Line
        line = "-" * (long_digit + 2)
        lines.append(line)

        # Finding the answer
        if answer == True:
            if split[1] == "+":
                calculation = int(split[0]) + int(split[2])
            else:
                calculation = int(split[0]) - int(split[2])
            answer_list.append(str(calculation).rjust(long_digit + 2))

    top_line = "    ".join(numerators)
    bottom_line = "    ".join(denominators)
    lines_line = "    ".join(lines)
    if answer == True:
        answer_line = "    ".join(answer_list)

    final_print = top_line + "\n" + bottom_line + "\n" + lines_line
    if answer == True:
        final_print = final_print + "\n" + answer_line

    return final_print


print("1\n")
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print("2\n")
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print("3\n")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
