
###  🟢 Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)

Öncelikle https://playground.dymension.xyz/ sitesine girmek için ana ağda en az 5 DYM stake etmelisiniz. Bunun için siteye girdikten sonra size gerekli talimatları gösterecek. 

Benim oluşturduğum RollApp
https://playground.dymension.xyz/rollapps/akirafudo_20433-1/dashboard





1. Sisteminizi Güncelleyin 🟢
Bağımlılıkları yüklemeden önce, sisteminizin güncel olduğundan emin olun:

```
sudo apt update && sudo apt upgrade -y
```

2. Gerekli Paketleri Yükleyin
Temel paketleri yükleyin:

```
sudo apt install -y build-essential clang curl aria2 wget tar jq libssl-dev pkg-config make
```

Docker Kurulumu
Docker API Sürümünü Ayarlayın:

```
export DOCKER_API_VERSION=1.41
```

Docker Deposu Kurulumu:
Docker'ın resmi GPG anahtarını ekleyin:

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Docker deposunu Apt kaynaklarına ekleyin:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
sudo apt-get update
```

Docker paketlerini yükleyin:

```
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Docker yetkisi verin:

```
sudo usermod -aG docker ${USER}
```


Go Yükleme:
Go'yu indirin ve yükleyin:

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

Go'yu PATH'e ekleyin:

```
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```
Kurulumu doğrulayın: go version go1.23.0 linux/amd64 olarak görmelisiniz.

```
go version 
```


Roller Kurulumu
Roller'ı yükleyin:
```
curl https://raw.githubusercontent.com/dymensionxyz/roller/main/install.sh | bash
```

Kurulumu doğrulayın:💈 Roller version 1.6.4-alpha-rc06 olarak görmelisiniz.

```
roller version
```

RollApp Başlatma
RollApp dizinini başlatmak için komutu çalıştırın: Sitede oluşturduğunuz Rollapp adını buraya gireceksiniz.

```
roller rollapp init
```

Başarılı bir kurulumdan sonra şu çıktıyı göreceksiniz:

```
💈 RollApp 'rollapp_12345-1' yapılandırma dosyaları yerel makinenizde başarıyla oluşturuldu.
```


RollApp Uç Noktalarını Ayarlayın
Telebit CLI'yi yükleyin:
```
curl https://get.telebit.io/ | bash
```

Gerekli uç noktaları oluşturun:

```
~/telebit http 1317 rest
~/telebit http 8545 evm
~/telebit http 26657 rpc
```

Uç noktaları kaydedin:

```
~/telebit save
```


RollApp Sequencer Ayarlama
RollApp sequencer'ını kurmak için aşağıdaki komutu çalıştırın:
```
roller rollapp setup
```

Sequencer'ı başlatın: (Arka planda çalıştırma kodları)

```
roller rollapp services load
```
```
roller rollapp services start
```
RollApp durumunu kontrol edin:

```
roller rollapp status
```

Relayer Kurulumu

IBC bağlantısını kurun:
```
roller relayer setup
```

Relayer'ı başlatın:


Relayer servislerini yükleyin:
```
roller relayer services load
```

Relayer servislerini arka planda başlatın:
```
roller relayer services start
```


eIBC İstemcisini Yapılandırın
RollApp'ları Beyaz Listeye Alın
İlk olarak, rollapp'ı beyaz listeye alarak başlayalım:  (roller eibc fulfill rollapps set xxx_1234-1 0.01)
```
roller eibc fulfill rollapps set <rollapp_id> <fee-in-percentage>
```

Token'ları Beyaz Listeye Alın:  <denom-on-the-token-registry> sitede oluşturduğunu token adı. Büyük harfle yazın.
```
roller eibc fulfill denoms set <denom-on-the-token-registry> <fee-in-percentage>
```


eIBC İstemcisini Başlatın

Eibc servisini yapılandırın.

```
roller eibc services load
```
eIBC servisini arka planda başlatın.
```
roller eibc services start
```

Bakiye Görüntüleme
```
roller eibc funds
```

Yararlı kodlar.

İbc yeniden başlatma.

roller eibc services restart

relayer yeniden başlatma.
roller relayer services restart

rollapp yeniden başlatma.
roller rollapp services restart

Ayrıca 
journalctl -fu relayer
journalctl -fu rollapp
journalctl -fu eibc
bu kodlar ile de bakabilirsiniz.
