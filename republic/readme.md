
### Republic Validatör Node kurulum rehberi

<img width="703" height="234" alt="image" src="https://github.com/user-attachments/assets/be898df7-7a36-4c95-ae17-0df293ad3d92" />


## 🟢 Puan sistemi
https://points.republicai.io/?ref=ED6928

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Republic Discord](https://discord.gg/AwKbbrdfcm)
 * [HerculesNode Explorer](https://explorer.herculesnode.com/0G-Testnet/staking)




## 🟢 Sistemi güncelleyelim
```shell
sudo apt update -y && sudo apt upgrade -y && sudo apt install jq -y
```

## 🟢 Go kuralım
```shell
cd $HOME
wget https://go.dev/dl/go1.22.3.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.22.3.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin' >> $HOME/.bash_profile
source $HOME/.bash_profile
```

## 🟢Cosmovisor
```shell
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@latest
```

## 🟢Ön ayar Değişken tanımlama
```shell
echo "export REPUBLIC_WALLET='wallet'" >> $HOME/.bash_profile
echo "export REPUBLIC_PORT='43'" >> $HOME/.bash_profile
source $HOME/.bash_profile
```

## 🟢 Dosyaları indirin
```shell
VERSION="v0.1.0" && mkdir -p $HOME/.republic/cosmovisor/genesis/bin && curl -L "https://media.githubusercontent.com/media/RepublicAI/networks/main/testnet/releases/${VERSION}/republicd-linux-amd64" -o republicd && chmod +x republicd && mv republicd $HOME/.republic/cosmovisor/genesis/bin/ && ln -sfn $HOME/.republic/cosmovisor/genesis $HOME/.republic/cosmovisor/current && sudo cp $HOME/.republic/cosmovisor/genesis/bin/republicd /usr/local/bin/
```

## 🟢 init işlemini yapalım ( Nodeisminiz yazan yere kendi node isminizi yazın yoksa nodeismi olarak kalır :)
```shell
republicd init Nodeİsminiz --chain-id raitestnet_77701-1 --home $HOME/.republic
```

```shell
curl -s https://raw.githubusercontent.com/RepublicAI/networks/main/testnet/genesis.json > $HOME/.republic/config/genesis.json
```


## 🟢 Genesis
```shell
sed -i.bak -e "s%:26658%:${REPUBLIC_PORT}658%g;
s%:26657%:${REPUBLIC_PORT}657%g;
s%:6060%:${REPUBLIC_PORT}060%g;
s%:26656%:${REPUBLIC_PORT}656%g;
s%^external_address = \"\"%external_address = \"$(wget -qO- eth0.me):${REPUBLIC_PORT}656\"%;
s%:26660%:${REPUBLIC_PORT}660%g" $HOME/.republic/config/config.toml
```

```shell
sed -i.bak -e "s%:1317%:${REPUBLIC_PORT}317%g;
s%:8080%:${REPUBLIC_PORT}080%g;
s%:9090%:${REPUBLIC_PORT}090%g;
s%:9091%:${REPUBLIC_PORT}091%g;
s%:8545%:${REPUBLIC_PORT}545%g;
s%:8546%:${REPUBLIC_PORT}546%g;
s%:6065%:${REPUBLIC_PORT}065%g" $HOME/.republic/config/app.toml
```

## 🟢 Peers
```shell
SEEDS=""
PEERS="8567f9acbb313978a16b1626fe0e997bbcd97990@162.243.109.138:26656,a02d1c8e9f481f30127ce0ef89c9e490f61a4e2e@38.49.214.70:26656,7e483c0ab1cbf60a1056263903dc3a3269244141@38.49.214.94:26656,38fa0132bd791dddf5a4db7c440af494af9ee3b2@34.61.170.254:26656,67ecda5dfaf5aa5519afdac580c832f0118a730f@62.171.142.162:26656,90cabe6f1bd8bd4eafec781f224cfac725ae5391@152.53.230.81:47656,cdae43b6f4ee3d3824648ae2bcb8ee21e689396e@89.167.25.39:43656,ab6065d07a85c9c6f10d8084a27baaecbb6cd529@65.108.231.223:43656,398279493cf9c41108b867cddfcd786b275e153c@185.100.54.13:26656,1fc361b76cb5d3190027e18299a22e3dcb689dd9@172.31.30.32:26656,5d28825836938c8ad6012eb9f0f2215421a77e31@173.212.224.154:26656,f751d819c6c50a9a4232e89e76d69a111ded570e@89.167.44.231:26656,02c54e90a23d7e7a7f2eb1197f3b57602e0c1244@198.7.125.48:26656,4e14a1edc972ed3f4c03eae8434cb3997b342029@46.224.213.11:43656,938b2dffbd2fc169806f9ab3d01b473281c7fc82@157.180.52.245:48656,561fd4716968ee71992adeca4c29cee338327009@89.34.219.104:26656,cbae02c6cc882a222ccd7939d4d93c4b3f7077a9@65.108.14.235:36656,a6c1cc71dae002bce81a42b2d2a154fbe1046c54@89.167.13.7:43656,4b02d8dc14065e21cefd7a93e7efeee09508e292@109.123.252.55:26656,3cc74ebe26e070dc898b1e074161ffafa827081b@152.53.230.108:17656,d3b15134e289878fb6b8e8f54b69a8be9060a418@37.27.109.41:26656,282a75919f493c98f705a25e17165c80c177598a@217.216.111.83:26656,543c7e614249cc7038850adb3f9af75b31690179@152.53.53.5:43656,bb8dd41fc4731fd1b99bb054103c5c9526433bdc@149.5.246.217:43656,09f1d1e1c69200f3c77e7266323775af56f9172c@77.42.89.219:43656,f41590c5fd116dc2e52fafb341e9a9b415566534@87.255.8.15:26656"

sed -i -e "s/^seeds *=.*/seeds = \"$SEEDS\"/; s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.republic/config/config.toml
```

## 🟢 Pruning - indexer - Gas işlemleri
```shell
sed -i -e "s/^pruning *=.*/pruning = \"custom\"/" $HOME/.republic/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = \"100\"/" $HOME/.republic/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = \"10\"/" $HOME/.republic/config/app.toml
```

```shell
sed -i -e "s/^indexer *=.*/indexer = \"null\"/" $HOME/.republic/config/config.toml
```

```shell
sed -i 's|minimum-gas-prices =.*|minimum-gas-prices = "250000000arai"|g' $HOME/.republic/config/app.toml
```

## 🟢 Servis oluşturun

```shell
sudo tee /etc/systemd/system/republicd.service > /dev/null <<EOF
[Unit]
Description=Republic AI Node
After=network-online.target

[Service]
User=$USER
Environment="DAEMON_NAME=republicd"
Environment="DAEMON_HOME=$HOME/.republic"
Environment="DAEMON_ALLOW_DOWNLOAD_BINARIES=true"
Environment="DAEMON_RESTART_AFTER_UPGRADE=true"
ExecStart=$HOME/go/bin/cosmovisor run start --home $HOME/.republic --chain-id raitestnet_77701-1
Restart=always
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
```



## 🟢 Başlatalım

```shell
sudo systemctl daemon-reload
sudo systemctl enable republicd
sudo systemctl start republicd
```

## 🟢 Loglara bakalım

```shell
journalctl -u republicd -f

```

```shell
republicd status --node tcp://localhost:${REPUBLIC_PORT}657
```

## 🟢 Güncelleme v0.2.1 ( tek tek girin kodları )
```shell
sudo systemctl stop republicd

wget https://github.com/RepublicAI/networks/releases/download/v0.2.1/republicd-linux-amd64 -O republicd

chmod +x republicd

sudo mv republicd /usr/local/bin/

sudo systemctl start republicd

journalctl -u republicd -f
```

## 🟢 Cüzdan oluşturalım ( size bir key verecek bunu saklayın daha sonra cüzdan adresinize faucet üzerinden token alın )

```shell
republicd keys add $REPUBLIC_WALLET
```


## 🟢 Validatör oluşturun ( Aşağıdaki komutu girdikten sonra validator.json dosyasını açın ve bilgilerinizi girin ! Önemli  

aşağıdaki komut 1 rai test token ile işlem yapar bu örneğe göre elinizde ne varsa ona göre değiştirebilirsiniz. 

20000000000000000000arai : 10 Adet Token 
10000000000000000000arai : 10 Adet Token 
1000000000000000000arai : 1 Adet Token

```shell
PUBKEY=$(jq -r '.pub_key.value' $HOME/.republic/config/priv_validator_key.json)

cat > validator.json << EOF
{
  "pubkey": {"@type":"/cosmos.crypto.ed25519.PubKey","key":"$PUBKEY"},
  "amount": "1000000000000000000arai",
  "moniker": "VALİDATÖR İSMİNİZİ YAZIN",
  "identity": "KEYBASENİZİ YAZIN YOKSA BOŞ BIRAKIN",
  "website": "https://herculesnode.com",
  "security": "MAİL ADRESİNİZİ YAZIN",
  "details": "HerculesNode community",
  "commission-rate": "0.05",
  "commission-max-rate": "0.15",
  "commission-max-change-rate": "0.02",
  "min-self-delegation": "1"
}
EOF
```

## 🟢 Validator.json sonrası bu komutu girin ve validatörünüzü oluşturun. Faucet üzerinden cüzdanınıza token almadan işlemi yapamazsınız !!

```shell
republicd tx staking create-validator validator.json \
--from $REPUBLIC_WALLET \
--chain-id raitestnet_77701-1 \
--gas auto \
--gas-adjustment 1.5 \
--gas-prices "1000000000arai" \
--node tcp://localhost:${REPUBLIC_PORT}657 \
-y
```

## 🟢 Delege işlemi

```shell
republicd tx staking delegate VALİDATÖR-ADRESİNİZİ-YAZIN \
10000000000000000000arai \
--from $REPUBLIC_WALLET \
--chain-id raitestnet_77701-1 \
--gas auto \
--gas-adjustment 1.5 \
--gas-prices 1000000000arai \
--node tcp://localhost:${REPUBLIC_PORT}657 \
-y
```

## 🟢 Unjail işlemi

```shell
republicd tx slashing unjail \
--from $REPUBLIC_WALLET \
--chain-id raitestnet_77701-1 \
--gas auto \
--gas-adjustment 1.5 \
--gas-prices 1000000000arai \
--node tcp://localhost:${REPUBLIC_PORT}657 \
-y
```

## 🟢 ödül çek

```shell
republicd tx distribution withdraw-rewards VALLOPER-ADRESS \
--from $REPUBLIC_WALLET \
--commission \
--chain-id raitestnet_77701-1 \
--gas auto \
--gas-adjustment 1.5 \
--gas-prices "1000000000arai" \
--node tcp://localhost:${REPUBLIC_PORT}657 \
-y
```

## 🟢 Güncel peer ekleme

```shell
URL="https://rpc.republicai.io/net_info" && \
PEERS=$(curl -s $URL | jq -r '.result.peers[] 
  | select(.remote_ip | test("^[0-9]{1,3}(\\.[0-9]{1,3}){3}$")) 
  | "\(.node_info.id)@\(.remote_ip):" + (.node_info.listen_addr | capture(":(?<port>[0-9]+)$").port)' \
  | paste -sd "," -) && \
sed -i "s|^persistent_peers *=.*|persistent_peers = \"$PEERS\"|" $HOME/.republicd/config/config.toml && \
sudo systemctl daemon-reload && \
sudo systemctl restart republicd

```

## 🟢 VAlidatör bilgilerine bakma duruma bakma

```shell
republicd q staking validator $(republicd keys show $REPUBLIC_WALLET --bech val -a)
```

## 🟢 RPC üzerinden peer sayısı +10 üzeri olması iyi

```shell
curl -s http://127.0.0.1:${REPUBLIC_PORT}657/net_info | jq '.result.n_peers'
```

## 🟢 Peer Listesi

```shell
curl -s http://127.0.0.1:{REPUBLIC_PORT}/net_info | jq '.result.peers[] | {id: .node_info.id, ip: .remote_ip, port: .node_info.listen_addr}'
```


## 🟢 Bakiyeye bakma

```shell
republicd q bank balances $(republicd keys show $REPUBLIC_WALLET -a)
```
<img width="696" height="109" alt="image" src="https://github.com/user-attachments/assets/67c41d46-8934-41a7-82df-44c4272ac65c" />


## 🟢 Nodu silme

```shell
sudo systemctl stop republicd.service
sudo systemctl disable republicd.service
sudo rm /etc/systemd/system/republicd.service
rm -rf $HOME/.republic
```









