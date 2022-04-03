from collections import Counter
import numpy as np
import pandas as pd
import os
import math

PARENT_PATH = "C://Users//Vojta//Desktop//iv//KPB//points//2//grams"
MONOGRAM_PATH = os.path.sep.join([PARENT_PATH, 'monograms.txt'])
BIGRAM_PATH = os.path.sep.join([PARENT_PATH, 'bigrams.txt'])
TRIGRAM_PATH = os.path.sep.join([PARENT_PATH, 'trigrams.txt'])
QUADGRAM_PATH = os.path.sep.join([PARENT_PATH, 'quadgrams.txt'])

def gram_dic(path):
    res = {}

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(' ')
            gram = parts[0]
            counter = int(parts[1].strip())
            res[gram] = counter

    n = np.sum(list(res.values()))

    return { k:(round((v/n), 3)) for k, v in res.items() }


# english_letter_freq_monogram = gram_dic(MONOGRAM_PATH)
# english_letter_freq_bigram = gram_dic(BIGRAM_PATH)
# english_letter_freq_trigram = gram_dic(TRIGRAM_PATH)
# english_letter_freq_quadgram = gram_dic(QUADGRAM_PATH)
english_letter_freq_monogram = {
    "A":8.55,
    "K":0.81,
    "U":2.68,
    "B":1.60,
    "L":4.21,
    "V":1.06,
    "C":3.16,
    "M":2.53,
    "W":1.83,
    "D":3.87,
    "N":7.17,
    "X":0.19,
    "E":12.10,
    "O":7.47,
    "Y":1.72,
    "F":2.18,
    "P":2.07,
    "Z":0.11,
    "G":2.09,
    "Q":0.10,
    "H":4.96,
    "R":6.33, 
    "I":7.33,
    "S":6.73, 
    "J":0.22,
    "T":8.94,
}
english_letter_freq_bigram = {
    "TH":2.71,"EN":1.13,"NG":0.89,
    "HE":2.33,"AT":1.12,"AL":0.88,
    "IN":2.03,"ED":1.08,"IT":0.88,
    "ER":1.78,"ND":1.07,"AS":0.87,
    "AN":1.61,"TO":1.07,"IS":0.86,
    "RE":1.41,"OR":1.06,"HA":0.83,
    "ES":1.32,"EA":1.00,"ET":0.76,
    "ON":1.32,"TI":0.99,"SE":0.73,
    "ST":1.25,"AR":0.98,"OU":0.72,
    "NT":1.17,"TE":0.98,"OF":0.71,
}
english_letter_freq_trigram = {
    "THE":1.81,"ERE":0.31,"HES":0.24,
    "AND":0.73,"TIO":0.31,"VER":0.24,
    "ING":0.72,"TER":0.30,"HIS":0.24,
    "ENT":0.42,"EST":0.28,"OFT":0.22,
    "ION":0.42,"ERS":0.28,"ITH":0.21,
    "HER":0.36,"ATI":0.26,"FTH":0.21,
    "FOR":0.34,"HAT":0.26,"STH":0.21,
    "THA":0.33,"ATE":0.25,"OTH":0.21,
    "NTH":0.33,"ALL":0.25,"RES":0.21,
    "INT":0.32,"ETH":0.24,"ONT":0.20
}
english_letter_freq_quadgram = {
    "TION":0.31,"OTHE":0.16,"THEM":0.12,
    "NTHE":0.27,"TTHE":0.16,"RTHE":0.12,
    "THER":0.24,"DTHE":0.15,"THEP":0.11,
    "THAT":0.21,"INGT":0.15,"FROM":0.10,
    "OFTH":0.19,"ETHE":0.15,"THIS":0.10,
    "FTHE":0.19,"SAND":0.14,"TING":0.10,
    "THES":0.18,"STHE":0.14,"THEI":0.10,
    "WITH":0.18,"HERE":0.13,"NGTH":0.10,
    "INTH":0.17,"THEC":0.13,"IONS":0.10,
    "ATIO":0.17,"MENT":0.12,"ANDT":0.10
}


