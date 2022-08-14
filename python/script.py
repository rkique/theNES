def list_to_txt(path):
    txt_file = open(path, 'r', encoding="utf-8")
    txt = txt_file.readlines()
    txt = [x.strip() for x in txt]
    return txt

depths = list_to_txt("input.txt")
depths = [int(t) for t in depths]

for i in range(2, len(depths)):
    print(depths[i], i-1, i-2)