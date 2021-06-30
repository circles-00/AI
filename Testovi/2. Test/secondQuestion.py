from searching_framework.uninformed_search import *


def D1(lista):
    for ii in range(len(lista)):
        if ii < len(lista) - 1 and lista[ii + 1] == -1 and lista[ii] != -1:
            return ii
    return -2


def D2(lista):
    for ii in range(len(lista)):
        if ii < len(lista) - 2 and lista[ii + 1] != -1 and lista[ii + 2] == -1 and lista[ii] != -1:
            return ii
    return -2


def L1(lista):
    for ii in range(len(lista)):
        if ii > 0 and lista[ii - 1] == -1 and lista[ii] != -1:
            return ii
    return -2


def L2(lista):
    for ii in range(len(lista)):
        if ii > 1 and lista[ii - 1] != -1 and lista[ii - 2] == -1 and lista[ii] != -1:
            return ii
    return -2


class Lenta(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        curr_state = list(state)

        # Try D1
        new_index = D1(curr_state)
        string = 'D1: Disk ' + str(curr_state[new_index])
        if new_index != -2:
            curr_state[new_index], curr_state[new_index + 1] = curr_state[new_index + 1], curr_state[new_index]
            successors[string] = tuple(curr_state)

        # Try D2
        new_index = D2(curr_state)
        string = 'D2: Disk ' + str(curr_state[new_index])
        if new_index != -2:
            curr_state[new_index], curr_state[new_index + 2] = curr_state[new_index + 2], curr_state[new_index]
            successors[string] = tuple(curr_state)

        # Try L1
        new_index = L1(curr_state)
        string = 'L1: Disk ' + str(curr_state[new_index])
        if new_index != -2:
            curr_state[new_index], curr_state[new_index - 1] = curr_state[new_index - 1], curr_state[new_index]
            successors[string] = tuple(curr_state)

        # Try L2
        new_index = L2(curr_state)
        string = 'L2: Disk ' + str(curr_state[new_index])
        if new_index != -2:
            curr_state[new_index], curr_state[new_index - 2] = curr_state[new_index - 2], curr_state[new_index]
            successors[string] = tuple(curr_state)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for ii in range(len(state)):
            if state[ii] != self.goal[ii]:
                return 0
        return 1


if __name__ == '__main__':
    N = int(input())
    L = int(input())

    state_list = list()

    for i in range(L):
        if i > N - 1:
            state_list.append(-1)
        else:
            state_list.append(i + 1)

    goal_list = state_list[::-1]
    lenta = Lenta(tuple(state_list), tuple(goal_list))

    res = breadth_first_graph_search(lenta)
    print(res.solution())
