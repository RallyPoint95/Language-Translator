import googletrans as gt

num = []
#lang2 = {}

lang = gt.LANGUAGES

for i in range(1,108):
    num.append(i)

lang2_keys = [str(x) for x in num]

lang2_values = lang.keys()

#print(lang_keys)

lang2 = dict(zip(lang2_keys, lang2_values))

#print(lang2)

for k,v in lang.items():
    val = lang.values()

for k,v in lang2.items():
    key = lang2.keys()

lang3 = dict(zip(key, val))

for k,v in lang3.items():
    print('%s: %s' % (k,v))
