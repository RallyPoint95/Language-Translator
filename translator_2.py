import googletrans as gt
from googletrans import Translator
import time

lang = gt.LANGUAGES

def lang_print():
    
    num = []

    lang = gt.LANGUAGES

    for i in range(1,108):
        num.append(i)

    lang2_keys = [str(x) for x in num]

    lang2_values = lang.keys()

    lang2 = dict(zip(lang2_keys, lang2_values))

    for k,v in lang.items():
        val = lang.values()

    for k,v in lang2.items():
        key = lang2.keys()

    lang3 = dict(zip(key, val))

    for k,v in lang3.items():
        print('%s: %s' % (k,v))

def lang_inpt(inpt):
    global lng

    num = []
    for i in range(1,108):
        num.append(i)

    lang2_keys = [str(x) for x in num]

    lang2_values = lang.keys()

    lang2 = dict(zip(lang2_keys, lang2_values))
    
    for k,v in lang.items():
        if inpt == v:
            lng = k

    for k,v in lang2.items():
        if inpt == k:
            lng = v

def lang_trans(text1):

    translator = Translator()

    translation = translator.translate(text1, dest = lng)

    print('here is the translated text: \n')
    print(translation.text)

print('------------Language Translate-------------')
print('---------------Using Google-------------')
time.sleep(2)

text1 = input('Enter the Sentence-1 : ')
time.sleep(1)
print('Please pick the language you want to translate.\n\n')
time.sleep(2)

lang_print()

print('\n')
inpt = input('Type you\'re language No. Or langauge name here: ')

print('please Wait....')
lang_inpt(inpt)
time.sleep(3)

lang_trans(text1)
