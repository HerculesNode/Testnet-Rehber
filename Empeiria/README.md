![image](https://github.com/user-attachments/assets/9ccbdb2c-0ecb-457f-8ffa-a5e560eba7fe)


### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Web](https://herculesnode.com)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Empeiria Twitter](https://x.com/empe_io)
 * [Explorer](https://explorer.herculesnode.com/Empeiria-Testnet)


# Gereksinimler
- 6 CPU
- 32 GB RAM ( daha az yetiyor )
- 240 GB SSD


# Güncellemeler
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install curl git wget htop tmux build-essential jq make lz4 gcc unzip -y
```

# Go Kurulumu
```shell
cd $HOME
VER="1.22.3"
wget "https://golang.org/dl/go$VER.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go$VER.linux-amd64.tar.gz"
rm "go$VER.linux-amd64.tar.gz"
[ ! -f ~/.bash_profile ] && touch ~/.bash_profile
echo "export PATH=$PATH:/usr/local/go/bin:~/go/bin" >> ~/.bash_profile
source $HOME/.bash_profile
[ ! -d ~/go/bin ] && mkdir -p ~/go/bin
```

# Kurulum
```shell
cd $HOME
mkdir -p $HOME/.empe-chain/cosmovisor/genesis/bin
wget https://github.com/empe-io/empe-chain-releases/raw/master/v0.1.0/emped_linux_amd64.tar.gz
tar -xvf emped_linux_amd64.tar.gz
rm -rf emped_linux_amd64.tar.gz
chmod +x emped
```
```shell
mv emped $HOME/.empe-chain/cosmovisor/genesis/bin/
```
```shell
sudo ln -s $HOME/.empe-chain/cosmovisor/genesis $HOME/.empe-chain/cosmovisor/current -f
sudo ln -s $HOME/.empe-chain/cosmovisor/current/bin/emped /usr/local/bin/emped -f
```
```shell
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@v1.5.0
```

# Servis Oluşturalım
```shell
sudo tee /etc/systemd/system/emped.service > /dev/null << EOF
[Unit]
Description=empe-chain node service
After=network-online.target

[Service]
User=$USER
ExecStart=$(which cosmovisor) run start
Restart=on-failure
RestartSec=10
LimitNOFILE=65535
Environment="DAEMON_HOME=${HOME}/.empe-chain"
Environment="DAEMON_NAME=emped"
Environment="UNSAFE_SKIP_BACKUP=true"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$HOME/.emped/cosmovisor/current/bin"

[Install]
WantedBy=multi-user.target
EOF
```
```shell
sudo systemctl daemon-reload
sudo systemctl enable emped
```

# Ayarlar
```shell
emped init "VALİDATOR-İSMİNİZ" --chain-id empe-testnet-2
```

# Genesis & Addrbook
```shell
wget -O $HOME/.empe-chain/config/genesis.json "https://raw.githubusercontent.com/empe-io/empe-chains/master/testnet-2/genesis.json"
wget -O $HOME/.empe-chain/config/addrbook.json "https://raw.githubusercontent.com/MictoNode/empe-chain/main/addrbook.json"
```
# Gas Settings
```shell
sed -i.bak -e "s/^minimum-gas-prices *=.*/minimum-gas-prices = \"0.0001uempe\"/;" ~/.empe-chain/config/app.toml
```
# Pruning
```shell
sed -i -e "s/^pruning *=.*/pruning = \"custom\"/" $HOME/.empe-chain/config/app.toml
sed -i -e "s/^pruning-keep-recent *=.*/pruning-keep-recent = \"100\"/" $HOME/.empe-chain/config/app.toml
sed -i -e "s/^pruning-interval *=.*/pruning-interval = \"10\"/" $HOME/.empe-chain/config/app.toml
sed -i "s/^indexer *=.*/indexer = \"null\"/" $HOME/.empe-chain/config/config.toml
```
# Snap
```shell
ARCHIVE=empe-chain-1_2024-07-28.tar
```
```shell
curl -O https://archive-testnet.empe.io/$ARCHIVE
tar -xvf $ARCHIVE -C ~/.empe-chain/data
rm $ARCHIVE
```
# Port Ayarları
You can replace 77 with anything you want.
```shell
echo "export CUSTOM_PORT="77"" >> $HOME/.bash_profile
source $HOME/.bash_profile
```
```shell
sed -i.bak -e "s%:1317%:${CUSTOM_PORT}17%g;
s%:8080%:${CUSTOM_PORT}80%g;
s%:9090%:${CUSTOM_PORT}90%g;
s%:9091%:${CUSTOM_PORT}91%g;
s%:8545%:${CUSTOM_PORT}45%g;
s%:8546%:${CUSTOM_PORT}46%g;
s%:6065%:${CUSTOM_PORT}65%g" $HOME/.empe-chain/config/app.toml
```
```shell
sed -i.bak -e "s%:26658%:${CUSTOM_PORT}58%g;
s%:26657%:${CUSTOM_PORT}57%g;
s%:6060%:${CUSTOM_PORT}60%g;
s%:26656%:${CUSTOM_PORT}56%g;
s%^external_address = \"\"%external_address = \"$(wget -qO- eth0.me):${CUSTOM_PORT}56\"%;
s%:26660%:${CUSTOM_PORT}60%g" $HOME/.empe-chain/config/config.toml
```

# Peers and Seeds
```shell
SEEDS=""
PEERS="edfc10bbf28b5052658b3b8b901d7d0fc25812a0@193.70.45.145:26656,4bd60dee1cb81cb544f545589b8dd286a7b3fd65@149.202.73.140:26656,149383fab60d8845c408dce7bb93c05aa1fd115e@54.37.80.141:26656,83f9769416445c3c0b0b3a9f79c2b4e19b45441b@94.16.115.147:43656,99ff20ec0c3623d2d725924b8fd0f1c4e1b22e15@195.201.59.173:26656,eed34161ff47076ad1ff83e68942bdd667106536@159.69.179.43:43656,4ff7d588d4c5d59a7208d4c0457cc3c26e6713cd@78.46.19.116:29056,a753ff99004f7860b546fd4b101f9e03e9ab0295@95.216.40.250:26656,692099b20acde5520084ecea12ddd9a36d4ca54d@178.18.251.146:12656,098f3c412e5a32948c526f8b9b7066d3f9f3786a@194.233.69.9:26656,829207ca2cf7debb16787a79c9fc1aa94e9b55ea@116.203.238.65:43656,5406f64d38f433cca31c2f6e96d5619fa92be5b5@168.119.179.250:26656,a9cf0ffdef421d1f4f4a3e1573800f4ee6529773@136.243.13.36:29056,0c0a348442fa5881ce15aba1030214cc7fad23ba@37.27.193.4:43656,94529b5e044f208d1869980f456a53fcef8fb321@14.167.155.13:43656,2354e634c9e8f630e2f93c6d3a7b845c681d00bb@167.235.102.45:11756,d8dedcd1b8c541141e9c57a23db35bea44a05129@37.27.129.24:23656,37f0a23a5eafa80e0ffb8961251343afc6efdea0@37.60.226.37:43656,5dfcb1c82cc041b18ff86dd520ce9185a2f0220c@116.203.133.101:43656,3373d3b6f215cc6dfb8e8b172053b72387575cb0@207.180.198.20:43656,ef2ad74a4f2e5e2a106f8b3df468984b267e2c02@5.9.73.170:29056,45bdc8628385d34afc271206ac629b07675cd614@65.21.202.124:25656,1c72d5acca5b75eec4aa9cfce4a8c298f7fecf46@20.78.12.218:26656,0a123ef98ea1d1176cdf7bec2b416b93010422bd@148.113.170.13:16610"
sed -i -e "s/^seeds *=.*/seeds = \"$SEEDS\"/; s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" $HOME/.empe-chain/config/config.toml
```
# Başlatalım
```shell
sudo systemctl restart emped
journalctl -fu emped -o cat
```
# Cüzdan oluşturalım
```shell
emped keys add wallet-name
```
# Faucet 
[Empeiria testnet faucet](https://faucet-testnet.empe.io/#/)

# Validator oluşturalım ( Son bloğa gelmeden oluşturmayın )

```shell
cd $HOME
```
```shell
emped tx staking create-validator \
  --amount=1000000uempe \
  --pubkey=$(emped tendermint show-validator) \
  --moniker "VALİDATOR-İSMİNİZ" \
  --chain-id=empe-testnet-2 \
  --identity "" \
  --details "HerculesNode community" \
  --website "http://herculesnode.com" \
  --commission-max-change-rate=0.01 \
  --commission-max-rate=1.0 \
  --commission-rate=0.05 \
  --min-self-delegation="1" \
  --fees=500uempe \
  --from=wallet-name \
  --node=http://localhost:7757
  -y
```

# Delege işlemleri
```shell
emped tx staking delegate VALİDATOR-ADRESİ amount000000uempe \
--chain-id empe-testnet-2 \
--from "wallet-name" \
--fees 500uempe \
--node=http://localhost:7757
```


# NODU KALDIRIN #
```shell
cd $HOME
sudo systemctl stop emped
sudo systemctl disable emped
sudo rm -rf /etc/systemd/system/emped.service
sudo systemctl daemon-reload
sudo rm -f /usr/local/bin/emped
sudo rm -f $(which emped)
sudo rm -rf $HOME/.empe-chain
sed -i "/EMPE_/d" $HOME/.bash_profile
```
