
### Farcaster Node Hubble


### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)
 * [Hercules Warpcast](https://warpcast.com/herculesnode)

 * Resmi döküman : https://docs.farcaster.xyz/hubble/hubble - https://www.thehubble.xyz/intro/hubble.html


## 🟢 Ön Bilgilendirme
- Bu işlem ile Farcaster üzerinde bir Node çalıştırabilirsiniz. 
- Bunu yapabilmek için Warpcast hesabınızın olması gerekiyor yoksa buradan üye olun 5$ maliyeti var
- https://warpcast.com/~/invite-page/290828?id=b3af94ef


## 🟢 özellik
- 16GB Ram istiyor. Fakat gözlemlediğime göre 16GB ram kullanmıyor daha az olabilir. Kurulumda 16GB istiyor 
- 4CPU
- 200 GB+
- Port 2281 - 2283 - Grafana için : 3000




## 🟢 Güncellemeler
```shell
sudo apt update -y
```

```shell
sudo apt upgrade -y
```

```shell
sudo apt install screen -y
```

```shell
screen -S warp
```



## 🟢 Docker indirelim	

- Docker kurulu ise önce `docker --version` komutuyla versiyon kontrolü yapın. Resimdeki gibiyse kurmanıza gerek yok. Değilse aşağıdaki komutlar ile kurun

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/f7f9d70c-422b-4839-a8ad-e0daa12f4977)



```shell
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
```shell
sudo mkdir -p /etc/apt/keyrings
```

```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```shell
sudo apt-get update
```

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```shell
sudo systemctl start docker
sudo systemctl enable docker
```

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```shell
sudo chmod +x /usr/local/bin/docker-compose
```


## 🟢 Tek kod kurulum çalıştıralım

```shell
curl -sSL https://download.thehubble.xyz/bootstrap.sh | bash
```

- Burada sizden ETH , OP mainnet ağında RPC isteyecek.  
- Alabileceğiniz yerler :  https://app.infura.io/dashboard ve https://www.alchemy.com/  buradan temin edebilirsiniz. 

#### 1-ETH mainnet RPC linkini girin
#### 2-Op Mainnet RPC linkini girin
#### 3-Warpcast FID numaranızı girin Profiliniz sağ üstten 3 çizgi ve About butonuna basın çıkıyor.

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/24432e01-c9c7-4a8c-b983-cf373f380082)



## 🟢 Sonuç izleme


- Aşağıdaki gibi çıktı almalısınız. Öncelikle Snap yükleyecek biraz uzun sürüyor ondan sonra resimdeki gibi bir ekran gelecek.
- Aşağıdaki kod ile FID doğrumu kontrol edebilirsiniz. 

```shell
docker logs hubble-hubble-1 2>&1 | grep "Hub Operator FID"
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/d0a4598e-b3a4-4ee3-a22b-5319f85c5c4f)


![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/80611013-b51f-4c52-9fed-1284357d430f)


- Ayrıca grafana ile kontrol edebilirsiniz.  http://SUNUCU-IP:3000 şeklinde

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/1496c07d-c8b2-44ec-86ae-6b5fcada0526)


## 🟢 Sağlıklı bir kurulumda aşağıdaki gibi dosyalar olması gerekiyor. 

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/cec5a452-e898-4801-a370-c39ea0bc96b1)



## 🟢 Yükseltme işlemi ( upgrade ) Bunu otomatik yapıyor. Manuel kullanmak isterseniz 

```shell
cd ~/hubble && ./hubble.sh upgrade
```


## 🟢 Yararlı komutlar

```shell
cd ~/hubble 
```

- Loglara bakma

```shell
./hubble.sh logs
```

- Durdurma 
```shell
./hubble.sh down
```

- Yeniden başlatma

```shell
./hubble.sh up
```

- veritabanı sıfırlama

```shell
rm -rf .rocks
```


#### Senktonize oldummu ? Bunun için grafana panelinize bakın aşağıdaki resimdeki gibi ise sorun yok %100 gösteriyorsa senkronize oldu demektir. değilse yeniden başlatın

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/dd393a7a-135a-4d2f-95be-f36ec884eb15)

