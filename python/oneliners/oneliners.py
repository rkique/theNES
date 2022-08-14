text2 = '''

Calejflsda lkjsadl flsdajlf jlkaslf jsdlk jfkljsdalj flsdjkl jfs
df f sdafasd fkjsdlakf ldsaj ajsdkljflk jsdklj fljsdalk jflkjsd
a jljflpoiOCn sdjfalsd jiowe wfnc lkmaldsk fjowie sdlkcmaoiqo hounakmqi cjlkjoiqnw 
jcaijoq hopiphoam coijq ajoicjoehcn hyaoqcnaoq hoaohoquo n a ouoapiuq ojdsoa dfowop hq 
'''

w = [[x for x in line.split() if len(x) < 4] for line in text2.split('\n')]
print(w)

text = [line.strip() for line in open("text.txt")]
print((lambda x, y: x+y)(3,10))

txt = ['lambda functions are anonymous functions.',
    'anonymous functions dont have a name.',
    'functions are objects in python.'
]

mark = map(lambda s: True if 'anonymous' in s else False, txt)
print(list(mark))

mark = map(lambda s: True if 'function' in s else False, txt)
print(list(mark))

mark = map(lambda s: len(s)**2 if len(s) > 38 else len(s), txt)
print(list(mark))

txt = "jdskajfldsaj"
print(txt[::-1])

find_18 = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
print(find_18(text2, 'ldsaj'))


price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

sample = [line[::2] for line in price]
print(sample)

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

#replaces second elements with first elements
visitors[1::2] = visitors[::2]
print(visitors)

import matplotlib.pyplot as plt

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

#removes first two and last two, and then copies it
expected_cycles = cardiac_cycle[1:-2] * 10
plt.plot(expected_cycles)
plt.show()


