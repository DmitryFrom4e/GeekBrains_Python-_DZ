# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# сделал с учетом регистра...
def replace_symb(text_in, text_replace):
    text_out = " ".join([i for i in text_in.split() if text_replace not in i.lower()])
    return text_out
    
text_in = "Абв авварравоо абваоабВ орпоорпооап аБв ллдаплпа ккшщкущш роваоорва asasабвю АБВsddsdsds"
search_text = "абв"

print(text_in)
text_in = replace_symb(text_in, search_text)

print(text_in)



