
### Airchains ZK-Rollups

- Availe göre anlatılmıştır.
- Bir çok key ve memo veriyor hepsini kaydedin.
- En son /root/.tracks/ dosyasını komple yedek alın


### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.xyz)


## 🟢 Sistem özellikleri
| Ram | cpu     | disk                      |
| :-------- | :------- | :-------------------------------- |
| `8GB`      | `4Core` | `200+ SSD` |

- Bunlar max gereksinim daha düşükte çalıştırabilir !


## 🟢 Go kuralım
```shell
cd $HOME && \
ver="1.21.3" && \
wget "https://golang.org/dl/go$ver.linux-amd64.tar.gz" && \
sudo rm -rf /usr/local/go && \
sudo tar -C /usr/local -xzf "go$ver.linux-amd64.tar.gz" && \
rm "go$ver.linux-amd64.tar.gz" && \
echo "export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin" >> $HOME/.bash_profile && \
source $HOME/.bash_profile && \
go version
```



## 🟢 Repo indirin
```shell
git clone https://github.com/airchains-network/evm-station.git
```

```shell
git clone https://github.com/airchains-network/tracks.git
```

```shell
git clone https://github.com/availproject/availup.git
```

## 🟢 Evm-Station kurun


- Screen Açın

```shell
screen -S evmstation
```


```shell
cd evm-station
```

- go bileşenleri kurun

```shell
go mod tidy
```

```shell
/bin/bash ./scripts/local-setup.sh
```

```shell
/bin/bash ./scripts/local-start.sh
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/7b3d993f-6a78-4b49-a87f-744b8cf289a8)



- Key alın bir yere kaydedin 

```shell
/bin/bash ./scripts/local-keys.sh
```

- ctrl + a + d screen çıkın


## 🟢 Avail çalıştırın.

- Screen Açın

```shell
screen -S avail
```

- çalıştırınca pub key verecek onu bir yere not edin. 

```shell
/bin/bash availup.sh --network "turing" --app_id 36
```

- ctrl + a + d screen çıkın


- Buradan Avail kelimelerinizi alın ve Polkadot yada Subwallet aktarın. Kelimeleri kaydedin
- Faucet token alın  https://faucet.avail.tools

```shell
nano /root/.avail/identity/identity.toml
```

## 🟢 Track çalıştırın.

- Screen Açın

```shell
sudo rm -rf ~/.tracks
```

- çalıştırınca pub key verecek onu bir yere not edin. 

```shell
cd tracks
```

```shell
go mod tidy
```

- İKİ YER DEĞİŞECEK 
- DAKEY : AVAIL KELİMELER
- MONİKER : MONİKER İSMİNİZ
- DA-RPC : avail


```shell
go run cmd/main.go init --daRpc "http://127.0.0.1:7000" --daKey "AVAİL-KELİMELERİ-YAZ" --daType "avail" --moniker "MONİKER-İSMİNİ-YAZ" --stationRpc "http://127.0.0.1:8545" --stationAPI "http://127.0.0.1:8545" --stationType "evm"
```

- HESAP İSMİ YAZIN 
- aircüzdan verecek kaydedin Discord girip faucet token alın $faucet aircüzdanınız

```shell
go run cmd/main.go keys junction --accountName HESAP-İSMİ-YAZIN --accountPath $HOME/.tracks/junction-accounts/keys
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/069b4cae-63e3-4531-b0e6-b486c8dcf368)


- Power başlatın

```shell
go run cmd/main.go prover v1EVM
```

- İstasyon Oluşturun
- Node id bu dosyada bulabilirsiniz .track/config/sequencer.toml
- CÜZDAN İSMİNİZ
- CÜZDANINIZI YAZIN Air cüzdanınızı yazın 

- /ip4/SUNUCU-İP-YAZ/tcp/2300/p2p/NODE-ID-YAZ  BU KISMI DEĞİŞTİRİN İP ADRESİNİZ VE NODE İD aşağıdaki sequencer.toml içnde bulabilirsiniz.

`nano /root/.tracks/config/sequencer.toml`

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/b132d4bf-812c-4469-9200-d107096b3dd5)


```shell
go run cmd/main.go create-station --accountName CÜZDAN-İSMİNİZ --accountPath $HOME/.tracks/junction-accounts/keys --jsonRPC "https://airchains-testnet-rpc.cosmonautstakes.com/" --info "EVM Track" --tracks AİR-CÜZDANINIZI-YAZIN --bootstrapNode "/ip4/SUNUCU-İP-YAZ/tcp/2300/p2p/NODE-ID-YAZ"
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/bcc00dfc-3fc3-4588-a06e-ed05d4609de8)


- Başlatın

```shell
go run cmd/main.go start
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/13ce14c7-cf11-41a0-9919-bb38573b37f3)


## 🟢 Puanlara bakın

- Bu adrese gidin Leap Wallet kurun ve air hesabınızın memolarını aktarın bağlanın
- https://points.airchains.io/

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/373cd65e-17ac-48fe-8549-b6c4efb1d724)



airchains validatoru DOUBLELIFT Teşekkürler..


