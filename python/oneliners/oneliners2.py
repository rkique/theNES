companies = {
    'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
    'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}
    }

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
print(illegal)

column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

# assembles array of dictionaries with zipped name and row
db = [dict(zip(column_names, row)) for row in db_rows]

labels = ['x', 'y']
coords = [(12, 230), (130, 19), (2, 2)]
labeled = [dict(zip(labels, coord)) for coord in coords]
print(labeled)



