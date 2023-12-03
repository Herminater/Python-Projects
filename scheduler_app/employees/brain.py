from .models import Employee, Calendar, Day, Shift
from ortools.sat.python import cp_model


#Beregn antal vagter fra calender_start til calender_slut
#Del vagter på ansatte eller ift. ønske ==> lav to fields. Et med antal vagter og et med max_vagter. 

#Gå vagter igennem en af gangen. 
#Giv dem vagter løbende, sådan at vagterne gives equally. 
#Forsøg at clustre vagterne, sådan at man arbejder et par dage i streg. 
#Hav i mente at folk ikke vil arbejde hver dag, så inkluder ferieønsker osv. (Ferieønsker kan varetages ved at lægge en værdi til vagt-tælleren der svarer til en uge)
from ortools.linear_solver import pywraplp
from ortools.linear_solver import pywraplp

def create_shifts_model(shifts):
 # Create the solver
 solver = pywraplp.Solver.CreateSolver('SCIP')

 # Define the decision variables
 # Each variable represents a shift on a specific day
 shift_vars = {}
 for day, shifts_dict in enumerate(shifts):
     for shift_instance, employees in shifts_dict.items():
         for employee in employees:
             if (day, shift_instance, employee) not in shift_vars:
               shift_vars[(day, shift_instance, employee)] = solver.IntVar(0, 1, f'shift_{day}_{shift_instance}_{employee}')

 # Define the objective function
 # The objective is to maximize the total number of shifts
 objective_terms = [shift_vars[(day, shift_instance, employee)] for day, shifts_dict in enumerate(shifts) for shift_instance, employees in shifts_dict.items() for employee in employees]
 solver.Maximize(solver.Sum(objective_terms))

 # Define the constraints
 # Each employee can only work one shift per day
 for day, shifts_dict in enumerate(shifts):
     for shift_instance, employees in shifts_dict.items():
         for employee in employees:
             solver.Add(solver.Sum([shift_vars[(day, shift_instance, employee)] for employee in employees]) <= 1)

 # Each shift has no more than one employee
 for day, shifts_dict in enumerate(shifts):
     for shift_instance, employees in shifts_dict.items():
         solver.Add(solver.Sum([shift_vars[(day, shift_instance, employee)] for employee in employees]) <= 1)

 # No employee can work more than three days in a row
 for employee in set(employee for day, shifts_dict in enumerate(shifts) for shift_instance, employees in shifts_dict.items() for employee in employees):
     for day in range(len(shifts) - 2):
         solver.Add(solver.Sum([shift_vars.get((day + i, shift_instance, employee), 0) for i in range(3)]) <= 3)

 # Max one shift per day
 for day, shifts_dict in enumerate(shifts):
     for shift_instance, employees in shifts_dict.items():
         for employee in employees:
             solver.Add(solver.Sum([shift_vars.get((day, shift_instance, employee), 0) for shift_instance in shifts_dict.keys()]) <= 1)


 # Solve the problem
 status = solver.Solve()

 # If the problem has an optimal solution, print it
 if status == pywraplp.Solver.OPTIMAL:
     print('Total number of shifts covered:', solver.Objective().Value())
     for day, shifts_dict in enumerate(shifts):
         if not shifts_dict: # If the dictionary is empty
             print(f'Day {day}, Shift None, Employee None')
         else:
             for shift_instance, employees in shifts_dict.items():
               for employee in employees:
                  if shift_vars[(day, shift_instance, employee)].solution_value() == 1:
                      print(f'Day {day}, Shift {shift_instance}, Employee {employee}')
 else:
     print('The problem does not have an optimal solution.')