from prep import amh_prep,phoneme_prep,clean_phoneme_prep


amh_prep('format/train_list.txt','clean_train_list.txt')
amh_prep('format/val_list.txt','clean_val_list.txt')

phoneme_prep('format/train_list.txt','pho_train_list.txt')
phoneme_prep('format/val_list.txt','pho_val_list.txt')

clean_phoneme_prep('format/train_list.txt','pho_cl_train_list.txt')
clean_phoneme_prep('format/val_list.txt','pho_cl_val_list.txt')