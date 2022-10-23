from preprocess.preprocess import cleaning
from persiantools import digits

Toman_words = ['تومان','تومن','ت','T']
Rial_words = ['R','ریال']
Numeric_words = {'هزار' : digits.en_to_fa('000') , 'میلیون' : digits.en_to_fa('000000')}

def converter(text,currency):
    """
        text: a text that hopefully contains some amount of money 
        currency: the currency we want to have. for now [rial or toman]

        returns the money in desired currency
    """
    numbers = digits.en_to_fa('0123456789')
    text = cleaning(text)
    tokens = text.split()
    out = ''
    
    num = ''
    current = 'Toman' # if there is no indicator in text, we assume its in toman
    for t in tokens:
        if t[0] in numbers:
            num = num + t
        if t in Numeric_words.keys():
            num = num + Numeric_words[t]
        if t in Toman_words:
            current = 'Toman'
        if t in Rial_words:
            current = 'Rial'
    if current == currency:
        out = num
    else:
        if currency == 'Rial':
            out = TomanToRial(num)
        if currency == 'Toman':
            out = RialToToman(num)
    
    return out, tokens


def TomanToRial(number):
    out = number + digits.en_to_fa('0')
    return out

def RialToToman(number):
    out = ''
    if number[-1] == digits.en_to_fa('0'):
        out = out[:-2]
    else:
        out = out[:-2] + ',' + out[-1]
    return out 
