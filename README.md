# Lost Ark Balık botu

# Yükleme
* python kur: https://www.python.org/downloads/
* pip kur:  ```py -m ensurepip --upgrade```
* Repoyu klonla: ```git clone https://github.com/gms10ur/LostArkBalikBotu.git```
* klonladığın klasöre gel: ```cd LostArkBalikBotu```
* gerekli kütüphaneleri yükle: ```pip install -r requirements.txt```
* çalıştır: ```python bot.py``` veya ```python antiafk.py```

# Nasıl Çalışır?
* bot.py, atışlar arasında herhangi bir duraklama olmadan balık tutar ve belirli aralıklarla oltayı otomatik olarak onarır. 
* antiafk.py ise aynı işi yapar ama her atış arasında 8.5 - 10 Dk arası bekleme yaparak enerjinizi korumanızı sağlar.

# Oyun ayarları ve Tuş Atamaları
* sadece üç ayara ihtiyacınız var!
* balık tutma E Tuşunda:\
  ![alt text](https://i.imgur.com/zI3m8Bd.png)
* otomatik tamir için pet menüsü ALT+P tuşlarında (sadece premium için, eğer sizde premium yoksa lütfen tamir bool değerini false yapın):\
  ![alt text](https://i.imgur.com/L85XF6q.png)
* oyun pencere ayarı: "Borderless" --> kenarlıksız olursa ALT+TAB atmanız çok kolay olur.
* şu anda yükseklik değeri 1080, 1440 ve 2160 piksel olan tüm çözünürlükler destekleniyor.

# Kullanım
* balık tutmaya başlamak için oyun içinde bir balık tutma noktasına gidin, bot.py veya antiafk.py'yi başlatın ve oyuna geri dönün. İkinci bir monitörünüz varsa açılan konsol penceresinden bot çıktısını izleyebilirsiniz.

# .py dosyalarını açarken sorun yaşıyorum kardeş diyorsan bu şekilde .exe'ye dönüştürebilirsin:
1. pyinstaller yükle: ```pip install pyinstaller```
2. Şu komutu gir: ```pyinstaller --add-data "resources;resources" bot.py```
3. Yeni exe dosyan şurada olacak: ```dist\bot\bot.exe ```

# Uyarı
* Ban yeme ihtimaliniz %0.000000001 ama yine de ban yerseniz gelip bana ağlamayın.