def get_n_gram_ref(n):
    if n == 1:
        return english_letter_freq_monogram
    if n == 2:
        return english_letter_freq_bigram
    if n == 3:
        return english_letter_freq_trigram
    if n == 4:
        return english_letter_freq_quadgram


def get_n_gram_table(input_text, n):
    n_grams_result = n_grams(input_text, n)
    ref = dict(sorted(get_n_gram_ref(n).items(), key=lambda x: x[1], reverse=True))

    is_bigger_ref = len(ref.items()) > len(n_grams_result.items())
    
    current = list(n_grams_result.items())
    ref = list(ref.items())

    len_current = len(current)
    len_ref = len(ref)

    print(len_ref, len_current)
    
    if len_current > len_ref:
        ref += [('-', 0)] * (len(current) - len(ref))
    else:
        current += [('-', 0)] * (len(ref) - len(current))

    df = pd.DataFrame()
    df['Current'] = current
    df['Ref'] = ref

    return df


def chi(cipher, freq=english_letter_freq_monogram):

    c = Counter(cipher)
    c = dict(c)
    
    n = np.sum(list(c.values()))

    suma = 0

    for char in c.keys():
        current = c[char]
        expected = n * freq[char]

        suma += ((current - expected)**2)/current

    return suma


def n_grams(input_text, n):

    n_grams = [input_text[i:i+n] for i in range(len(input_text) - n)] 

    c = dict(Counter(n_grams))

    n = np.sum(list(c.values()))

    res = {k:(v/n) for k, v in c.items()}
    
    res = dict([(k, round(v * 100, 3)) for k, v in sorted(res.items(), key=lambda x: x[1], reverse=True)])

    return res


def translate(cipher, fr, to):
    txt = cipher
    x = fr
    y = to
    mytable = txt.maketrans(x, y)
    return txt.translate(mytable)


def blank_text(text, cipher_to_original):
    res = ""

    for char in text:
        if char in cipher_to_original:
            res += cipher_to_original[char]
        else:
            res += "_"

    return res

def translate_with(cipher, cipher_to_original):
    fr = "".join(list(cipher_to_original.keys()))
    to = "".join(list(cipher_to_original.values()))
    return translate(cipher, fr, to)

def chi_calc(cipher):
    n = len(cipher)
    c = dict(Counter(cipher))

    chi = 0
    for k in english_letter_freq_monogram.keys():
        if k in c:
            if_eng = n * english_letter_freq_monogram[k]
            chi += ((c[k] - if_eng)**2)/if_eng

    return math.sqrt(chi)


def find_min(cipher, current_key = {}):
    already = set(current_key.values())
    al = set(english_letter_freq_monogram.keys())

    possible = al.difference(already)
    dfs = []
    for char in possible:
        current_df = chi(cipher, char, current_key)
        dfs.append(current_df)

    return pd.concat(dfs).sort_values(by='chi', ascending=True)


def chi(cipher, test_char, current_key = {}):    
    already = set(current_key.values())
    al = set(english_letter_freq_monogram.keys())

    possible = al.difference(already)

    res = {}

    for char in possible:
        current = current_key.copy()
        current[test_char] = char
        current_text = translate_with(cipher, current)
        res[char] = {
            "rule": f"{test_char} => {char}",
            "new_text": current_text,
            "chi":  chi_calc(current_text)
        }

    return pd.DataFrame.from_dict(res, orient="index").sort_values(by='chi', ascending=True)




def find_not_decrypted(cipher, current_key):
    known = set(current_key.keys())
    al = set(cipher)

    need_find = al.difference(known)

    dfs = []
    for char in need_find: 
        df = chi(cipher, char, current_key)
        dfs.append(df)
        
    return pd.concat(dfs).sort_values(by='chi', ascending=True)

    







