import googletrans as gt
from googletrans import Translator
import time



lang = gt.LANGUAGES
##print(lang.keys()) # accessing the keys in dictionary
##print(lang.values()) # accessing the values in dictionary

#print(len(lang))

def lang_print():
    print('Please pick the language you want to translate.\n\n')
    print('1: afrikaans\n'
      '2: albanian\n'
      '3: amharic\n'
      '4: arabic\n'
      '5: armenian\n'
      '6: azerbaijani\n'
      '7: basque\n'
      '8: belarusian\n'
      '9: bengali\n'
      '10: bosnian\n'
      '11: bulgarian\n'
      '12: catalan\n'
      '13: cebuano\n'
      '14: chichewa\n'
      '15: chinese (simplified)\n'
      '16: chinese (traditional)\n'
      '17: corsican\n'
      '18: croatian\n'
      '19: czech\n'
      '20: danish\n'
      '21: dutch\n'
      '22: english\n'
      '23: esperanto\n'
      '24: estonian\n'
      '25: filipino\n'
      '26: finnish\n'
      '27: french\n'
      '28: frisian\n'
      '29: galician\n'
      '30: georgian\n'
      '31: german\n'
      '32: greek\n'
      '33: gujarati\n'
      '34: haitian creole\n'
      '35: hausa\n'
      '36: hawaiian\n'
      '37: hebrew\n'
      '38: hebrew\n'
      '39: hindi\n'
      '40: hmong\n'
      '41: hungarian\n'
      '42: icelandic\n'
      '43: igbo\n'
      '44: indonesian\n'
      '45: irish\n'
      '46: italian\n'
      '47: japanese\n'
      '48: javanese\n'
      '49: kannada\n'
      '50: kazakh\n'
      '51: khmer\n'
      '52: korean\n'
      '53: kurdish (kurmanji)\n'
      '54: kyrgyz\n'
      '55: lao\n'
      '56: latin\n'
      '57: latvian\n'
      '58: lithuanian\n'
      '59: luxembourgish\n'
      '60: macedonian\n'
      '61: malagasy\n'
      '62: malay\n'
      '63: malayalam\n'
      '64: maltese\n'
      '65: maori\n'
      '66: marathi\n'
      '67: mongolian\n'
      '68: myanmar (burmese)\n'
      '69: nepali\n'
      '70: norwegian\n'
      '71: odia\n'
      '72: pashto\n'
      '73: persian\n'
      '74: polish\n'
      '75: portuguese\n'
      '76: punjabi\n'
      '77: romanian\n'
      '78: russian\n'
      '79: samoan\n'
      '80: scots gaelic\n'
      '81: serbian\n'
      '82: sesotho\n'
      '83: shona\n'
      '84: sindhi\n'
      '85: sinhala\n'
      '86: slovak\n'
      '87: slovenian\n'
      '88: somali\n'
      '89: spanish\n'
      '90: sundanese\n'
      '91: swahili\n'
      '92: swedish\n'
      '93: tajik\n'
      '94: tamil\n'
      '95: telugu\n'
      '96: thai\n'
      '97: turkish\n'
      '98: ukrainian\n'
      '99: urdu\n'
      '100: uyghur\n'
      '101: uzbek\n'
      '102: vietnamese\n'
      '103: welsh\n'
      '104: xhosa\n'
      '105: yiddish\n'
      '106: yoruba\n'
      '107: zulu')


