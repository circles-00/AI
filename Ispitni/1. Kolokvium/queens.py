from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    N = int(input())
    variables = range(1, N + 1)
    domain = [(i, j) for i in range(N) for j in range(N)]

    problem.addVariables(variables, domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # x1 != x2
    # y1 != y2
    # abs(x1 - x2) != abs(y1 - y2)

    for q1 in variables:
        for q2 in variables:
            if q1 < q2:
                problem.addConstraint(
                    lambda a, b: a[0] != b[0] and a[1] != b[1] and abs(a[0] - b[0]) != abs(a[1] - b[1]), (q1, q2))

    # ----------------------------------------------------

    if N <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())