from DataPreprocessor.cleaner import amharic_cleaners
from DataPreprocessor.Amh_cleaner import Cleaner
#load phonemizer
import phonemizer
global_phonemizer = phonemizer.backend.EspeakBackend(language='am', 
                                                     preserve_punctuation=True,  
                                                     with_stress=True, 
                                                     language_switch='remove-flags',
                                                     words_mismatch='ignore')

def phoneme_prep(input_path:str,out_path):
    # input_path /content/drive/MyDrive/ASR/item_list.txt'
    # out_path /content/drive/MyDrive/ASR/item_IPA_list.txt'
    item_list = open(input_path,'r',encoding='utf8').read()
    item_new = []
    item_texts = item_list.splitlines()
    for text in item_texts:
        writable = text.split('|')
        writable[1] = global_phonemizer.phonemize([writable[1]])[0]
        item_new.append('|'.join(writable))
    open(out_path,'w',encoding='utf8').write('\n'.join(item_new))

def amh_prep(input_path:str,out_path):
    # input_path /content/drive/MyDrive/ASR/item_list.txt'
    # out_path /content/drive/MyDrive/ASR/item_IPA_list.txt'
    item_list = open(input_path,'r',encoding='utf8').read()
    item_new = []
    item_texts = item_list.splitlines()
    for text in item_texts:
        writable = text.split('|')
        writable[1] = amharic_cleaners(writable[1])
        item_new.append('|'.join(writable))
    open(out_path,'w',encoding='utf8').write('\n'.join(item_new))

def amh_prep(input_path:str,out_path):
    # input_path /content/drive/MyDrive/ASR/item_list.txt'
    # out_path /content/drive/MyDrive/ASR/item_IPA_list.txt'
    item_list = open(input_path,'r',encoding='utf8').read()
    item_new = []
    item_texts = item_list.splitlines()
    for text in item_texts:
        writable = text.split('|')
        writable[1] = amharic_cleaners(writable[1])
        item_new.append('|'.join(writable))
    open(out_path,'w',encoding='utf8').write('\n'.join(item_new))

def clean_phoneme_prep(input_path:str,out_path):
    # input_path /content/drive/MyDrive/ASR/item_list.txt'
    # out_path /content/drive/MyDrive/ASR/item_IPA_list.txt'
    item_list = open(input_path,'r',encoding='utf8').read()
    item_new = []
    item_texts = item_list.splitlines()
    for text in item_texts:
        writable = text.split('|')
        # Text Cleaned by cleaners then feed to phonemizer
        writable[1] = global_phonemizer.phonemize([Cleaner(writable[1]).clean()])[0]
        item_new.append('|'.join(writable))
    open(out_path,'w',encoding='utf8').write('\n'.join(item_new))