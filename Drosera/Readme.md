# Drosera Network Node Setup Guide

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Drosera Discord](https://discord.gg/drosera)



Bu rehberde Drosera testnet ağına nasıl katkıda bulunabileceğinizi adım adım anlatıyoruz:

1. CLI kurulumları
2. Trap (tuzak) kurulumu
3. Operator (operatör) bağlantısı
4. Docker ve SystemD ile kurulum 

---

## ✨ Sistem Gereksinimleri

- ⚖️ 2 CPU
- 🧼 4 GB RAM
- 📊 20 GB Disk Alanı

---

## ⌚ Gerekli Kurulumlar

```bash
sudo apt-get update && sudo apt-get upgrade -y

sudo apt install curl ufw iptables build-essential git wget lz4 jq make gcc nano automake autoconf tmux htop nvme-cli libgbm1 pkg-config libssl-dev libleveldb-dev tar clang bsdmainutils ncdu unzip -y
```

---

## 🛠️ Trap Kurulumu

### CLI Kurulumları

**Drosera CLI**:
```bash
curl -L https://app.drosera.io/install | bash
source ~/.bashrc
droseraup
```

**Foundry**:
```bash
curl -L https://foundry.paradigm.xyz | bash
source ~/.bashrc
foundryup
```

**Bun**:
```bash
curl -fsSL https://bun.sh/install | bash
source ~/.bashrc
```

### Trap Oluşturma
```bash
mkdir my-drosera-trap && cd my-drosera-trap

git config --global user.email "mail@ornek.com"
git config --global user.name "kullaniciadi"

forge init -t drosera-network/trap-foundry-template
bun install
forge build
```

### Deploy Etme
```bash
DROSERA_PRIVATE_KEY=PRIVATE_KEY drosera apply
```

---

## 📈 Trap Kontrol Paneli

https://app.drosera.io adresine giderek
- Cüzdanınızla bağlanın
- "Traps Owned" sekmesinden deploy ettiğiniz trap'i görün

---

## 📢 Bloom Boost

Panelden trap'inizi açın ve "Send Bloom Boost" butonuna tıklayarak biraz Holesky ETH gönderin.

![image](https://github.com/user-attachments/assets/16ee2f5c-c4fe-4501-8ba9-5efa5e16dbe5)


---


### Whitelist Ayarları
```bash
cd my-drosera-trap
nano drosera.toml
```
En alttaki private yi private_trap yapın address aynı kalacak operator_address yerine kendi mm adresini yazacaksınz. Tırnaklar kalacak.
```toml
private_trap = true
whitelist = ["Operator_Address"]
```
```bash
DROSERA_PRIVATE_KEY=PRIVATE_KEY drosera apply
```

### Operator CLI
```bash
cd ~
curl -LO https://github.com/drosera-network/releases/releases/download/v1.16.2/drosera-operator-v1.16.2-x86_64-unknown-linux-gnu.tar.gz
tar -xvf drosera-operator-*.tar.gz
sudo cp drosera-operator /usr/bin
drosera-operator --version
```



### Operator Kaydı-       Private_KEY yerine keyi yazın.
```bash
drosera-operator register --eth-rpc-url https://ethereum-holesky-rpc.publicnode.com --eth-private-key PRIVATE_KEY
```

### Portları Açma
```bash
sudo ufw allow ssh
sudo ufw allow 31313/tcp
sudo ufw allow 31314/tcp
sudo ufw enable
```

---

## 🚀 Operator Başlatma  ( 2 çeşit kurulum var ister Docker ister SystemD ikisini bir kurmayın hangisi size uygunsa onunla yapın ) 

### 1. kurulum Docker Yöntemi
```bash
git clone https://github.com/0xmoei/Drosera-Network
cd Drosera-Network
cp .env.example .env
nano .env
```

- `.env` içindeki bilgileri doldurun

```bash
docker compose up -d
docker logs -f drosera-node
```

### 2. kurulum SystemD Yöntemi             VPS_IP        PRIVATE_KEY    bilgilerini giriyoruz. İsterseniz Alchemy den kendinize özel rpc alabilirsiniz. Onu da rpc-url kısmına yazabilirsiniz.
```bash
sudo tee /etc/systemd/system/drosera.service > /dev/null <<EOF
[Unit]
Description=Drosera Operator
After=network.target

[Service]
User=$USER
ExecStart=$(which drosera-operator) node --db-file-path $HOME/.drosera.db \
--network-p2p-port 31313 --server-port 31314 \
--eth-rpc-url https://ethereum-holesky-rpc.publicnode.com \
--eth-private-key PRIVATE_KEY \
--listen-address 0.0.0.0 \
--network-external-p2p-address VPS_IP \
--disable-dnr-confirmation true

[Install]
WantedBy=multi-user.target
EOF
```
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl enable drosera
```
```bash
sudo systemctl start drosera
```
```bash
journalctl -u drosera -f
```

---

## 🔗 Operator Bağlantısı

https://app.drosera.io adresine gidin, Trap detaylarına girin ve "Opt-in" butonuna tıklayarak operator adresinizi trap'e bağlayın. Eğer Register işlemini yapmadıysanız Opt-in yapamazsınız.

---
![image](https://github.com/user-attachments/assets/c7fbf68b-cb87-44d3-95d9-a98fd75257aa)

## 🔺 Node Durumu
**Tüm işlemler bitince tekrar başlatın.**
```bash
sudo systemctl restart drosera
```
Dashboard'da yeşil bloklar oluşmaya başladıysa node'unuz başarılı şekilde çalışıyor demektir.

---
