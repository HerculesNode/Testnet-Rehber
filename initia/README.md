### Herculesnode Scannerx Initia Guide v0.2.15

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [faucet](https://faucet.testnet.initia.xyz/)
 * [ScannerX Explorer](https://explorer.scannerx.net/Initia/staking)
 * [görevler](https://initia-xyz.notion.site/The-Initiation-Validator-Tasks-6d88ab0034644473907435662f9285b3)
 * [Form](https://docs.google.com/forms/d/e/1FAIpQLSc09Kl6mXyZHOL12n_6IUA8MCcL6OqzTqsoZn9N8gpptoeU_Q/viewform)

## 🟢 Sistem özellikleri
| Ram | cpu     | disk                      |
| :-------- | :------- | :-------------------------------- |
| `4GB`      | `8Core` | `500+ SSD` |


| Services | 
| :-------- | 
| RPC : https://initia-testnet-rpc.herculesrollap.store:443     | 
| API : https://initia-testnet-api.herculesrollap.store:443     | 



## 🟢 Sistemi güncelleyelim
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y
```

## 🟢 Go kuralım
```shell
cd $HOME && \
ver="1.22.0" && \
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
git clone https://github.com/initia-labs/initia
cd initia
git checkout v0.2.15
make build
initiad version
```
![image](https://github.com/HerculesNode/initia/assets/101635385/ab01aca6-18f3-49f1-8365-40fb408c1b83)


```shell
mkdir -p $HOME/.initia/cosmovisor/genesis/bin
mv /root/initia/build/initiad $HOME/.initia/cosmovisor/genesis/bin/
```

## 🟢 System
```shell
sudo ln -s $HOME/.initia/cosmovisor/genesis $HOME/.initia/cosmovisor/current -f
sudo ln -s $HOME/.initia/cosmovisor/current/bin/initiad /usr/local/bin/initiad -f
```

```shell
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.5.0
```

## 🟢 Servis oluşturun

```shell
sudo tee /etc/systemd/system/initiad.service > /dev/null << EOF
[Unit]
Description=initia node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=$HOME/.initia"
Environment="DAEMON_NAME=initiad"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.initia/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
```

```shell
sudo systemctl daemon-reload
sudo systemctl enable initiad.service
```

## 🟢 Node Ayarları

```shell
initiad config set client chain-id initiation-1
initiad config set client node tcp://localhost:15657
initiad config set client keyring-backend test
```

- Node adınızı yazın
```shell
initiad init NODE-ADI-YAZ --chain-id initiation-1
```

## 🟢 Genesis

```shell
rm ~/.initia/config/genesis.json
curl -Ls https://raw.githubusercontent.com/molla202/pokemon/main/genesis.json > $HOME/.initia/config/genesis.json
curl -Ls https://raw.githubusercontent.com/Core-Node-Team/Testnet-TR/main/Initia/addrbook.json > $HOME/.initia/config/addrbook.json
```

## 🟢 Port

```shell
echo "export N_PORT="15"" >> $HOME/.bash_profile
source $HOME/.bash_profile
```

```shell
sed -i.bak -e "s%:1317%:${N_PORT}317%g;
s%:8080%:${N_PORT}080%g;
s%:9090%:${N_PORT}090%g;
s%:9091%:${N_PORT}091%g;
s%:8545%:${N_PORT}545%g;
s%:8546%:${N_PORT}546%g;
s%:6065%:${N_PORT}065%g" $HOME/.initia/config/app.toml
```

```shell
sed -i.bak -e "s%:26658%:${N_PORT}658%g;
s%:26657%:${N_PORT}657%g;
s%:6060%:${N_PORT}060%g;
s%:26656%:${N_PORT}656%g;
s%^external_address = \"\"%external_address = \"$(wget -qO- eth0.me):${N_PORT}656\"%;
s%:26660%:${N_PORT}660%g" $HOME/.initia/config/config.toml
```

## 🟢 Seed

```shell
PEERS="a3660a8b7a0d88b12506787b26952930f1774fc2@65.21.69.53:48656,e3ac92ce5b790c76ce07c5fa3b257d83a517f2f6@178.18.251.146:30656,2692225700832eb9b46c7b3fc6e4dea2ec044a78@34.126.156.141:26656,2a574706e4a1eba0e5e46733c232849778faf93b@84.247.137.184:53456,40d3f977d97d3c02bd5835070cc139f289e774da@168.119.10.134:26313,1f6633bc18eb06b6c0cab97d72c585a6d7a207bc@65.109.59.22:25756,4a988797d8d8473888640b76d7d238b86ce84a2c@23.158.24.168:26656,e3679e68616b2cd66908c460d0371ac3ed7795aa@176.34.17.102:26656,d2a8a00cd5c4431deb899bc39a057b8d8695be9e@138.201.37.195:53456,329227cf8632240914511faa9b43050a34aa863e@43.131.13.84:26656,517c8e70f2a20b8a3179a30fe6eb3ad80c407c07@37.60.231.212:26656,07632ab562028c3394ee8e78823069bfc8de7b4c@37.27.52.25:19656,028999a1696b45863ff84df12ebf2aebc5d40c2d@37.27.48.77:26656,3c44f7dbb473fee6d6e5471f22fa8d8095bd3969@185.219.142.137:53456,8db320e665dbe123af20c4a5c667a17dc146f4d0@51.75.144.149:26656,c424044f3249e73c050a7b45eb6561b52d0db456@158.220.124.183:53456,767fdcfdb0998209834b929c59a2b57d474cc496@207.148.114.112:26656,edcc2c7098c42ee348e50ac2242ff897f51405e9@65.109.34.205:36656,140c332230ac19f118e5882deaf00906a1dba467@185.219.142.119:53456,4eb031b59bd0210481390eefc656c916d47e7872@37.60.248.151:53456,ff9dbc6bb53227ef94dc75ab1ddcaeb2404e1b0b@178.170.47.171:26656,ffb9874da3e0ead65ad62ac2b569122f085c0774@149.28.134.228:26656" && \
SEEDS="2eaa272622d1ba6796100ab39f58c75d458b9dbc@34.142.181.82:26656,c28827cb96c14c905b127b92065a3fb4cd77d7f6@testnet-seeds.whispernode.com:25756" && \
sed -i -e "s/^seeds *=.*/seeds = \"$SEEDS\"/; s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.initia/config/config.toml
```

## 🟢 Gas pruning

```shell
sed -i -e "s|^minimum-gas-prices *=.*|minimum-gas-prices = \"0.15uinit,0.01uusdc\"|" $HOME/.initia/config/app.toml
```
```shell
sed -i -e "s/^pruning *=.*/pruning = \"custom\"/" $HOME/.initia/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = \"100\"/" $HOME/.initia/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = \"50\"/" $HOME/.initia/config/app.toml
```

## 🟢 Snap 390K

```shell
sudo systemctl stop initiad
```
```shell
wget http://snapshots.staking4all.org/testnet-snapshots/initia/latest/initia.tar.lz4 -O latest_snapshot.tar.lz4
```

```shell
cp $HOME/.initia/data/priv_validator_state.json $HOME/.initia/priv_validator_state.json.backup
```

```shell
initiad tendermint unsafe-reset-all --home $HOME/.initia --keep-addr-book
```

- Uzun sürer bekleyin bitmeden birşey yapmayın

```shell
lz4 -d -c ./latest_snapshot.tar.lz4 | tar -xf - -C $HOME/.initia
```

```shell
mv $HOME/.initia/priv_validator_state.json.backup $HOME/.initia/data/priv_validator_state.json
```
```shell
sudo systemctl restart initiad && sudo journalctl -u initiad -f -o cat
```


## 🟢 peer 1

```shell
PEERS="a79fb8776078dc03fdb8a22d55e68d33cd278b20@109.123.253.61:26656,f91806acfdde672985f30af68414e25b4c223ed7@62.169.26.88:26656,ba7bef1694eb050177f70f55dee90104532366db@161.97.96.72:14656,7ddb2d3848d8911d1405d2b6dda5f79e6d1bc7d6@38.242.206.219:26656,bb6b5982fcf2715461b8c3702bc1259b66f340cb@65.108.96.173:26656,ef6d348e85e3dc4a5dbab92fbc91242a3ff5b22a@95.216.66.89:26656,d348f8661e5f3d00c2b54c0dab6a3733a1faaad3@109.123.244.119:14656,060f8c89fe208e12555171b40dcaabfd382264af@95.111.240.155:15656,9797536c7b2511471135ecbccdb9243ef4ecdf64@43.134.109.184:26656,e924262b980f7d11a4dbc70b373fc7f5fa0b7d47@135.181.128.23:26656,131297aadbc57572b7377f431ad03cfbc7bfbbb5@49.12.59.182:26656,6751db6eae5829013461db8a30fca58846b309e0@84.247.169.170:26656,8053dd69b6978e7c77ed9d89e24ee13fc6244454@194.238.31.99:27656,504d4bdf202a989094f9e4ceecad65c0c677205d@49.13.136.252:26656,4e28a7763a364d25de96fa11360fe3c7aa06b065@43.155.147.147:26656" && sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.initia/config/config.toml && sudo systemctl restart initiad && sudo journalctl -u initiad -f -o cat
```

## 🟢 peer 2

```shell
PEERS="17b0fb616bae3fc2e6babf717e2ec132353142db@51.195.88.136:15674,0f80116882d7732d52abaf3e6c007f3218665635@185.16.39.138:53456,7f7fcc6e7ce3287ea6bd7a7c6cb8119c97d4697d@49.13.25.33:26656,3b944bcae9db0b88d8419adde8e26188a6a5ef5d@65.109.59.22:25756,c7148b9dd296ff12723ba6301c91f8376e5490bf@162.55.47.206:27656,fbba8098f52c272c3319061826bced9143b6efc3@181.214.231.175:26656,bbaa823545488a7e8785d891b2f5f49d648bb6f5@181.214.231.170:26656,793a86268d83e78f596fbb918d6d82d6bcb8e3f6@181.214.231.173:26656,a12dc32421d3aabafd52239d774c27af6fda494d@88.99.164.202:26656,aaa63e5685e1e3362e2fb271adea05ea74a965c0@179.61.251.10:26656,6e05d67b0b0b8f36dd8075abe8161331bab98fa1@65.109.32.125:26656,8c63f08b951f7680a443caa1144b720d2a666261@65.108.232.174:17956,917d28e3c7234763788aaa9656a683d5ffac2f3b@179.61.251.153:26656,e043d748f85f4b001f19002fe87ca5021a79018a@181.214.99.209:26656,4f76c615791a4efd8ae7bd4b243606bb7536d38e@181.214.231.152:26656,cbb8e26a938d8e9faeb440c36fff0a0c31d958fe@181.214.99.207:26656,0ecdbae53da02eec6f7a8097022218821b724347@138.201.129.214:53456,653f72af8782180e4cca5c4caa0bb92282a8a754@37.27.124.171:27656,49735e6f020a9efcc181e90a95f78861f6d1cdf9@95.216.172.13:27656,6a6d164766341e4e4f56d0359f130a757f21851a@95.217.148.179:29656,44ed0669a0195b2dd5b4ab157ebf030d70f3ee97@5.78.119.115:27656,33455905a397b214b22598900eafe7540b26d49c@142.132.200.200:26656,cd69bcb00a6ecc1ba2b4a3465de4d4dd3e0a3db1@65.108.231.124:51656,a79bcd799755f327504d04fb5decf97068c0a3f9@144.76.30.36:15674,a98e47c02763d05f2a9623cb67e8e40e0d06504a@5.9.70.180:15674,548e26b95b895efc964b08a6b2e991c6d5a6791d@142.132.151.35:15674,71e6186d3b11ed1f110298da39577b46acdea810@213.199.40.95:27656,483508be6e5854f2682ffee6b06565aaf910884a@94.130.133.189:33756,4426384d44d2ad79037eab349ed92f8c40503cb8@149.50.108.14:27656" && sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.initia/config/config.toml && sudo systemctl restart initiad && sudo journalctl -u initiad -f -o cat
```

## 🟢 peer 3 Toplu

```shell
PEERS="a79fb8776078dc03fdb8a22d55e68d33cd278b20@109.123.253.61:26656,f91806acfdde672985f30af68414e25b4c223ed7@62.169.26.88:26656,ba7bef1694eb050177f70f55dee90104532366db@161.97.96.72:14656,7ddb2d3848d8911d1405d2b6dda5f79e6d1bc7d6@38.242.206.219:26656,bb6b5982fcf2715461b8c3702bc1259b66f340cb@65.108.96.173:26656,ef6d348e85e3dc4a5dbab92fbc91242a3ff5b22a@95.216.66.89:26656,d348f8661e5f3d00c2b54c0dab6a3733a1faaad3@109.123.244.119:14656,060f8c89fe208e12555171b40dcaabfd382264af@95.111.240.155:15656,9797536c7b2511471135ecbccdb9243ef4ecdf64@43.134.109.184:26656,e924262b980f7d11a4dbc70b373fc7f5fa0b7d47@135.181.128.23:26656,131297aadbc57572b7377f431ad03cfbc7bfbbb5@49.12.59.182:26656,6751db6eae5829013461db8a30fca58846b309e0@84.247.169.170:26656,8053dd69b6978e7c77ed9d89e24ee13fc6244454@194.238.31.99:27656,504d4bdf202a989094f9e4ceecad65c0c677205d@49.13.136.252:26656,4e28a7763a364d25de96fa11360fe3c7aa06b065@43.155.147.147:26656,e424d9f0663c1330751af292d7ba771d3726bdb0@5.161.244.60:39656,c7a84a526dc4c62ad9c32cbbc6761b568e6a774d@148.113.9.92:25656,4d2088e6228e5c1c67913ebbcdb496258828da9d@195.26.254.116:26656,148c0845575c874e677978112b1c8059090ed4ab@162.55.239.166:29656,6d3e665b42db96ae18b660efed0289e189d13695@109.120.187.4:26656,f01913ad804b63cad146d51ae9f1a483626cfc36@65.21.131.187:22656,66abd758f6971eb8227fc54d11cb56ca1ca280e6@65.109.113.251:13656,7aa28abc3575d3a52b0f71d72713dff30c38b1da@213.133.111.189:26656,c949d1ff552e08f3ed9a8d84fca9b80fa9fcbf77@138.201.20.145:26656,17b0fb616bae3fc2e6babf717e2ec132353142db@51.195.88.136:15674,6a6d164766341e4e4f56d0359f130a757f21851a@95.217.148.179:29656,252514328ff37287a7e5cf8df8d1132a3934570f@65.108.126.173:26656,6a39f5bc5ec178e9c3f1370dee29a4ced7f805f4@84.247.132.187:26656,19df07f12ae496964dc87431eac891bee58513f0@116.202.42.156:39999,497cedc0536e98dda0cbbbac6da64350af437100@54.37.196.157:26656,0aae3374c5d92bd6b5314c8b1e79634702b09c62@88.99.67.49:26656,cd69bcb00a6ecc1ba2b4a3465de4d4dd3e0a3db1@65.108.231.124:51656,41f3a803a2fd02cd38a2b41cb2349fbc72c49621@84.46.253.6:26656,688fbe8580c2945afe7e71b50bb3d323643cc41e@149.50.109.147:14656,25c298e8b74756c6f9e9f01fe8be14f14a307922@65.108.121.227:13756,17b0fb616bae3fc2e6babf717e2ec132353142db@51.195.88.136:15674,0f80116882d7732d52abaf3e6c007f3218665635@185.16.39.138:53456,7f7fcc6e7ce3287ea6bd7a7c6cb8119c97d4697d@49.13.25.33:26656,3b944bcae9db0b88d8419adde8e26188a6a5ef5d@65.109.59.22:25756,c7148b9dd296ff12723ba6301c91f8376e5490bf@162.55.47.206:27656,fbba8098f52c272c3319061826bced9143b6efc3@181.214.231.175:26656,bbaa823545488a7e8785d891b2f5f49d648bb6f5@181.214.231.170:26656,793a86268d83e78f596fbb918d6d82d6bcb8e3f6@181.214.231.173:26656,a12dc32421d3aabafd52239d774c27af6fda494d@88.99.164.202:26656,aaa63e5685e1e3362e2fb271adea05ea74a965c0@179.61.251.10:26656,6e05d67b0b0b8f36dd8075abe8161331bab98fa1@65.109.32.125:26656,8c63f08b951f7680a443caa1144b720d2a666261@65.108.232.174:17956,917d28e3c7234763788aaa9656a683d5ffac2f3b@179.61.251.153:26656,e043d748f85f4b001f19002fe87ca5021a79018a@181.214.99.209:26656,4f76c615791a4efd8ae7bd4b243606bb7536d38e@181.214.231.152:26656,cbb8e26a938d8e9faeb440c36fff0a0c31d958fe@181.214.99.207:26656,0ecdbae53da02eec6f7a8097022218821b724347@138.201.129.214:53456,653f72af8782180e4cca5c4caa0bb92282a8a754@37.27.124.171:27656,49735e6f020a9efcc181e90a95f78861f6d1cdf9@95.216.172.13:27656,6a6d164766341e4e4f56d0359f130a757f21851a@95.217.148.179:29656,44ed0669a0195b2dd5b4ab157ebf030d70f3ee97@5.78.119.115:27656,33455905a397b214b22598900eafe7540b26d49c@142.132.200.200:26656,cd69bcb00a6ecc1ba2b4a3465de4d4dd3e0a3db1@65.108.231.124:51656,a79bcd799755f327504d04fb5decf97068c0a3f9@144.76.30.36:15674,a98e47c02763d05f2a9623cb67e8e40e0d06504a@5.9.70.180:15674,548e26b95b895efc964b08a6b2e991c6d5a6791d@142.132.151.35:15674,71e6186d3b11ed1f110298da39577b46acdea810@213.199.40.95:27656,483508be6e5854f2682ffee6b06565aaf910884a@94.130.133.189:33756,4426384d44d2ad79037eab349ed92f8c40503cb8@149.50.108.14:27656" && sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.initia/config/config.toml && sudo systemctl restart initiad && sudo journalctl -u initiad -f -o cat
```



## 🟢 Start verelim

```shell
sudo systemctl daemon-reload && \
sudo systemctl enable initiad && \
sudo systemctl restart initiad && \
sudo journalctl -u initiad -f -o cat
```

## 🟢 Cüzdan Bakiyesi sorgulama ( Cüzdan ismini yazın )

```shell
initiad q bank balances $(initiad keys show CÜZDAN-İSMİ -a) 
```

## 🟢 Log

```shell
sudo journalctl -u initiad.service -f --no-hostname -o cat
```

## 🟢 true / false log

```shell
initiad status | jq -r .sync_info
```

## 🟢 Cüzdan oluşturma
- Cüzdan adını yaz

```shell
initiad keys add cuzdan-adini-yaz
```
- recover
  
```shell
initiad keys add wallet --recover
```

## 🟢 Validatör oluştur

```shell
initiad tx mstaking create-validator \
  --amount=5000000uinit \
  --pubkey=$(initiad tendermint show-validator) \
  --moniker=MONIKER-YAZ \
  --chain-id=initiation-1 \
  --commission-rate=0.05 \
  --commission-max-rate=0.10 \
  --commission-max-change-rate=0.01 \
  --from=CUZDAN-ADI-YAZ \
  --identity="" \
  --website="https://twitter.com/HerculesNode" \
  --details="HerculesNode community " \
  --node=http://localhost:15657 \
  --gas-adjustment 1.4 \
  --gas auto \
  --gas-prices 0.15uinit \
  -y
```

## 🟢 Edit Validatör

```shell
initiad tx mstaking edit-validator \
--moniker "isim-yaz" \
--from cüzdan-adi-yaz \
--gas-adjustment 1.4 \
--gas auto \
--gas-prices 0.15uinit \
-y
```

## 🟢 Delege

```shell
initiad tx mstaking delegate $(initiad keys show wallet --bech val -a)  miktar000000uinit --from wallet --gas-adjustment 1.4 --gas auto --gas-prices 0.15uinit --node=http://localhost:15657 -y
```

## 🟢 unjail ( Cüzdan ismi yazın )

```shell
initiad tx slashing unjail --from CÜZDAN-İSMİ --gas=2000000 --fees=300000uinit -y
```

## 🟢 Token gönderin ( 3 yer değişecek )

```shell
initiad tx bank send CÜZDAN-İSMİNİZ GÖNDERECEĞİNİZ-CÜZDAN-ADRESİ GÖNDERECEĞİN-ADETuinit --gas=2000000 --fees=300000uinit -y
```


## 🟢 Aktif Validatör

```shell
initiad q mstaking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' \
| jq -r '.voting_power + " - " + .description.moniker' \
| sort -gr | nl
```

## 🟢 İnactive validator

```shell
initiad q mstaking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' \
| jq -r '.voting_power + " - " + .description.moniker' \
| sort -gr | nl
```


## 🟢 blok kontrol

```shell
local_height=$(initiad status | jq -r .sync_info.latest_block_height); network_height=$(curl -s https://rpc-initia-testnet.trusted-point.com/status | jq -r .result.sync_info.latest_block_height); blocks_left=$((network_height - local_height)); echo "Your node height: $local_height"; echo "Network height: $network_height"; echo "Blocks left: $blocks_left"
```

## 🟢 Nodu silin

```shell
sudo systemctl stop initiad
sudo systemctl disable initiad
sudo rm /etc/systemd/system/initiad.service
rm -rf $HOME/.initia
sudo rm /usr/local/bin/initiad
```



## 🟢 Güncelleme  v 2.15

```shell
systemctl stop initiad
cd $HOME
rm -rf initia
git clone https://github.com/initia-labs/initia.git
cd initia
git checkout v0.2.15
make build
./build/initiad version
```

```shell
mv /root/initia/build/initiad $HOME/.initia/cosmovisor/genesis/bin/
```
```shell
sudo systemctl daemon-reload
sudo systemctl restart initiad
sudo journalctl -u initiad.service -f --no-hostname -o cat
```
