![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/9f3bd440-d371-47b5-afcd-f0d0f4e342d1)

### zgtendermint_16600-2  -  v0.2.3

- If you have previously operated a validator, do not upload the Priv Key. Instead, you will create a new validator. Only recover your wallet and use the code to create a new validator. Then, back up the new priv_key.

### Link
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [OG Discord](https://discord.gg/0glabs)
 * [HerculesNode Explorer](https://explorer.herculesnode.com/0G-Testnet/staking)


## 🟢 Discord Role

- Go to the Discord Roles channel and take the roles.

![image](https://github.com/HerculesNode/0G-Testnet/assets/101635385/c2ddbff1-1989-4f63-8b20-cf3ebb368442)


## 🟢 System specifications
| Ram | cpu     | disk                      |
| :-------- | :------- | :-------------------------------- |
| `8GB`      | `4Core` | `500+ SSD` |


## 🟢 System Update
```shell
sudo apt update && \
sudo apt install curl git jq build-essential gcc unzip wget lz4 -y
```

## 🟢 Go Install
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

## 🟢 0G clone File v0.2.3
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

## 🟢 Node Setting

```shell
0gchaind config chain-id zgtendermint_16600-2
0gchaind config keyring-backend os
0gchaind config node tcp://localhost:26657
```

- Please write your NODE NAME

```shell
0gchaind init NODE-NAME --chain-id zgtendermint_16600-2
```

## 🟢 Genesis file 

```shell
rm ~/.0gchain/config/genesis.json
wget -P ~/.0gchain/config https://github.com/0glabs/0g-chain/releases/download/v0.2.3/genesis.json

```

```shell
0gchaind validate-genesis
```

## 🟢 PEER and SEED 

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

## 🟢 Port settings (use if another project is running).

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

## 🟢 Start

```shell
sudo systemctl daemon-reload
sudo systemctl restart 0gchaind
```

## 🟢 Log

```shell
sudo journalctl -u 0gchaind.service -f --no-hostname -o cat
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/57951da3-14ac-460b-ae3e-bc63588053b2)



## 🟢 Wallet creation (If you participated in the previous testnet, recover the same wallet. If you are setting up for the first time, do not use the recovery code).

- Recovery code: This code recovers using the old mnemonic phrases.

```shell
0gchaind keys add WALLET-NAME --eth --recover
```

- New wallet Create

```shell
0gchaind keys add WALLET-NAME --eth
```

## 🟢 Getting the EVM address: If you have recovered, it will provide the same address. If you have created a new one, it will give the address associated with it

```shell
echo "0x$(0gchaind debug addr $(0gchaind keys show WALLET-NAME -a) | grep hex | awk '{print $3}')"
```

```shell
0gchaind keys unsafe-export-eth-key WALLET-NAME
```


## 🟢 Faucet

- Get faucet tokens from here. You will receive them with your EVM address.
- https://faucet.0g.ai/


## 🟢 Synchronization Check: If the blocks are synchronized, you will get a FALSE output. After that, create the validator.

```shell
0gchaind status | jq
```

![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/1dba9cf6-65f6-44d6-aa97-501136d7a297)




## 🟢 Create a validator (Enter your Moniker, which is your display name, and your wallet name)

```shell
0gchaind tx staking create-validator \
  --amount=1000000ua0gi \
  --pubkey=$(0gchaind tendermint show-validator) \
  --moniker=MONIKER-NAME \
  --chain-id=zgtendermint_16600-2 \
  --commission-rate="0.10" \
  --commission-max-rate="0.20" \
  --commission-max-change-rate="0.01" \
  --min-self-delegation=1 \
  --from=WALLET-NAME \
  --identity="" \
  --website="https://herculesnode.com" \
  --details="HerculesNode community" \
  --gas=auto \
  --gas-adjustment=1.4 \
  -y
```

## 🟢 Let's check the validator.

- If you have previously operated a validator, when you enter the validator creation code, your old validator information will appear if you have recovered your old wallet. Now, backup the /root/.0gchain/config/priv_validator_key.json file!

- If you have set up a new validator, it will provide the address for the new validator. Backup this file again.

- If you want to check, go to that address and append the validator address to the end and open it. 
- https://explorer.herculesnode.com/0G-Testnet/staking/VALIDATOR-ADRESS

- Afterwards, open the priv_validator_key.json file you backed up with a text editor and verify that the information matches what is in Explorer. The file content should look like the image.

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/41b269c6-cf8e-4362-8a09-ed9edd1fa1d4)


## 🟢 delegate 

```shell
0gchaind tx staking delegate $(0gchaind keys show WALLET-NAME --bech val -a) 1000000ua0gi --from WALLET-NAME -y
```

## 🟢 Unjail 

```shell
0gchaind tx slashing unjail --from CÜZDAN-ADINIZ --from WALLET-NAME --gas=500000 --gas-prices=99999ua0gi -y
```

## 🟢 Active List

```shell
0gchaind q staking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_BONDED")' \
| jq -r '.tokens + " - " + .description.moniker' \
| sort -gr | nl
```

## 🟢 Inaktive list

```shell
0gchaind q staking validators -o json --limit=1000 \
| jq '.validators[] | select(.status=="BOND_STATUS_UNBONDED")' \
| jq -r '.tokens + " - " + .description.moniker' \
| sort -gr | nl
```

## 🟢 Balance

```shell
0gchaind q bank balances $(0gchaind keys show WALLET-NAME -a)
```

## 🟢 Validator status

```shell
0gchaind q staking validator $(0gchaind keys show WALLET-NAME --bech val -a)
```


## 🟢 Delete

```shell
sudo systemctl stop 0gchaind.service
sudo systemctl disable 0gchaind.service
sudo rm /etc/systemd/system/0gchaind.service
rm -rf $HOME/.0gchain $HOME/0g-chain
```


## 🟢 RPC enable

- Navigate to /root/.0gchain/config/app.toml file and find the API Configuration section.

- Change the part where it says false to true, then save the file and restart your node

```shell
nano .0gchain/config/app.toml
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/20aacc68-21e1-4837-8d36-395825f48d3e)


```shell
sudo systemctl daemon-reload
sudo systemctl restart 0gchaind
```

```shell
sudo journalctl -u 0gchaind.service -f --no-hostname -o cat
```

