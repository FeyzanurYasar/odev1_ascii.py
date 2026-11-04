print('Döngülü Hesap Makinesi')
while True: #Programın sonsuz döngü içine girmesini sağlar,ve işlem bittiğinde menüye tekrar döner.
    print("--------------------------------")
    print('+ Toplama (+)')
    print('-Çıkarma (-)')
    print('*Çarpma (*)')                 
    print('/Bölme (*)')
    print('**Üst Alma (**)')     
    print('// Tam Bölme (//)')
    print('q Çıkış') #Kullanıcının programdan çıkması için.
    print("--------------------------------")

    #Kullanıcıdan işlem alıyoruz.
    secim = input('Yapmak istediğiniz işlemi girin (+,-,/,*,//,** veya çıkış için 'q'):')

    #Çıkış koşulu
    if seçim.lower() == 'q':  #seçim.lower() sayesinde Q yazıldığında dahi program çalışmaya devam eder.
    print('Hesap makinesinden çıkılıyor.')
    break #döngüyü kır.

    # İşlemin geçerli olup olmadığını kontrol et
    if secim in ('+', '-','*', '/', '**', '//'): #seçilen işlemdeki karakterin parantez içindekiyle örtüşüp örtüşmemesi kontrol edilir,
    try: #try ve excapt ikilisi birbirinden ayrılmaz. işlem yapmayı deneyin (try) eğer kullanıcı kullanıcı harf girerse ve değer hatası (excapt ValueError) çıkarsa uyarı göster devam et
    sayi1 = float(input('Birinci sayıyı girin: ')) #float küsüratlı rakam ve sayılar için
    sayi2 = float(input('İkinci sayıyı girin: '))  #float küsüratlı rakam ve sayılar için
    print("--------------------------------")

#Toplama
if secim== '+':
   sonuç = sayi1 + sayi2 
   print(f'Sonuç: {sayi1} + {sayi2} = {sonuc}')

#Çıkarma
if secim == '-': 
   sonuc = sayi1 - sayi2
    print(f'Sonuç: {sayi1} - {sayi2} = {sanuc}')

#Çarpma
if secim == '*':
   sonuc = sayi1 * sayi2
print(f'Sonuç: {sayi1} * {sayi2} = {sanuc}')

#Bölme
if seçim == '/':
    if sayi2 != 0:  #sayi2 0 ise işlem yapma.
    sonuc = sayi1 / sayi2
    print(f'Sonuç: {sayi1} / {sayi2} = {sanuc}')
else:  #if değilse else de olabilr

#Üst Alma 
elif secim == '**'
sonuc = sayi1 ** sayi2
print(f'Sonuç: {sayi1} ** {sayi2} = {sanuc}')

#Tam Bölme
elif secim == '//':
    if sayi2 !=0:
    sonuc = int(sayi // sayi2) 
    print(f'Sonuç: {sayi1} // {sayi2} = {sanuc}')
    print('Hata bir sayi 0 bölünemez!')
except ValueError: #try ve excapt ikilisi birbirinden ayrılmaz. işlem yapmayı deneyin (try) eğer kullanıcı kullanıcı harf girerse ve değer hatası (excapt ValueError) çıkarsa uyarı göster devam et
print('Hata: geçerli bir sayı giriniz!')
else:
print('Geçeraiz seçim yaptınız! Lütfen +,-,*,/,**,// veya çıkış için 'q' giriniz.'




                 
      

    
