from constraint import *


def check_Marija(prisustvo_marija, vreme_sostanok):
    return prisustvo_marija != 1 or vreme_sostanok == 14


def check_Petar(prisustvo_petar, vreme_sostanok):
    return prisustvo_petar != 1 or vreme_sostanok == 16 or vreme_sostanok == 19 or vreme_sostanok == 13


def check_Marija_Petar(prisustvo_marija, prisustvo_petar):
    return prisustvo_marija != prisustvo_petar


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19, 20])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # problem.addConstraint(lambda r1, r2: r1 != 1 or r2 == 13 or r2 == 14 or r2 == 16 or r2 == 19, ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(check_Marija, ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(check_Petar, ("Petar_prisustvo", "vreme_sostanok"))
    problem.addConstraint(check_Marija_Petar, ("Marija_prisustvo", "Petar_prisustvo"))

    # ----------------------------------------------------
    # [print(solution) for solution in problem.getSolutions()]

    solutions = problem.getSolutions()
    for solution in solutions:
        print("%s'Simona_prisustvo': %d, 'Marija_prisustvo': %d, 'Petar_prisustvo': %d, 'vreme_sostanok': %d%s" % (
            "{", solution['Simona_prisustvo'], solution['Marija_prisustvo'], solution['Petar_prisustvo'],
            solution['vreme_sostanok'], "}"))
        # print("{}'Simona_prisustvo': {}, 'Marija_prisustvo': {}, 'Petar_prisustvo': {}, 'vreme_sostanok': {}{}".format("{", solution['Simona_prisustvo'], solution['Marija_prisustvo'], solution['Petar_prisustvo'], solution['vreme_sostanok'], "}"))
