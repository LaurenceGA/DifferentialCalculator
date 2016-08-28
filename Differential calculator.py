#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Differential calculator.py", "7/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def get_parts(eqn):
    a = None
    var = None
    power = None
    for i, char in enumerate(eqn):
        if not a:
            if char.isalpha():
                a = eqn[:i]
                var = eqn[i:i+1]
                power = eqn[i+2:]

    return a, var, power


def derive_parts(a, var, power):
    if a:
        a = float(a)
    else:
        if var:
            a = 1
        else:
            a = 0
    if power:
        power = float(power)
    else:
        power = 1

    a *= power
    power -= 1

    return a, var, power


def form_derivative(a, var, power):
    if var:
        if power == 1:
            power = ""
        elif power == 0:
            power = ""
            var = ""
        else:
            power = "^{0:g}".format(power)

        if a == 0:
            a = '0'
            var = ""
            power = ""
        elif a == 1:
            if var:
                a = ""
            else:
                a = '1'
        elif a == -1:
            a = "-"
        else:
            a = "{0:g}".format(a)
    else:
        var = ""
        power = ""

    derivative = "{}{}{}".format(a, var, power)

    return derivative


def get_derivative(eqn):
    a, var, power = get_parts(eqn)
    a, var, power = derive_parts(a, var, power)

    return form_derivative(a, var, power)


def derive(eqn):
    eqn = eqn.strip()
    eqn_parts = []
    part_start = 0
    part_end = 1

    skip = True if eqn[0] in ['+', '-'] else False

    for char in eqn:
        if skip == True:
            skip = False
            part_end += 1
            continue
        if char in ['+', '-'] or part_end == len(eqn):
            if part_end == len(eqn):
                eqn_parts.append([eqn[part_start:part_end].strip(), ""])
            else:
                eqn_parts.append([eqn[part_start:part_end-1].strip(), char])
            part_start = part_end
        part_end += 1

    # print(eqn_parts)

    for i in range(len(eqn_parts)):
        eqn_parts[i][0] = get_derivative(eqn_parts[i][0])
        if eqn_parts[i][0] == '0' and len(eqn_parts) > 1:
            eqn_parts[i][0] = ''
            # print(eqn_parts)
            if eqn_parts[i-1]:
                eqn_parts[i-1][1] = ''

    eqn_parts = [" ".join(part).strip() for part in eqn_parts]
    # print(eqn_parts)

    final_eqn = " ".join(eqn_parts).strip()

    indicies = []

    for i, char in enumerate(final_eqn):
        if char == ' ':
            if i == 0:
                indicies.append(i)
            elif i == len(final_eqn)-1:
                indicies.append(i)

            if i+1 < len(final_eqn):
                if final_eqn[i+1] == ' ':
                    indicies.append(i+1)

    final_eqn = list(final_eqn)

    for i in sorted(set(indicies), reverse=True):
        del final_eqn[i]

    # print(final_eqn)

    final_eqn = ''.join(final_eqn)

    return final_eqn

# equation = input("Enter an equation: ")


test_cases = ['315x^513 - 134r - 134 - 1324 + 1342 - f + 134',
              '124 - r - 124',
              '5x^2',
              'x',
              '1',
              'x^1',
              'a - a - a + 1',
              '-5'
]

# test_cases = ['3']

for test in test_cases:
    print("{}:\n\t<{}>\n".format(test, derive(test)))
# print("The derivative is {}".format(derive(equation)))
