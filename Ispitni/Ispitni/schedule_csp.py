from constraint import *

def what(x, y):
    split = x.split('_')
    split1 = y.split('_')
    if split[0] == split1[0]:
    #print(split[0] + '_' + str(int(split[1]) + 1) == y)
        return y != (split[0] + '_' + str(int(split[1])+1)) and x != (split1[0] + '_' + str(int(split1[1])+1))
    return True
   
    

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())
    
    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13","Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12", "Wed_13","Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13","Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]
    
    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]
    
    # ---Tuka dodadete gi promenlivite--------------------
    for i in range(casovi_AI):
        problem.addVariable("AI_cas_" + str(i+1), AI_predavanja_domain)
    for i in range(casovi_ML):
        problem.addVariable("ML_cas_" + str(i+1), ML_predavanja_domain)
    for i in range(casovi_R):
        problem.addVariable("R_cas_" + str(i+1), R_predavanja_domain)
    for i in range(casovi_BI):
        problem.addVariable("BI_cas_" + str(i+1), BI_predavanja_domain)
    
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------

    for i in range(casovi_AI):
        for j in range(casovi_ML):
                problem.addConstraint(what, ('AI_cas_' + str(i+1), 'ML_cas_' + str(j+1)))
                
    for i in range(casovi_AI):
        for j in range(casovi_R):
                problem.addConstraint(what, ('AI_cas_' + str(i+1), 'R_cas_' + str(j+1)))
                
    for i in range(casovi_AI):
        for j in range(casovi_BI):
                problem.addConstraint(what, ('AI_cas_' + str(i+1), 'BI_cas_' + str(j+1)))
                
    for i in range(casovi_ML):
        for j in range(casovi_R):
                problem.addConstraint(what, ('ML_cas_' + str(i+1), 'R_cas_' + str(j+1)))
                
    for i in range(casovi_ML):
        for j in range(casovi_BI):
                problem.addConstraint(what, ('ML_cas_' + str(i+1), 'BI_cas_' + str(j+1)))
                
    for i in range(casovi_R):
        for j in range(casovi_BI):
                problem.addConstraint(what, ('R_cas_' + str(i+1), 'BI_cas_' + str(j+1)))
                
    problem.addConstraint(what, ('AI_vezbi', 'ML_vezbi'))
    problem.addConstraint(what, ('AI_vezbi', 'BI_vezbi'))
    problem.addConstraint(what, ('ML_vezbi', 'BI_vezbi'))
    
                
    problem.addConstraint(AllDifferentConstraint())
    for i in range(casovi_BI):
        problem.addConstraint(lambda r1, r2: (r1 == 'Mon_10' and r2 == 'Tue_10') or (r1 == 'Mon_10' and r2 == 'Thu_10') or (r1 == 'Wed_10' and r2 == 'Tue_10') or (r1 == 'Wed_10' and r2 == 'Thu_10') or (r1 == 'Fri_10' and r2 == 'Tue_10') or (r1 == 'Fri_10' and r2 == 'Thu_10') or (r1 == 'Mon_11' and r2 == 'Tue_11') or (r1 == 'Mon_11' and r2 == 'Thu_11') or (r1 == 'Wed_11' and r2 == 'Tue_11') or (r1 == 'Wed_11' and r2 == 'Thu_11') or (r1 == 'Fri_11' and r2 == 'Tue_11') or (r1 == 'Fri_11' and r2 == 'Thu_11'), ('BI_cas_'+str(i+1), 'BI_vezbi'))
    # ----------------------------------------------------
    solution = problem.getSolution()
    
    print("{'BI_vezbi': '%s', " % (solution['BI_vezbi']), end='')
    for i in range(casovi_BI):
        line = "BI_cas_" + str(i+1)
        print("'%s': '%s', " % (line, solution[line]), end='')
    for i in range(casovi_AI):
        line = "AI_cas_" + str(i+1)
        print("'%s': '%s', " % (line, solution[line]), end='')   
    print("'AI_vezbi': '%s', " % (solution['AI_vezbi']), end='')
    print("'ML_vezbi': '%s', " % (solution['ML_vezbi']), end='')
    for i in range(casovi_ML):
        line = "ML_cas_" + str(i+1)
        print("'%s': '%s', " % (line, solution[line]), end='')   
    for i in range(casovi_R):
        line = "R_cas_" + str(i+1)
        if i == (casovi_R - 1):
            print("'%s': '%s'}" % (line, solution[line]))
        else:
            print("'%s': '%s', " % (line, solution[line]))   
    
    # print(solution)