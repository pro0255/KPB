import pandas as pd
import numpy as np

def generate_vigener_matrix(alphabet):
    l = len(alphabet)
    alphabet_c = list(alphabet.keys())
    matrix = np.zeros(shape=(l, l), dtype=str)

    for r_i in range(0, l):
        for c_i in range(0, l):
            matrix[r_i, c_i] = alphabet_c[(c_i + r_i) % l]  


    return pd.DataFrame(matrix, index=alphabet, columns=alphabet)

class VigenerCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.vigener_matrix = generate_vigener_matrix(alphabet)

    def encode(self, oa_text, key):
        sa_text = ""
        size_key = len(key)
        chars_key = list(key)

        for index_oa, char_oa in enumerate(oa_text):
            current_key_index = index_oa % size_key  
            current_key_char = chars_key[current_key_index]

            sa_text += self.vigener_matrix.loc[char_oa, current_key_char]


        return sa_text
    
    def decode(self, sa_text, key):
        oa_text = ""
        size_key = len(key)
        chars_key = list(key)

        for index_sa, char_sa in enumerate(sa_text):
            current_key_index = index_sa % size_key  
            current_key_char = chars_key[current_key_index]

            current_index = list(self.vigener_matrix.loc[:, current_key_char].values).index(char_sa)
            current_oa_char = self.vigener_matrix.iloc[current_index, 0]

            oa_text += current_oa_char


        return oa_text