# Val Prep ### DONE ###
# text_val = open('val_list.txt','r',encoding='utf8').read()
# audio_val = open('item_val.txt','r').read()

# texts = text_val.splitlines()
# audios = audio_val.splitlines()


# if(len(texts) != len(audios)):
#     # their size should match
#     raise RuntimeError

# # Format
# # 01_d501025.wav , ችግሮቹን ደግሞ ማስወገድ ነበረ ባቸው | aud,txt
# # LJSpeech-1.1/wavs/{audio}|{text}|0
# naming = []
# for idx in range(len(audios)):
#     spk = audios[idx].split('_')[0]
#     naming.append(f'LJSpeech-1.1/wavs/{audios[idx]}|{texts[idx]}|{spk}')

# with open('train.txt','w', encoding='utf8') as f:
#     f.write('\n'.join(naming))

# Train Prep
text_val = open('train_list.txt','r',encoding='utf8').read()
audio_val = open('item_train.txt','r').read()

texts = text_val.splitlines()
audios = audio_val.splitlines()


if(len(texts) != len(audios)):
    # their size should match
    raise RuntimeError

# Format
# tr_dw_01_10002.wav , ችግሮቹን ደግሞ ማስወገድ ነበረ ባቸው | aud,txt
# LJSpeech-1.1/wavs/{audio}|{text}|0
naming = []
for idx in range(len(audios)):
    spk = audios[idx].split('_')[2]
    naming.append(f'LJSpeech-1.1/wavs/{audios[idx]}|{texts[idx]}|{spk}')

with open('train.txt','w', encoding='utf8') as f:
    f.write('\n'.join(naming))