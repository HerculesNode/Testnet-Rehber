

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)
 * [Nubit Website](https://alpha.nubit.org/#/)<br>
 * [Nubit-Discord](https://discord.gg/nubit)<br>
 * [Nubit-Twitter](https://x.com/Nubit_org)<br>

## 💻 Sistem Gereksinimleri
| Bileşenler | Minimum Gereksinimler | 
| ------------ | ------------ |
| CPU |	2|
| RAM	| 4 GB |
| Storage	| 40++ GB SSD |

## 🟢 Nubit dashboard:

```shell
https://alpha.nubit.org/
```

## 🟢 Genel Sunucu Güncellemeleri


```shell
sudo apt-get update && sudo apt-get upgrade -y 
```

```shell
curl -sL1 https://nubit.sh | bash
```
## 🟢 Her şey yüklenip bloklar akmaya başladınktan sonra ctrl+c ile durdurup servis olarak çalıştıracağız. Harici olarak önceki etkinliklerden cüzdan adresiniz varsa onu import edebilirsiniz.

## 🟢 Cüzdan import kodu: 
```shell
/root/nubit-node/bin/nkey add my_nubit_key --recover --p2p.network nubit-alphatestnet-1 --node.type light
```
## 🟢 Servis oluşturma:
```shell
sudo tee /etc/systemd/system/nubitd.service > /dev/null <<EOF
[Unit]
Description=nubitd node
After=network-online.target
[Service]
User=$USER
ExecStart=/root/nubit-node/bin/nubit light start \
--p2p.network nubit-alphatestnet-1 \
--core.ip validator.nubit-alphatestnet-1.com \
--metrics.endpoint otel.nubit-alphatestnet-1.com:4318 \
--rpc.skip-auth
Restart=on-failure
RestartSec=5
LimitNOFILE=65535
[Install]
WantedBy=multi-user.target
EOF
```

## 🟢 Servis başlatalım.
```shell
sudo systemctl daemon-reload
```
```shell
sudo systemctl enable nubitd
```
```shell
sudo systemctl restart nubitd
```

## 🟢 Log kontrol.

```shell
sudo journalctl -u nubitd -fo cat
```

## 🟢  Public Key öğrenme. Key kısmının devamında tırnak içindeki değer.

```shell
/root/nubit-node/bin/nkey list --p2p.network nubit-alphatestnet-1 --node.type light
```

