

###  🟢 Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)


###  🟢 Update ve gereklilikler
```
sudo add-apt-repository ppa:openjdk-r/ppa
apt update && apt upgrade -y
sudo apt-get install openjdk-17-jdk
```

###  🟢 Sunucuya alert kurulumu
```
mkdir /srv/humanode/
cd /srv/humanode/
git clone --branch build https://github.com/gicu-adasanu/humanode-alert.git
cd humanode-alert
```

###  🟢 Telegram üzerinden ayarları yapma. Öncelikle Botfather a gidiyoruz.
```
https://t.me/BotFather
```

###  🟢 Aşağıdaki komut ile yeni bot oluşturmak istediğimiz söylüyoruz. Sonra sonu _bot şeklinde bitecek bir isim giriyoruz. herculesalert_bot vb. İsmi girince telegram size bir kod verecek (Use this token to access the HTTP API: xxx şeklinde) o kodu alıyoruz. 
```
/newbot
```

###  🟢 Aşağıdaki kod ile sunucu üzerinden bot tokeni kaydediyoruz. bot.token=your_bot_token (your_bot_token yerine size verilen tokeni yazıyorsunuz.)

```
nano "/srv/humanode/humanode-alert/application.properties"
```

###  🟢 Aşağıdaki kod ile java başlatıyoruz. Yukarıda 17 sürümünü indirmiştik. java --version ile kontrol edin 17 olması gerekiyor. kodlar çalışmaya başlayacak sonra ctrl a d ile çıkıyoruz.

```
java -Dspring.config.location=/srv/humanode/humanode-alert/application.properties -jar humanode-alert-1.0.0.jar
```

###  🟢 Botfather tarafından bize gönderilen son mesajdaki t.me/xxx_bot sekmesine giriyoruz. Burada /register kodunu uygulayınca bize aşağıdaki gibi bir mesaj veriyor. Mesajda yazıldığı gibi doğrulama öncesi bize bildirim gönderiyor.


You have successfully registered, you will receive alerts every day (if have enabled notifications) with time left to authenticate and a reminder alert once a minute, 5 minutes before expiry. To see commands for enable/disable notification type /help



##  🟢 Telegram botu komutları

/register
/enable_notification
/disable_notification
/get_bioauth_link
/help

