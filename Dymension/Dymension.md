Hazırlayan: [@omerbektasX ](https://t.me/omerbektasx)

###  🟢 Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)
 * [Dymension Discord](https://discord.gg/9zGfcRk2)

###  🟢 HerculesNode Team rollapps 
- @omerbektasX https://playground.dymension.xyz/rollapps/akirafudo_20433-1/dashboard - Token ismi : AKIRA
- @HerculesNode https://playground.dymension.xyz/rollapps/hercules_10238-1/dashboard - Token ismi : RUTE 
- @eftayaksular https://playground.dymension.xyz/rollapps/yukovskiwars_10426-1/dashboard - Token ismi : WAR 

###  🟢 HerculesNode Telegram Token botu ile Faucet dağıtın <br>
Rehber: https://github.com/HerculesNode/Testnet-Rehber/blob/main/Dymension/faucet.md



###  🟢 playground Kurulum işlemleri 

### Öncelikle https://playground.dymension.xyz/ sitesine girmek için ana ağda en az 5 DYM stake etmelisiniz. Bunun için siteye girdikten sonra size gerekli talimatları gösterecek. 

Mainnet Stake etme adresi : https://portal.dymension.xyz/

### İhtiyaç olacak DYM ler:
1- Domain almak için 5 adet ( isim )
2- Stake yapmak için 10.1 adet
3- Squencer için 20 adet
4- Ayrıca mocha ağında tia gerekiyor Celestia discord adresinden alabilirsiniz. 
### Adresleri size kodlar çıktı olarak verecek.

### Dym Discord adresine gidin $request cüzdan-adresi (dym....) yazarak faucet isteyin. 




İlk olarak sitemize giriyoruz. Resim domain ve roll app id giriyoruz. Burada isim uzunluğuna göre dym istiyor. Ekran görüntülerinde adım adım yapılacaklar var.

![dym1](https://github.com/user-attachments/assets/9f171e17-8abd-4371-bfa2-3fa402cc23d4)



![dym2](https://github.com/user-attachments/assets/1dba80fd-8de2-4d61-92f3-cec83a7abddb)


![dym3](https://github.com/user-attachments/assets/441b51b2-ee77-4433-9c2b-a82a439fa675)




###  1. Sisteminizi Güncelleyin 🟢
Bağımlılıkları yüklemeden önce, sisteminizin güncel olduğundan emin olun:

```
sudo apt update && sudo apt upgrade -y
```

### 2. Gerekli Paketleri Yükleyin
Temel paketleri yükleyin:

```
sudo apt install -y build-essential clang curl aria2 wget tar jq libssl-dev pkg-config make
```

### Docker Kurulumu
Docker API Sürümünü Ayarlayın:

```
export DOCKER_API_VERSION=1.41
```

### Docker Deposu Kurulumu:
### Docker'ın resmi GPG anahtarını ekleyin:

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Docker deposunu Apt kaynaklarına ekleyin:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get update
```

### Docker paketlerini yükleyin:

```
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Docker yetkisi verin:

```
sudo usermod -aG docker ${USER}
```


### Go Yükleme:
### Go'yu indirin ve yükleyin:

```
ver="1.23.0"
```

```
cd $HOME
wget "https://golang.org/dl/go$ver.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$ver.linux-amd64.tar.gz"
rm "go$ver.linux-amd64.tar.gz"
```

### Go'yu PATH'e ekleyin:

```
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```
### Kurulumu doğrulayın: go version go1.23.0 linux/amd64 olarak görmelisiniz.

```
go version 
```


### Roller Kurulumu
### Roller'ı yükleyin:
```
curl https://raw.githubusercontent.com/dymensionxyz/roller/main/install.sh | bash
```

### Kurulumu doğrulayın:💈 Roller version 1.6.4-alpha-rc06 olarak görmelisiniz.

```
roller version
```

### RollApp Başlatma
### RollApp dizinini başlatmak için komutu çalıştırın: Sitede oluşturduğunuz Rollapp adını buraya gireceksiniz.

```
roller rollapp init
```
![Dym 4](https://github.com/user-attachments/assets/ab472f45-2a2b-4b07-9872-2b0e9ea517db)

### Başarılı bir kurulumdan sonra şu çıktıyı göreceksiniz:

```
💈 RollApp 'rollapp_12345-1' yapılandırma dosyaları yerel makinenizde başarıyla oluşturuldu.
```


### RollApp Uç Noktalarını Ayarlayın
### Telebit CLI'yi yükleyin:
![dym5](https://github.com/user-attachments/assets/6caf4178-8ea5-4d6c-aa22-3cb3d28d9231)
```
curl https://get.telebit.io/ | bash
```

### Gerekli uç noktaları oluşturun:

```
~/telebit http 1317 rest
~/telebit http 8545 evm
~/telebit http 26657 rpc
```

### Uç noktaları kaydedin:

```
~/telebit save
```

### RollApp Sequencer Ayarlama
### RollApp sequencer'ını kurmak için aşağıdaki komutu çalıştırın:
![dym6](https://github.com/user-attachments/assets/0c7cb41c-9b2e-47ce-bdcf-23a5fd303920)

![dym7](https://github.com/user-attachments/assets/f067ee10-000b-4d5f-83c6-5b958ad74f5f)
```
roller rollapp setup
```

### Sequencer'ı başlatın: (Arka planda çalıştırma kodları)

```
roller rollapp services load
```
```
roller rollapp services start
```
### RollApp durumunu kontrol edin:

![dym8](https://github.com/user-attachments/assets/28f26749-b05c-42d2-aa02-561e15492cc6)

```
roller rollapp status
```

### Relayer Kurulumu

### IBC bağlantısını kurun:

```
roller relayer setup
```
![dym9](https://github.com/user-attachments/assets/4eeee1e0-22ae-4a47-8f91-f41d141246b6)

### Relayer'ı başlatın:


### Relayer servislerini yükleyin:
```
roller relayer services load
```
### Relayer servislerini arka planda başlatın:
```
roller relayer services start
```

# eIBC Client Başlatma ve Whale Hesabını Fonlama

Bu adımlar, Dymension ağı üzerinde bir **whale** hesabı oluşturarak eIBC client'ını başlatmayı ve bu hesabı uygun denoms ile fonlamayı içerir. DYM fonlaması zorunludur, çünkü ağ üzerindeki işlem ücretlerini karşılamak için DYM gerekmektedir.

## Adımlar

### eIBC Client'ı Başlatma

eIBC client'ını başlatmak için aşağıdaki komutu çalıştırın:

```
roller eibc init
```

### eIBC İstemcisini Yapılandırın
### RollApp'ları Beyaz Listeye Alın
### İlk olarak, rollapp'ı beyaz listeye alarak başlayalım:  (roller eibc fulfill rollapps set xxx_1234-1 0.01)
```
roller eibc fulfill rollapps set <rollapp_id> <fee-in-percentage>
```

### Token'ları Beyaz Listeye Alın:  <denom-on-the-token-registry> sitede oluşturduğunu token adı. Büyük harfle yazın.
```
roller eibc fulfill denoms set <denom-on-the-token-registry> <fee-in-percentage>
```


### eIBC İstemcisini Başlatın
### Eibc servisini yapılandırın.

```
roller eibc services load
```
eIBC servisini arka planda başlatın.
```
roller eibc services start
```

### Bakiye Görüntüleme
```
roller eibc funds
```

### Tokenleri bastık şimdi sıra portal üzerinden yeşil yani active olmasını bekleyeceğiz. Çok fazla sürerse "roller relayer services restart" relayer yeniden başlatın.
### Yeşili gördük mü? Umarım görmüşünüzdür. Aşağıdaki gibi aktif olduğunda üst sekmeden transferi tıklıyoruz.


![dym10](https://github.com/user-attachments/assets/9e417212-f91b-4ea7-9a3e-b6ad4ac5d8c5)

### Aşağıdaki gibi onaylandığı zaman pool oluşturma vakti.
![image](https://github.com/user-attachments/assets/a8d6850a-2779-4cf8-b4dd-5d9dba4519a8)


### Pool kısmına giriyoruz.
![dym11](https://github.com/user-attachments/assets/1b6368d7-1488-4890-9993-1e066f81ea53)


### Artık her şey hazır. 

![image](https://github.com/user-attachments/assets/cf6abde6-39fb-4f13-b470-fb524c6bf627)


![image](https://github.com/user-attachments/assets/16a17909-9ef6-4aef-8f11-9e58172cf141)



### Yararlı kodlar.

### İbc yeniden başlatma.
roller eibc services restart

### relayer yeniden başlatma.
roller relayer services restart

### rollapp yeniden başlatma.
roller rollapp services restart

### Ayrıca 
journalctl -fu relayer <br>
journalctl -fu rollapp <br>
journalctl -fu eibc <br>
bu kodlar ile de bakabilirsiniz.
