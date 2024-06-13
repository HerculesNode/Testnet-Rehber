![image](https://github.com/HerculesNode/0G-Newton/assets/101635385/9f3bd440-d371-47b5-afcd-f0d0f4e342d1)



### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [OG Discord](https://discord.gg/0glabs)
 * [Hercules Explorer](https://explorer.herculesnode.xyz/0G-Testnet/staking)
 * [Hercules web](https://herculesnode.xyz)

## 🟢 rol alma

- Discord Roles kanalına gidin ve rolleri alın

![image](https://github.com/HerculesNode/0G-Testnet/assets/101635385/c2ddbff1-1989-4f63-8b20-cf3ebb368442)


## 🟢 Sistem özellikleri
| Ram | cpu     | disk                      |
| :-------- | :------- | :-------------------------------- |
| `16GB`      | `4Core` | `500+ SSD` |

- Bunlar max gereksinim daha düşükte çalıştırabilir !

## 🟢 Sistemi güncelleyelim
```shell
sudo apt update && \
sudo apt install curl git jq build-essential gcc unzip wget lz4 -y
sudo apt-get install clang cmake build-essential
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

## 🟢 Rust indirin
```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## 🟢 Dosyaları indirin
```shell
sudo apt install git
git clone -b v0.3.0 https://github.com/0glabs/0g-storage-node.git
```

## 🟢 Cargo yükleme
```shell
cd $HOME/0g-storage-node
git submodule update --init
sudo apt install cargo
cargo build --release
```

## 🟢 Variable yükleme
```shell
ENR_ADDRESS=$(wget -qO- eth0.me)
echo "export ENR_ADDRESS=${ENR_ADDRESS}" >> ~/.bash_profile
echo 'export LOG_CONTRACT_ADDRESS="0xb8F03061969da6Ad38f0a4a9f8a86bE71dA3c8E7"' >> ~/.bash_profile
echo 'export MINE_CONTRACT="0x96D90AAcb2D5Ab5C69c1c351B0a0F105aae490bE"' >> ~/.bash_profile
echo 'export ZGS_LOG_SYNC_BLOCK="334797"' >> ~/.bash_profile
echo 'export BLOCKCHAIN_RPC_ENDPOINT="https://0gevmrpc.nodebrand.xyz"' >> ~/.bash_profile
source ~/.bash_profile
echo -e "\n\033[31mCHECK YOUR VARIABLES\033[0m\n\nENR_ADDRESS: $ENR_ADDRESS\n\n\nLOG_CONTRACT_ADDRESS: $LOG_CONTRACT_ADDRESS\nMINE_CONTRACT: $MINE_CONTRACT\nZGS_LOG_SYNC_BLOCK: $ZGS_LOG_SYNC_BLOCK\nBLOCKCHAIN_RPC_ENDPOINT: $BLOCKCHAIN_RPC_ENDPOINT\n\n\033[33mby Nodebrand.\033[0m"
```

## 🟢 Private key çıkarmak ve kaydetmek için uygulayın.
```shell
PRIVATE_KEY=$(0gchaind keys unsafe-export-eth-key $WALLET_NAME) &&
sed -i 's|^miner_key = ""|miner_key = "'"$PRIVATE_KEY"'"|' $HOME/0g-storage-node/run/config.toml
```

Network name : 0g Chain Testnet

New RPC URL : https://rpc-testnet.0g.ai

Chain ID : 16600

Currency symbol: A0GI

Block explorer URL (Optional) : https://scan-testnet.0g.ai/


## 🟢 Node harici çalıştıracak kişiler Metamask üzerinden cüzdanın private keyini export edip aşağıdaki kod ile kaydetsin.
```shell
read -sp "Enter your private key: " PRIVATE_KEY && echo
sed -i 's|^miner_key = ""|miner_key = "'"$PRIVATE_KEY"'"|' $HOME/0g-storage-node/run/config.toml
```

## 🟢 Update config.toml 
```shell
sed -i '
s|^\s*#\?\s*network_dir\s*=.*|network_dir = "network"|
s|^\s*#\?\s*network_enr_address\s*=.*|network_enr_address = "'"$ENR_ADDRESS"'"|
s|^\s*#\?\s*network_enr_tcp_port\s*=.*|network_enr_tcp_port = 1234|
s|^\s*#\?\s*network_enr_udp_port\s*=.*|network_enr_udp_port = 1234|
s|^\s*#\?\s*network_libp2p_port\s*=.*|network_libp2p_port = 1234|
s|^\s*#\?\s*network_discovery_port\s*=.*|network_discovery_port = 1234|
s|^\s*#\?\s*rpc_enabled\s*=.*|rpc_enabled = true|
s|^\s*#\?\s*db_dir\s*=.*|db_dir = "db"|
s|^\s*#\?\s*log_config_file\s*=.*|log_config_file = "log_config"|
s|^\s*#\?\s*log_directory\s*=.*|log_directory = "log"|
s|^\s*#\?\s*network_boot_nodes\s*=.*|network_boot_nodes = \["/ip4/54.219.26.22/udp/1234/p2p/16Uiu2HAmPxGNWu9eVAQPJww79J32pTJLKGcpjRMb4Qb8xxKkyuG1","/ip4/52.52.127.117/udp/1234/p2p/16Uiu2HAm93Hd5azfhkGBbkx1zero3nYHvfjQYM2NtiW4R3r5bE2g"\]|
s|^\s*#\?\s*log_contract_address\s*=.*|log_contract_address = "'"$LOG_CONTRACT_ADDRESS"'"|
s|^\s*#\?\s*mine_contract_address\s*=.*|mine_contract_address = "'"$MINE_CONTRACT"'"|
s|^\s*#\?\s*log_sync_start_block_number\s*=.*|log_sync_start_block_number = '"$ZGS_LOG_SYNC_BLOCK"'|
s|^\s*#\?\s*blockchain_rpc_endpoint\s*=.*|blockchain_rpc_endpoint = "'"$BLOCKCHAIN_RPC_ENDPOINT"'"|
s|^\s*miner_id\s*=\s*""|# miner_id = ""|
' $HOME/0g-storage-node/run/config.toml
```

## 🟢 Servis dosyası oluşturma
```shell
sudo tee /etc/systemd/system/zgs.service > /dev/null <<EOF
[Unit]
Description=ZGS Node
After=network.target

[Service]
User=$USER
WorkingDirectory=$HOME/0g-storage-node/run
ExecStart=$HOME/0g-storage-node/target/release/zgs_node --config $HOME/0g-storage-node/run/config.toml
Restart=on-failure
RestartSec=10
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
```

## 🟢 Servis başlatma
```shell
sudo systemctl daemon-reload && \
sudo systemctl enable zgs && \
sudo systemctl start zgs
```

## 🟢 Logları kontrol etme
```shell
tail -f ~/0g-storage-node/run/log/zgs.log.$(TZ=UTC date +%Y-%m-%d)
```

## 🟢 Loglarda bir hata alırsanız aşağıdaki kodu uygulayın. Çıktığı starage-node kanalına gönderin.
```shell
echo -e "LOG_CONTRACT_ADDRESS: $LOG_CONTRACT_ADDRESS\nMINE_CONTRACT: $MINE_CONTRACT\nZGS_LOG_SYNC_BLOCK: $ZGS_LOG_SYNC_BLOCK\nBLOCKCHAIN_RPC_ENDPOINT: $BLOCKCHAIN_RPC_ENDPOINT\n\n\033[33mby Nodebrand.\033[0m"
```
