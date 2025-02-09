### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Gaia Discord](https://discord.com/invite/gaianet-ai)
 * [Gaia Portal](https://gaianet.ai/reward?invite_code=R7jjji)

## 🟢Gaia Gösterge Paneli
Gaia XP programında, Gaia AI Ajanları ile etkileşim kurarak ve Gaia düğümleri çalıştırarak puan biriktiriyoruz.

## 🟢Cüzdanınızı Gaia Gösterge Paneli ile bağlayın ve kaydınızı tamamlayın.
-https://gaianet.ai/reward?invite_code=R7jjji

-XP’nizi artırmak için bu davet kodunu kullanın: R7jjji

-Ödüller Özeti bölümündeki sosyal görevleri tamamlayın.

## 🟢Gaia Düğümü Kurulumu
Aşağıdaki adımları izleyerek Node Puanları ve Kullanıcı Puanları kazanabilirsiniz:

## 🟢Düğümü kurma
-Düğümünüzü çevrimiçi tutma ve isteklere yanıt verme
-Bir Domain’e katılma
-Katıldığınız domain’e bağlı AI ajanı ile sohbet etme
## 🟢 1. Sistem Gereksinimleri
Qwen2 0.5B Instruct modelini çalıştırabilmek için aşağıdaki sistem gereksinimlerini karşılamanız gerekir:


CPU: 4 çekirdek

RAM: 8GB

Depolama: 10GB


## 🟢 2. Bağımlılıkları Kurma
Paketleri güncelleyin:

```shell
sudo apt update && sudo apt upgrade -y
```

Python’u yükleyin:

```shell
sudo apt install -y python3-pip
sudo apt install pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
## 🟢 3. Gaia Node CLI Kurulumu
Aşağıdaki komutu çalıştırarak Gaia Node CLI’yi yükleyin:

```shell
curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/install.sh' | bash
```
Kurulumdan sonra terminali yeniden başlatın veya şu komutu çalıştırın:

```shell
source /root/.bashrc
```

## 🟢 4. Gaia Düğümünü Yapılandırma
Aşağıdaki komut ile Qwen2 0.5B Instruct modelini indirerek düğümünüzü başlatın:

```shell
gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/qwen2-0.5b-instruct/config.json
```
## 🟢 5. Gaia Düğümünü Başlatma

Gaia düğümünü çalıştırarak, belirli bir AI Modeli ile etkileşim kurabileceğimiz bir AI Ajanı dağıtmış oluyoruz.

## 🟢 Düğümü Başlat

```shell
gaianet start
```

Düğümü Durdur (Opsiyonel)
```shell
gaianet stop
```

## 🟢 6. Düğümü Gaia Gösterge Paneline Kaydetme
Node ID ve Device ID bilgilerini almak için şu komutu çalıştırın: 

```shell
gaianet info
```
https://www.gaianet.ai/setting/nodes sayfasında connect new node dediğinizde bu bilgileri gireceksiniz.

## 🟢 7. Bir Domain’e Katılma

Node Puanı kazanmak için bir domain’e katılmalı ve AI ajanı ile sohbet etmelisiniz.
Kendi düğümünüz ile sohbet etmek puan kazandırmaz.
Aşağıdaki komutları terminalde çalıştırın: gaia.domains değiştirmiyoruz. Bir sonraki kısımda portaldan domain seçeceğiz.

```shell
gaianet stop
gaianet config --domain gaia.domains
gaianet init
gaianet start
```
Node Ayarları sayfasına gidin.

Aktif düğümünüzün yanındaki üç noktaya tıklayın ve Join Domain seçeneğini seçin.
Sonraki adımları takip edin.

pengu.gaia.domain adlı domain’i arayın ve katılın. Pengu ya katılamayanlar başka domain seçebilir.

## 🟢8. Düğümünüzle Sohbet Edin
Düğümünüzle etkileşime geçmek ve XP kazanmak için: Pengu Gaia Domain adresini ziyaret edin.

Sohbet etmek için Kredi Bakiyesi gereklidir.
GaiaPoints’lerinizi her gün Kredi Bakiyesi’ne dönüştürün.
GaiaPoints değeriniz aynı kalır, ancak günde 1000 puan çevirebilirsiniz. Fazla kullanırsanız eksiye düşer.

## 🟢9. Otomatik Sohbet Botunu Çalıştırma
API Anahtarı Oluşturun: https://www.gaianet.ai/setting/gaia-api-keys

Gaia API Anahtarları sayfasına gidin ve yeni bir anahtar oluşturun. Anahtarı bir yere kaydedin.
Python Script’i İndirin:

Terminalde aşağıdaki komutu çalıştırın:

```shell
curl -L -o gaiabot.py https://raw.githubusercontent.com/HerculesNode/Testnet-Rehber/refs/heads/main/Gaia/bot.py
```
Script’i Çalıştırın:
Bir önceki işlemleri screen içinde yaptıysanız screen den ctrl a d ile çıkın tekrar screen oluşturun

Terminalde bir screen açarak botu arka planda çalıştırın:
```shell
screen -S gaiabot
```
Botu başlatın:
```shell
python3 gaiabot.py
```
Gaia API anahtarınızı girin.
Screen’i küçültmek için Ctrl+A+D tuşlarına basın.

Geri dönmek için şu komutu çalıştırın: screen -r gaiabot

Durdurmak için CTRL+C tuşlarına basıp ardından şu komutu çalıştırın: screen -XS gaiabot quit

Bazı ağ yoğunlukları nedeniyle başarısız girişimler olabilir, ancak birkaç denemeden sonra başarılı sonuç alabilirsiniz.

## 🟢10. Puan Kazanma
Bu adımları takip ettiğinizde Puanlarınız her 24 saat veya daha uzun bir sürede güncellenecektir.

Kullanıcı Puanları: Kendi domain’iniz veya diğer domain’lerle sohbet ederek kazanılır.

Node Puanları: Düğümünüzün çevrimiçi kalması ve bağlı olduğu domain ile sohbet etmesi ile kazanılır.

Eğer yerel bir bilgisayar (Windows veya Linux) kullanıyorsanız, düğümünüzü ve sohbet botunu her gün yeniden çalıştırabilirsiniz
