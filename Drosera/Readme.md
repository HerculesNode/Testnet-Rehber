# Drosera Network Node Setup Guide

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Drosera Discord](https://discord.gg/drosera)



Bu rehberde Drosera testnet ağına nasıl katkıda bulunabileceğinizi adım adım anlatıyoruz:

1. CLI kurulumları
2. Trap (tuzak) kurulumu
3. Operator (operatör) bağlantısı

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

### Docker Kurulumu
```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

sudo apt-get install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

sudo docker run hello-world
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

```bash
drosera dryrun
```

---

## 🛠️ Operator Kurulumu

### Whitelist Ayarları
```bash
cd my-drosera-trap
nano drosera.toml
```
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

### Docker Image
```bash
docker pull ghcr.io/drosera-network/drosera-operator:latest
```

### Operator Kaydı
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

## 🚀 Operator Başlatma

### Docker Yöntemi
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

### SystemD Yöntemi
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

sudo systemctl daemon-reload
sudo systemctl enable drosera
sudo systemctl start drosera
journalctl -u drosera -f
```

---

## 🔗 Operator Bağlantısı

https://app.drosera.io adresine gidin, Trap detaylarına girin ve "Opt-in" butonuna tıklayarak operator adresinizi trap'e bağlayın.

---

## 🔺 Node Durumu

Dashboard'da yeşil bloklar oluşmaya başladıysa node'unuz başarılı şekilde çalışıyor demektir.

---
