![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/9f3bd440-d371-47b5-afcd-f0d0f4e342d1)



### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [OG Discord](https://discord.gg/0glabs)
 * [ScannerX Explorer](https://explorer.herculesnode.com/0G-Testnet/staking)


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

## 🟢 Dosyaları indirin
```shell
git clone -b v0.1.0 https://github.com/0glabs/0g-chain.git
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
0gchaind config chain-id zgtendermint_16600-1
0gchaind config keyring-backend os
0gchaind config node tcp://localhost:16657
```

```shell
0gchaind init NODE-ISMINI-YAZ --chain-id zgtendermint_16600-1
```

## 🟢 Genesis

```shell
rm ~/.0gchain/config/genesis.json
curl -Ls https://github.com/0glabs/0g-chain/releases/download/v0.1.0/genesis.json > $HOME/.0gchain/config/genesis.json
curl -Ls https://raw.githubusercontent.com/Core-Node-Team/Testnet-TR/main/0G-Newton/addrbook.json > $HOME/.0gchain/config/addrbook.json
```

```shell
rm ~/.0gchain/config/genesis.json
wget -P ~/.0gchain/config https://github.com/0glabs/0g-chain/releases/download/v0.1.0/genesis.json
```

## 🟢 diğer Seed

```shell
PEERS="fbc3b6d41cd39a62ef5e3fc596435adfaf428a34@37.120.189.81:16656,645531eb02b275a59cc3b1af99e541852849f695@84.247.139.25:16656,d00273ac6a2470cd4e48008d9af4d2521b134394@62.169.29.136:26656,f5a7d34355f6d89b7ece583131c6b1f79ac5485e@218.102.97.67:25856,a3e6c6214805c1c068882f1981855c7a9f5926ea@213.168.249.202:26656,da1f4985ce3df05fd085460485adefa93592a54c@172.232.33.25:26656,91f079ccd2e0edf42e0fa57183ac92c22c525658@14.245.25.144:14256,9d09d391b2cf706a597d03fe8bb6700fe5cac53d@65.108.198.183:18456,5a202fb905f20f96d8ff0726f0c0756d17cf23d8@43.248.98.100:26656,74775d65b6ab427c685efcaa8190912d3a60e562@123.19.45.21:12656,f2693dd86766b5bf8fd6ab87e2e970d564d20aff@54.193.250.204:26656,9d7564df34efa146a94c073e5bf3f5e11f947b75@155.133.22.230:26656,e179d05dc792d9b902be3baa7a31a07a92afbcf0@118.142.83.5:26656,c4b9c3a7f3651af729d73b150e714ee91e7585c1@14.176.200.133:26656,f64f0fb500c62bffa33d60450d30792ee4b5fbd0@167.86.119.168:26656,d4085fd93ab77576f2acdb25d2d817061db5afe6@62.169.19.156:26656,2b8ee12f4f94ebc337af94dbec07de6f029a24e6@94.16.31.161:26656,0f5022e4265184052a5468379687625a81fd255e@154.12.253.116:26656,3859828e1099214de14dae91d1f7decf2374eeb4@47.236.170.254:26656,23b0a0624699f85062ddebf910583f70a5b9e86b@14.167.152.116:14256,b8f8ed478f2794629fdb5cf0c01edaed80f00f84@168.119.64.172:26656,5d81d59e81356a33e6ccccaa3d419ff73244697e@107.173.18.103:26656,c4d619f6088cb0b24b4ab43a0510bf9251ab5d7f@54.241.167.190:26656,a83f5d07a8a64827851c9f1d0c21c900b9309608@188.166.181.110:26656,19943cbe46cdb9eb37cb06c0067ce63154eee6ea@213.199.52.155:26656,a6ff8a651dd0a0e66dbfb2174ccadcbbcf567b29@66.94.122.224:26656,f3c912cf5653e51ee94aaad0589a3d176d31a19d@157.90.0.102:31656,141dbd90d5c3411c9ba72ba03704ccdb70875b01@65.109.147.58:36656,cd529839591e13f5ed69e9a029c5d7d96de170fe@46.4.55.46:34656,a8d7c5a051c4649ba7e267c94e48a7c64a00f0eb@65.108.127.146:26656" && \
SEEDS="c4d619f6088cb0b24b4ab43a0510bf9251ab5d7f@54.241.167.190:26656,44d11d4ba92a01b520923f51632d2450984d5886@54.176.175.48:26656,f2693dd86766b5bf8fd6ab87e2e970d564d20aff@54.193.250.204:26656,f878d40c538c8c23653a5b70f615f8dccec6fb9f@54.215.187.94:26656" && \
sed -i -e "s/^seeds *=.*/seeds = \"$SEEDS\"/; s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.0gchain/config/config.toml
```

```shell

sed -i -e "s/^pruning *=.*/pruning = \"custom\"/" $HOME/.0gchain/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = \"100\"/" $HOME/.0gchain/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = \"50\"/" $HOME/.0gchain/config/app.toml

sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "0ua0gi"|g' $HOME/.0gchain/config/app.toml
sed -i -e "s/prometheus = false/prometheus = true/" $HOME/.0gchain/config/config.toml
sed -i -e "s/^indexer *=.*/indexer = \"null\"/" $HOME/.0gchain/config/config.toml
```

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

## 🟢 başlatın

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
  --chain-id=zgtendermint_16600-1 \
  --commission-rate=0.05 \
  --commission-max-rate=0.10 \
  --commission-max-change-rate=0.01 \
  --min-self-delegation=1 \
  --from=CUZDAN-ADI-YAZ \
  --identity="" \
  --website="https://explorer.scannerx.net" \
  --details="HerculesNode community" \
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
