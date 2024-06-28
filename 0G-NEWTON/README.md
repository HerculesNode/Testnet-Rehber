![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/9f3bd440-d371-47b5-afcd-f0d0f4e342d1)

### zgtendermint_16600-2  -  v0.2.3

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [OG Discord](https://discord.gg/0glabs)
 * [HerculesNode Explorer](https://explorer.herculesnode.com/0G-Testnet/staking)


## 🟢 rol alma

- Discord Roles kanalına gidin ve rolleri alın

![image](https://github.com/HerculesNode/0G-Testnet/assets/101635385/c2ddbff1-1989-4f63-8b20-cf3ebb368442)


## 🟢 Sistem özellikleri
| Ram | cpu     | disk                      |
| :-------- | :------- | :-------------------------------- |
| `8GB`      | `4Core` | `500+ SSD` |

- Bunlar max gereksinim daha düşükte çalıştırabilir !

## 🟢 Sistemi güncelleyelim
```shell
sudo apt update && \
sudo apt install curl git jq build-essential gcc unzip wget lz4 -y
```

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

## 🟢 Dosyaları indirin v0.2.3
```shell
git clone -b v0.2.3 https://github.com/0glabs/0g-chain.git
./0g-chain/networks/testnet/install.sh
source .profile
```

```shell
mkdir -p $HOME/.0gchain/cosmovisor/genesis/bin
mv /root/go/bin/0gchaind $HOME/.0gchain/cosmovisor/genesis/bin/
```
## 🟢 System
```shell
sudo ln -s $HOME/.0gchain/cosmovisor/genesis $HOME/.0gchain/cosmovisor/current -f
sudo ln -s $HOME/.0gchain/cosmovisor/current/bin/0gchaind /usr/local/bin/0gchaind -f
```
```shell
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.5.0
```

## 🟢 Servis oluşturun

```shell
sudo tee /etc/systemd/system/0gchaind.service > /dev/null << EOF
[Unit]
Description=0gchaind node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.0gchain"
Environment="DAEMON_NAME=0gchaind"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.0gchain/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
```

```shell
sudo ln -s $HOME/.0gchain/cosmovisor/genesis $HOME/.0gchain/cosmovisor/current -f
sudo ln -s $HOME/.0gchain/cosmovisor/current/bin/0gchaind /usr/local/bin/0gchaind -f
```
```shell
sudo systemctl daemon-reload
sudo systemctl enable 0gchaind.service
```

## 🟢 Node Ayarları

```shell
0gchaind config chain-id zgtendermint_16600-2
0gchaind config keyring-backend os
0gchaind config node tcp://localhost:26657
```

```shell
0gchaind init NODE-ISMINI-YAZ --chain-id zgtendermint_16600-2
```

## 🟢 Genesis dosyası 

```shell
rm ~/.0gchain/config/genesis.json
wget -P ~/.0gchain/config https://github.com/0glabs/0g-chain/releases/download/v0.2.3/genesis.json

```

```shell
0gchaind validate-genesis
```

## 🟢 PEER VE SEED 

```shell
PEERS="cd529839591e13f5ed69e9a029c5d7d96de170fe@46.4.55.46:34656,28070a5cf6464c4f1a7716acdace3e7e57f39fd6@75.119.157.128:26646,baeceedd1ec1ba6ce1b6d19bb40f7b571026fb05@75.119.136.242:26646,b2ea93761696d4881e87f032a7f6158c6c25d92c@45.14.194.241:26646,d589ec553a75287d87635a8403f140f53b2f8432@85.239.232.29:13456,bf8f850598d3d52ee176296f07c10212e0d334ca@testnet-v2-0g-rpc.emberstake.xyz:34140,6122859577a3465ba67065f3b63194cae67ef4c4@110.171.123.186:36656" && \
sed -i -e "s/^seeds *=.*/seeds = \"$SEEDS\"/; s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.0gchain/config/config.toml
```

## 🟢 Prune

```shell

sed -i -e "s/^pruning *=.*/pruning = \"custom\"/" $HOME/.0gchain/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = \"100\"/" $HOME/.0gchain/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = \"50\"/" $HOME/.0gchain/config/app.toml

sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0ua0gi"|g' $HOME/.0gchain/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.0gchain/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = \"null\"/" $HOME/.0gchain/config/config.toml
```

## 🟢 Port Ayarları ( eğer başka bir proje çalışıyorsa kullanın )

```shell
echo "export G_PORT="16"" >> $HOME/.bash_profile
source $HOME/.bash_profile
```

```shell
sed -i.bak -e "s%:1317%:${G_PORT}317%g;
s%:8080%:${G_PORT}080%g;
s%:9090%:${G_PORT}090%g;
s%:9091%:${G_PORT}091%g;
s%:8545%:${G_PORT}545%g;
s%:8546%:${G_PORT}546%g;
s%:6065%:${G_PORT}065%g" $HOME/.0gchain/config/app.toml
```

```shell
sed -i.bak -e "s%:26658%:${G_PORT}658%g;
s%:26657%:${G_PORT}657%g;
s%:6060%:${G_PORT}060%g;
s%:26656%:${G_PORT}656%g;
s%^external_address = \"\"%external_address = \"$(wget -qO- eth0.me):${G_PORT}656\"%;
s%:26660%:${G_PORT}660%g" $HOME/.0gchain/config/config.toml
```

```shell
sed -i \
    -e 's/address = "127.0.0.1:8545"/address = "0.0.0.0:8545"/' \
    -e 's|^api = ".*"|api = "eth,txpool,personal,net,debug,web3"|' \
    $HOME/.0gchain/config/app.toml
```

## 🟢 Başlatalım

```shell
sudo systemctl daemon-reload
sudo systemctl restart 0gchaind
```

## 🟢 Log

```shell
sudo journalctl -u 0gchaind.service -f --no-hostname -o cat
```


## 🟢 Cüzdan oluşturma ( Eğer daha önceki testnete katıldıysanız aynı cüzdanı recover edin. İlk defa kuruyorsanız recover olan kodu kullanmayın.

- recover kodu : Bu kod eski memoricler ile recover yapar.

```shell
0gchaind keys add CÜZDAN-ADI --eth --recover
```

- Yeni cüzdan oluşturma

```shell
0gchaind keys add cuzdan-adini-yaz --eth
```

## 🟢 Evm adresi alma recover ettiyseniz aynısını verecek. Yeni oluşturduysanız onunla alakalı olanı verecek

```shell
echo "0x$(0gchaind debug addr $(0gchaind keys show CÜZDAN-ADINI-YAZ -a) | grep hex | awk '{print $3}')"
```

```shell
0gchaind keys unsafe-export-eth-key cüzdan-adi-yaz
```


## 🟢 senk Kontrol eğer senk olduysa FALSE çıktısı alırsınız daha sonra validatör oluşturun

```shell
0gchaind status | jq
```

![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/1dba9cf6-65f6-44d6-aa97-501136d7a297)


## 🟢 Validatör oluşturun ( Moniker yani görünen isminizi yazın ve cüzdan ismini yazın

```shell
0gchaind tx staking create-validator \
  --amount=1000000ua0gi \
  --pubkey=$(0gchaind tendermint show-validator) \
  --moniker=MONİKER-YAZ \
  --chain-id=zgtendermint_16600-2 \
  --commission-rate="0.10" \
  --commission-max-rate="0.20" \
  --commission-max-change-rate="0.01" \
  --min-self-delegation=1 \
  --from=CUZDAN-ADI-YAZ \
  --identity="" \
  --website="https://herculesnode.com" \
  --details="HerculesNode community" \
  --gas=auto \
  --gas-adjustment=1.4 \
  --node=http://localhost:16657 \
  -y
```

## 🟢 Faucet

- Buradan faucet token alın. EVM adresi ile alacaksınız
- https://faucet.0g.ai/

## 🟢 Delege işlemi

```shell
0gchaind tx staking delegate $(0gchaind keys show cüzdanadınıyaz --bech val -a) 1000000ua0gi --from cüzdanadınızyaz -y
```

## 🟢 Unjail işlemi

```shell
0gchaind tx slashing unjail --from CÜZDAN-ADINIZ --from herculwallet --gas=500000 --gas-prices=99999ua0gi --node=http://localhost:16657 -y
```

## 🟢 Aktif listeye bakma

```shell
0gchaind q staking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' \
| jq -r '.tokens + " - " + .description.moniker' \
| sort -gr | nl
```

## 🟢 inAktif listeye bakma

```shell
0gchaind q staking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' \
| jq -r '.tokens + " - " + .description.moniker' \
| sort -gr | nl
```

## 🟢 Bakiyeye bakma

```shell
0gchaind q bank balances $(0gchaind keys show CUZDAN-ADINIZ -a)
```

## 🟢 VAlidatör bilgilerine bakma duruma bakma

```shell
0gchaind q staking validator $(0gchaind keys show CUZDAN-ADINIZ --bech val -a)
```


## 🟢 Nodu silme

```shell
sudo systemctl stop 0gchaind.service
sudo systemctl disable 0gchaind.service
sudo rm /etc/systemd/system/0gchaind.service
rm -rf $HOME/.0gchain $HOME/0g-chain
```
