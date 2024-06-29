### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [OG Discord](https://discord.gg/0glabs)
 * [Hercules Explorer](https://explorer.herculesnode.xyz/0G-Testnet/staking)
 * [Hercules web](https://herculesnode.xyz)


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
```bash
cd $HOME
git clone -b v0.3.2 https://github.com/0glabs/0g-storage-node.git
cd 0g-storage-node
git submodule update --init
cargo build --release
sudo mv "$HOME/0g-storage-node/target/release/zgs_node" /usr/local/bin
```

## 🟢 Enr çıkartalım
```bash
ENR_ADDRESS=$(wget -qO- eth0.me)
echo "export ENR_ADDRESS=${ENR_ADDRESS}"
```

```bash
cat <<EOF >> ~/.bash_profile
export ENR_ADDRESS=${ENR_ADDRESS}
export ZGS_CONFIG_FILE="$HOME/0g-storage-node/run/config.toml"
export ZGS_LOG_DIR="$HOME/0g-storage-node/run/log"
export ZGS_LOG_CONFIG_FILE="$HOME/0g-storage-node/run/log_config"
EOF

sourc



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

## 🟢 Store Miner key girelim OG Validator cüzdan private keyinizi gireceksiniz.
```bash
read -p "Enter your private key for miner_key configuration: " PRIVATE_KEY && echo
```

## 🟢 DB yolu oluşturalım
```bash
mkdir -p "$HOME/0g-storage-node/network" "$HOME/0g-storage-node/db"
```


## 🟢 Update config.toml 
```bash
sed -i 's|^\s*#\?\s*network_dir\s*=.*|network_dir = "/root/0g-storage-node/network"|' "$ZGS_CONFIG_FILE"

sed -i "s|^\s*#\?\s*network_enr_address\s*=.*|network_enr_address = \"$ENR_ADDRESS\"|" "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*network_enr_tcp_port\s*=.*|network_enr_tcp_port = 1234|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*network_enr_udp_port\s*=.*|network_enr_udp_port = 1234|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*network_libp2p_port\s*=.*|network_libp2p_port = 1234|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*network_discovery_port\s*=.*|network_discovery_port = 1234|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*network_target_peers\s*=.*|network_target_peers = 50|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*blockchain_rpc_endpoint\s*=.*|blockchain_rpc_endpoint = "https://og-testnet-jsonrpc.blockhub.id"|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*rpc_enabled\s*=\s*true|rpc_enabled = true|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*rpc_listen_address\s*=\s*"0.0.0.0:5678"|rpc_listen_address = "0.0.0.0:5678"|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*db_dir\s*=.*|db_dir = "/root/0g-storage-node/db"|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*log_config_file\s*=.*|log_config_file = "/root/0g-storage-node/run/log_config"|' "$ZGS_CONFIG_FILE"

sed -i 's|^\s*#\?\s*log_directory\s*=.*|log_directory = "/root/0g-storage-node/run/log"|' "$ZGS_CONFIG_FILE"

sed -i "s|^\s*#\?\s*miner_key\s*=.*|miner_key = \"$PRIVATE_KEY\"|" "$ZGS_CONFIG_FILE"
```

## 🟢 Servis dosyası oluşturma
```bash
sudo tee /etc/systemd/system/zgs.service > /dev/null <<EOF
[Unit]
Description=0G Storage Node
After=network.target

[Service]
User=$USER
Type=simple
ExecStart=/usr/local/bin/zgs_node --config $HOME/0g-storage-node/run/config.toml
Restart=on-failure
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF
```
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
