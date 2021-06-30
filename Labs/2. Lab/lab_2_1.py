from constraint import *

if __name__ == '__main__':

    # Define variables
    problem = Problem()
    domain_Participants = list()
    domain_Team_leaders = list()
    variables = list()

    num_Participants = int(input())
    for i in range(num_Participants):
        line = (input().split(" "))
        domain_Participants.append(float(line[0]))
        variables.append(line[1])

    num_Team_leaders = int(input())
    for i in range(num_Team_leaders):
        line = (input().split(" "))
        domain_Team_leaders.append(float(line[0]))
        variables.append(line[1])

    problem.addVariable("Team Leader", domain_Team_leaders)
    problem.addVariable("Participant 1", domain_Participants)
    problem.addVariable("Participant 2", domain_Participants)
    problem.addVariable("Participant 3", domain_Participants)
    problem.addVariable("Participant 4", domain_Participants)
    problem.addVariable("Participant 5", domain_Participants)
    problem.addConstraint(ExactSumConstraint(100.0))
    problem.addConstraint(AllDifferentConstraint())
    solution = problem.getSolution()

    Team_leader = None
    Participant_1 = None
    Participant_2 = None
    Participant_3 = None
    Participant_4 = None
    Participant_5 = None

    count = 0
    for v in domain_Participants + domain_Team_leaders:
        if solution['Team Leader'] == v:
            Team_leader = variables[count]
        if solution['Participant 1'] == v:
            Participant_1 = variables[count]
        if solution['Participant 2'] == v:
            Participant_2 = variables[count]
        if solution['Participant 3'] == v:
            Participant_3 = variables[count]
        if solution['Participant 4'] == v:
            Participant_4 = variables[count]
        if solution['Participant 5'] == v:
            Participant_5 = variables[count]
        count += 1

    total = solution['Team Leader'] + solution['Participant 1'] + solution['Participant 2'] + solution[
        'Participant 3'] + solution['Participant 4'] + solution['Participant 5']
    print("Total score:", "%.1f" % total)
    print("Team leader:", Team_leader)
    print("Participant 1:", Participant_1)
    print("Participant 2:", Participant_2)
    print("Participant 3:", Participant_3)
    print("Participant 4:", Participant_4)
    print("Participant 5:", Participant_5)
