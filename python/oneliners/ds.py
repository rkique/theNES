import numpy as np

# a = np.array([1,2,3])
# print(a)

# b = np.array([[1,2],
#             [3,4]])
# print(b)

# #displays as slices of z
# c = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
# print(c)

# alice = [99, 101, 103]
# bob = [110, 108, 105]
# tim = [90, 88, 85]
# salaries = np.array([alice, bob, tim])
# taxation = np.array([[0.2, 0.25, 0.22],
#                      [0.4, 0.5, 0.5],
#                      [0.1, 0.2, 0.1]])

# max_income = np.max(salaries - salaries*taxation)
# print(max_income)


# a = np.array(range(55,61))
# print(a)
# print(a[:2:-1])


# c = np.array([[[1,2], [3,4]], 
#               [[5,6],[7,8]]])
# #select all with second index 0 and third index 1
# print(c[:,0,1])

# #select all with third index 0
# print(c[:,:,0])

# print(c[1,:])

# #all except last third index 
# print(c[:,:,:-1])

# print(np.ndim(c))   


# dataScientist = [130, 132, 137]
# productManager = [127, 140, 145]
# designer = [118, 118, 127]
# softwareEngineer = [129, 131, 137]
# employees = np.array([dataScientist,
#                       productManager,
#                       designer,
#                       softwareEngineer])

# employees[0, ::2] = employees[0,::2] * 1.1
# print(employees)
# print(employees.ndim)
# print(employees.dtype)

# X = np.array([[1,0,0],
#             [0,2,2],
#             [3,0,0]
# ])
# print(np.nonzero(X))

X = np.array(
    [[ 42, 40, 41, 43, 44, 43 ], # Hong Kong
     [ 30, 31, 29, 29, 29, 30 ], # New York
     [ 8, 13, 31, 11, 11, 9 ], # Berlin
     [ 11, 11, 12, 13, 11, 12 ]]) # Montreal
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

polluted = set(cities[np.nonzero(X > np.average(X))[0]])
print(X > np.average(X))
#we get row indices for higher than average cities
print(np.nonzero(X > np.average(X)))
#cities determined by row indices
print(cities[np.nonzero(X > np.average(X))[0]])

alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

actual_incomes = salaries - salaries*taxation
print(actual_incomes)
max_income = np.max(actual_incomes)
print(max_income)
#index of person with the maximum income
print(np.nonzero(actual_incomes == max_income)[0])