def lang_inpt(inpt):
    global lng
    if inpt == '1' or inpt == 'afrikaans':
        lng = 'af'
    elif inpt == '2' or inpt == 'albanian':
        lng = 'sq'
    elif inpt == '3' or inpt == 'amharic':
        lng = 'am'
    elif inpt == '4' or inpt == 'arabic':
        lng = 'ar'
    elif inpt == '5' or inpt == 'armenian':
        lng = 'hy'
    elif inpt == '6' or inpt == 'azerbaijani':
        lng = 'az'
    elif inpt == '7' or inpt == 'basque':
        lng = 'eu'
    elif inpt == '8' or inpt == 'belarusian':
        lng = 'be'
    elif inpt == '9' or inpt == 'bengali':
        lng = 'bn'
    elif inpt == '10' or inpt == 'bosnian':
        lng = 'bs'
    elif inpt == '11' or inpt == 'bulgarian':
        lng = 'bg'
    elif inpt == '12' or inpt == 'catalan':
        lng = 'ca'
    elif inpt == '13' or inpt == 'cebuano':
        lng = 'ceb'
    elif inpt == '14' or inpt == 'chichewa':
        lng = 'ny'
    elif inpt == '15' or inpt == 'chinese':
        lng = 'zh-cn'
    elif inpt == '16' or inpt == 'chinese':
        lng = 'zh-tw'
    elif inpt == '17' or inpt == 'corsican':
        lng = 'co'
    elif inpt == '18' or inpt == 'croatian':
        lng = 'hr'
    elif inpt == '19' or inpt == 'czech':
        lng = 'cs'
    elif inpt == '20' or inpt == 'danish':
        lng = 'da'
    elif inpt == '21' or inpt == 'dutch':
        lng = 'nl'
    elif inpt == '22' or inpt == 'english':
        lng = 'en'
    elif inpt == '23' or inpt == 'esperanto':
        lng = 'eo'
    elif inpt == '24' or inpt == 'estonian':
        lng = 'et'
    elif inpt == '25' or inpt == 'filipino':
        lng = 'tl'
    elif inpt == '26' or inpt == 'finnish':
        lng = 'fi'
    elif inpt == '27' or inpt == 'french':
        lng = 'fr'
    elif inpt == '28' or inpt == 'frisian':
        lng = 'fy'
    elif inpt == '29' or inpt == 'galician':
        lng = 'gl'
    elif inpt == '30' or inpt == 'georgian':
        lng = 'ka'
    elif inpt == '31' or inpt == 'german':
        lng = 'de'
    elif inpt == '32' or inpt == 'greek':
        lng = 'el'
    elif inpt == '33' or inpt == 'gujarati':
        lng = 'gu'
    elif inpt == '34' or inpt == 'haitian creole':
        lng = 'ht'
    elif inpt == '35' or inpt == 'hausa':
        lng = 'ha'
    elif inpt == '36' or inpt == 'hawaiian':
        lng = 'haw'
    elif inpt == '37' or inpt == 'hebrew':
        lng = 'iw'
    elif inpt == '38' or inpt == 'hebrew':
        lng = 'he'
    elif inpt == '39' or inpt == 'hindi':
        lng = 'hi'
    elif inpt == '40' or inpt == 'hmong':
        lng = 'hmn'
    elif inpt == '41' or inpt == 'hungarian':
        lng = 'hu'
    elif inpt == '42' or inpt == 'icelandic':
        lng = 'is'
    elif inpt == '43' or inpt == 'igbo':
        lng = 'ig'
    elif inpt == '44' or inpt == 'indonesian':
        lng = 'id'
    elif inpt == '45' or inpt == 'irish':
        lng = 'ga'
    elif inpt == '46' or inpt == 'italian':
        lng = 'it'
    elif inpt == '47' or inpt == 'japanese':
        lng = 'ja'
    elif inpt == '48' or inpt == 'javanese':
        lng = 'jw'
    elif inpt == '49' or inpt == 'kannada':
        lng = 'kn'
    elif inpt == '50' or inpt == 'kazakh':
        lng = 'kk'
    elif inpt == '51' or inpt == 'khmer':
        lng = 'km'
    elif inpt == '52' or inpt == 'korean':
        lng = 'ko'
    elif inpt == '53' or inpt == 'kurdish' or inpt == 'kurmanji':
        lng = 'ku'
    elif inpt == '54' or inpt == 'kyrgyz':
        lng = 'ky'
    elif inpt == '55' or inpt == 'lao':
        lng = 'lo'
    elif inpt == '56' or inpt == 'latin':
        lng = 'la'
    elif inpt == '57' or inpt == 'latvian':
        lng = 'lv'
    elif inpt == '58' or inpt == 'lithuanian':
        lng = 'lt'
    elif inpt == '59' or inpt == 'luxembourgish':
        lng = 'lb'
    elif inpt == '60' or inpt == 'macedonian':
        lng = 'mk'
    elif inpt == '61' or inpt == 'malagasy':
        lng = 'mg'
    elif inpt == '62' or inpt == 'malay':
        lng = 'ms'
    elif inpt == '63' or inpt == 'malayalam':
        lng = 'ml'
    elif inpt == '64' or inpt == 'maltese':
        lng = 'mt'
    elif inpt == '65' or inpt == 'maori':
        lng = 'mi'
    elif inpt == '66' or inpt == 'marathi':
        lng = 'mr'
    elif inpt == '67' or inpt == 'mongolian':
        lng = 'mn'
    elif inpt == '68' or inpt == 'burmese' or inpt == 'myanmar':
        lng = 'my'
    elif inpt == '69' or inpt == 'nepali':
        lng = 'ne'
    elif inpt == '70' or inpt == 'norwegian':
        lng = 'no'
    elif inpt == '71' or inpt == 'odia':
        lng = 'or'
    elif inpt == '72' or inpt == 'pashto':
        lng = 'ps'
    elif inpt == '73' or inpt == 'persian':
        lng = 'fa'
    elif inpt == '74' or inpt == 'polish':
        lng = 'pl'
    elif inpt == '75' or inpt == 'portuguese':
        lng = 'pt'
    elif inpt == '76' or inpt == 'punjabi':
        lng = 'pa'
    elif inpt == '77' or inpt == 'romanian':
        lng = 'ro'
    elif inpt == '78' or inpt == 'russian':
        lng = 'ru'
    elif inpt == '79' or inpt == 'samoan':
        lng = 'sm'
    elif inpt == '80' or inpt == 'scots gaelic':
        lng = 'gd'
    elif inpt == '81' or inpt == 'serbian':
        lng = 'sr'
    elif inpt == '82' or inpt == 'sesotho':
        lng = 'st'
    elif inpt == '83' or inpt == 'shona':
        lng = 'sn'
    elif inpt == '84' or inpt == 'sindhi':
        lng = 'sd'
    elif inpt == '85' or inpt == 'sinhala':
        lng = 'si'
    elif inpt == '86' or inpt == 'slovak':
        lng = 'sk'
    elif inpt == '87' or inpt == 'slovenian':
        lng = 'sl'
    elif inpt == '88' or inpt == 'somali':
        lng = 'so'
    elif inpt == '89' or inpt == 'spanish':
        lng = 'es'
    elif inpt == '90' or inpt == 'sundanese':
        lng = 'su'
    elif inpt == '91' or inpt == 'swahili':
        lng = 'sw'
    elif inpt == '92' or inpt == 'swedish':
        lng = 'sv'
    elif inpt == '93' or inpt == 'tajik':
        lng = 'tg'
    elif inpt == '94' or inpt == 'tamil':
        lng = 'ta'
    elif inpt == '95' or inpt == 'telugu':
        lng = 'te'
    elif inpt == '96' or inpt == 'thai':
        lng = 'th'
    elif inpt == '97' or inpt == 'turkish':
        lng = 'tr'
    elif inpt == '98' or inpt == 'ukrainian':
        lng = 'uk'
    elif inpt == '99' or inpt == 'urdu':
        lng = 'ur'
    elif inpt == '100' or inpt == 'uyghur':
        lng = 'ug'
    elif inpt == '101' or inpt == 'uzbek':
        lng = 'uz'
    elif inpt == '102' or inpt == 'vietnamese':
        lng = 'vi'
    elif inpt == '103' or inpt == 'welsh':
        lng = 'cy'
    elif inpt == '104' or inpt == 'xhosa':
        lng = 'xh'
    elif inpt == '105' or inpt == 'yiddish':
        lng = 'yi'
    elif inpt == '106' or inpt == 'yoruba':
        lng = 'yo'
    elif inpt == '107' or inpt == 'zulu':
        lng = 'zu'
        

def lang_trans(text1):

    translator = Translator()
    #print(translator.detect(text1))

    #print(translator.detect(text2))

    translation = translator.translate(text1, dest = lng)
    #translation1 = translator.translate(text2, dest = lng)

    print('here is the translated text: \n')
    print(translation.text)
    #print(translation1.text)

'''
for k,v in lang.items():
    print(k, v)
'''





print('------------Language Translate-------------')
print('---------------Using Google-------------')

text1 = input('Enter the Sentence-1 : ')

#text2 = input('Enter the Sentence-2 : ')

lang_print()

print('\n')
inpt = input('Type you\'re language No. Or langauge name here: ')
    



print('please Wait....')
lang_inpt(inpt)
time.sleep(3)

lang_trans(text1)

