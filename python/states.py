import json

def txt_to_list(path):
    txt_file = open(path, 'r', encoding="utf-8")
    txt = txt_file.readlines()
    txt = [x.strip() for x in txt]
    return txt

def txt_to_dict(path):
    pre = txt_to_list(path)
    pre = [rawlist.split(",") for rawlist in pre]
    return {w[0]: w[1] for w in pre}

populations = txt_to_dict('populations.txt')
# Read the JSON data
with open('states.json') as f:
    data = json.load(f)
    geometries = data['objects']['states']['geometries']
    #[2]['properties']['name']
    for geometry in geometries:
        if(geometry['properties']['name'] in populations.keys()):
            geometry['properties']['population'] = populations[geometry['properties']['name']]

with open('states+.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    