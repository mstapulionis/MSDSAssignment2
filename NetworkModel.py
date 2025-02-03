from pulp import *

# BEST CASE !!

# Create a dictionary of the activities and hours expected
bestCase = {'DescribeProduct': 4,
            'DevelopMarketing': 8,
            'DesignBrochure': 6,
            'RequirementsAnalysis': 8,
            'SoftwareDesign': 12,
            'SystemDesign': 10,
            'Coding': 20,
            'Documentation': 6,
            'UnitTesting': 10,
            'SystemTesting': 12,
            'PackageDeliverables': 6,
            'SurveyMarket': 10,
            'DevelopPricing': 6,
            'DevelopImplementation': 8,
            'WriteProposal': 6}
bestCaseList = list(bestCase.keys())

# Create a dictionary of activity precedences
precedences = {'DescribeProduct': [],
            'DevelopMarketing': [],
            'DesignBrochure': ['DescribeProduct'],
            'RequirementsAnalysis': ['DescribeProduct'],
            'SoftwareDesign': ['RequirementsAnalysis'],
            'SystemDesign': ['RequirementsAnalysis'],
            'Coding': ['SoftwareDesign', 'SystemDesign'],
            'Documentation': ['Coding'],
            'UnitTesting': ['Coding'],
            'SystemTesting': ['UnitTesting'],
            'PackageDeliverables': ['Documentation', 'SystemTesting'],
            'SurveyMarket': ['DevelopMarketing', 'DesignBrochure'],
            'DevelopPricing': ['PackageDeliverables', 'SurveyMarket'],
            'DevelopImplementation': ['DescribeProduct', 'PackageDeliverables'],
            'WriteProposal': ['DevelopPricing', 'DevelopImplementation']}

# Create LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {case: LpVariable(f"start_{case}",0, None) for case in bestCaseList}

end_times = {case: LpVariable(f"end_{case}",0, None) for case in bestCaseList}

# Add the constraints
for case in bestCaseList:
    prob += end_times[case] == start_times[case] + bestCase[case], f"{case}_duration"

    for predecessor in precedences[case]:
        prob += start_times[case] >= end_times[predecessor], f"{case}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[case] for case in bestCaseList]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("critical Path time:")
for case in bestCaseList:
    if value(start_times[case]) == 0:
        print(f"{case} starts at time 0")
    if value(end_times[case]) == max([value(end_times[case]) for case in bestCaseList]):
        print(f"{case} ends at {value(end_times[case])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)


# EXPECTED CASE !!


# Create a dictionary of the activities and hours expected
expectedCase = {'DescribeProduct': 8,
            'DevelopMarketing': 16,
            'DesignBrochure': 12,
            'RequirementsAnalysis': 16,
            'SoftwareDesign': 24,
            'SystemDesign': 20,
            'Coding': 40,
            'Documentation': 12,
            'UnitTesting': 20,
            'SystemTesting': 24,
            'PackageDeliverables': 12,
            'SurveyMarket': 20,
            'DevelopPricing': 12,
            'DevelopImplementation': 16,
            'WriteProposal': 12}
expectedCaseList = list(expectedCase.keys())

# Create a dictionary of activity precedences
precedences = {'DescribeProduct': [],
            'DevelopMarketing': [],
            'DesignBrochure': ['DescribeProduct'],
            'RequirementsAnalysis': ['DescribeProduct'],
            'SoftwareDesign': ['RequirementsAnalysis'],
            'SystemDesign': ['RequirementsAnalysis'],
            'Coding': ['SoftwareDesign', 'SystemDesign'],
            'Documentation': ['Coding'],
            'UnitTesting': ['Coding'],
            'SystemTesting': ['UnitTesting'],
            'PackageDeliverables': ['Documentation', 'SystemTesting'],
            'SurveyMarket': ['DevelopMarketing', 'DesignBrochure'],
            'DevelopPricing': ['PackageDeliverables', 'SurveyMarket'],
            'DevelopImplementation': ['DescribeProduct', 'PackageDeliverables'],
            'WriteProposal': ['DevelopPricing', 'DevelopImplementation']}

# Create LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {case: LpVariable(f"start_{case}",0, None) for case in expectedCaseList}

end_times = {case: LpVariable(f"end_{case}",0, None) for case in expectedCaseList}

# Add the constraints
for case in expectedCaseList:
    prob += end_times[case] == start_times[case] + expectedCase[case], f"{case}_duration"

    for predecessor in precedences[case]:
        prob += start_times[case] >= end_times[predecessor], f"{case}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[case] for case in expectedCaseList]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("critical Path time:")
for case in expectedCaseList:
    if value(start_times[case]) == 0:
        print(f"{case} starts at time 0")
    if value(end_times[case]) == max([value(end_times[case]) for case in expectedCaseList]):
        print(f"{case} ends at {value(end_times[case])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)


## WORST CASE !!

# Create a dictionary of the activities and hours expected
worstCase = {'DescribeProduct': 12,
            'DevelopMarketing': 824,
            'DesignBrochure': 18,
            'RequirementsAnalysis': 24,
            'SoftwareDesign': 36,
            'SystemDesign': 30,
            'Coding': 60,
            'Documentation': 18,
            'UnitTesting': 30,
            'SystemTesting': 36,
            'PackageDeliverables': 18,
            'SurveyMarket': 30,
            'DevelopPricing': 18,
            'DevelopImplementation': 24,
            'WriteProposal': 18}
worstCaseList = list(worstCase.keys())

# Create a dictionary of activity precedences
precedences = {'DescribeProduct': [],
            'DevelopMarketing': [],
            'DesignBrochure': ['DescribeProduct'],
            'RequirementsAnalysis': ['DescribeProduct'],
            'SoftwareDesign': ['RequirementsAnalysis'],
            'SystemDesign': ['RequirementsAnalysis'],
            'Coding': ['SoftwareDesign', 'SystemDesign'],
            'Documentation': ['Coding'],
            'UnitTesting': ['Coding'],
            'SystemTesting': ['UnitTesting'],
            'PackageDeliverables': ['Documentation', 'SystemTesting'],
            'SurveyMarket': ['DevelopMarketing', 'DesignBrochure'],
            'DevelopPricing': ['PackageDeliverables', 'SurveyMarket'],
            'DevelopImplementation': ['DescribeProduct', 'PackageDeliverables'],
            'WriteProposal': ['DevelopPricing', 'DevelopImplementation']}

# Create LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {case: LpVariable(f"start_{case}",0, None) for case in worstCaseList}

end_times = {case: LpVariable(f"end_{case}",0, None) for case in worstCaseList}

# Add the constraints
for case in worstCaseList:
    prob += end_times[case] == start_times[case] + worstCase[case], f"{case}_duration"

    for predecessor in precedences[case]:
        prob += start_times[case] >= end_times[predecessor], f"{case}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[case] for case in worstCaseList]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("critical Path time:")
for case in worstCaseList:
    if value(start_times[case]) == 0:
        print(f"{case} starts at time 0")
    if value(end_times[case]) == max([value(end_times[case]) for case in worstCaseList]):
        print(f"{case} ends at {value(end_times[case])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)