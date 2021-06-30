from searching_framework import Problem
from searching_framework.informed_search import *


def up(x, y, obstacles):
    if y < 9 and (x, y + 1) not in obstacles:
        y += 1
    return y


def down(x, y, obstacles):
    if y > 0 and (x, y - 1) not in obstacles:
        y -= 1
    return y


def right(x, y, obstacles):
    if x < 9 and (x + 1, y) not in obstacles:
        x += 1
    return x


def left(x, y, obstacles):
    if x > 0 and (x - 1, y) not in obstacles:
        x -= 1
    return x


class Pacman(Problem):

    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()
        pac_x = state[0]
        pac_y = state[1]
        orientation = state[2]
        foods = state[3]

        if orientation == 'istok':
            new_x = right(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['ProdolzhiPravo'] = (new_x, pac_y, 'istok',
                                                tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))
            new_x = left(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['ProdolzhiNazad'] = (new_x, pac_y, 'zapad',
                                                tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

            new_y = up(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['SvrtiLevo'] = (pac_x, new_y, 'sever',
                                           tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_y = down(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['SvrtiDesno'] = (pac_x, new_y, 'jug',
                                            tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

        if orientation == 'jug':
            new_y = down(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['ProdolzhiPravo'] = (pac_x, new_y, 'jug',
                                                tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_y = up(pac_x, pac_y, self.obstacles)
            if pac_x != new_y:
                successors['ProdolzhiNazad'] = (pac_x, new_y, 'sever',
                                                tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_x = right(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['SvrtiLevo'] = (new_x, pac_y, 'istok',
                                           tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

            new_x = left(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['SvrtiDesno'] = (new_x, pac_y, 'zapad',
                                            tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

        if orientation == 'sever':
            new_y = up(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['ProdolzhiPravo'] = (pac_x, new_y, 'sever',
                                                tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_y = down(pac_x, pac_y, self.obstacles)
            if pac_x != new_y:
                successors['ProdolzhiNazad'] = (pac_x, new_y, 'jug',
                                                tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_x = left(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['SvrtiLevo'] = (new_x, pac_y, 'zapad',
                                           tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

            new_x = right(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['SvrtiDesno'] = (new_x, pac_y, 'istok',
                                            tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

        if orientation == 'zapad':
            new_x = left(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['ProdolzhiPravo'] = (new_x, pac_y, 'zapad',
                                                tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))
            new_x = right(pac_x, pac_y, self.obstacles)
            if pac_x != new_x:
                successors['ProdolzhiNazad'] = (new_x, pac_y, 'istok',
                                                tuple([f for f in foods if f[0] != new_x or f[1] != pac_y]))

            new_y = down(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['SvrtiLevo'] = (pac_x, new_y, 'jug',
                                           tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

            new_y = up(pac_x, pac_y, self.obstacles)
            if pac_y != new_y:
                successors['SvrtiDesno'] = (pac_x, new_y, 'sever',
                                            tuple([f for f in foods if f[0] != pac_x or f[1] != new_y]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[3]) == 0

    def h(self, node):
        state = node.state
        pac_x = state[0]
        pac_y = state[1]
        all_food = state[3]

        minimum = 99999999
        for i in all_food:
            food_coordinates = i
            food_x = food_coordinates[0]
            food_y = food_coordinates[1]
            distance = (abs((pac_x - food_x)) + abs((pac_y - food_y)))
            if distance < minimum:
                minimum = distance

        return minimum


if __name__ == '__main__':
    obstacle_pos = ((0, 9), (0, 8), (0, 6),
                    (1, 2), (1, 3), (1, 4), (1, 9),
                    (2, 9),
                    (3, 9), (3, 6),
                    (4, 6), (4, 7), (4, 5), (4, 1),
                    (5, 1), (5, 6),
                    (6, 9), (6, 0), (6, 1), (6, 2),
                    (8, 1), (8, 4), (8, 7), (8, 8),
                    (9, 4), (9, 7), (9, 8))

    pacman_x = int(input())
    pacman_y = int(input())
    pacman_orientation = input()

    food_count = int(input())
    food = list()

    for i in range(food_count):
        food.append([int(j) for j in input().split(",")])

    for j in range(food_count):
        food[j] = tuple(food[j])

    pacman = Pacman(obstacle_pos, (pacman_x, pacman_y, pacman_orientation, tuple(food)))

    res = astar_search(pacman)
    print(res.solution())
