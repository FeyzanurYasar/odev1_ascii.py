# odev1_ascii.py
# odev1_ascii.py
print('Ascii Kodu | karakter')
print('-----------|---------')
for kod in range(128): #0-127) arasındaki kodlar (sayılar) için

    if (0<= kod <= 31) or (kod == 127):
        karakter = 'Kontrol karakterleri' #0-31 arası ve 127 kontrol karakteri
    elif kod == 32:
        karakter = '(boşluk)' #32 boşluk karakteri

    else:  #Diğer karakterler 
        karakter = chr(kod)
    print(kod, '           |', karakter)   
