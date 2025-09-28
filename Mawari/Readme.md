# 🌌 Mawari Node Setup Guide  

![Mawari Logo](https://github.com/user-attachments/assets/1bad4a09-6812-4f18-8ac8-723c73ffd8a1)

---

## ⚙️ Minimum System Requirements  

| Component   | Minimum Requirement |  
|-------------|----------------------|  
| **CPU**     | 4+ Cores             |  
| **RAM**     | 5+ GB                |  
| **Disk**    | 50 GB+ NVMe SSD      |  
| **Network** | 100 Mbps (1 Gbps+)   |  

---

## ☁️ Recommended VPS Providers  

| Provider     | Link                                                                 | Features          |  
|--------------|----------------------------------------------------------------------|-------------------|  
| **Contabo**  | [Contabo](https://www.dpbolvw.net/click-101330552-12454592)          | Cheap / PayPal    |  
| **NetCup**   | [NetCup](https://www.netcup.com/en/?ref=261820)                      | Cheap / PayPal    |  

---

## 🌍 Official Links  

- 🐦 Twitter: [Mawari XR](https://x.com/mawariXR)  
- 🌐 Faucet: [Testnet Faucet](https://hub.testnet.mawari.net/)  
- 🎨 Mint Page: [Mint Testnet](https://testnet.mawari.net/mint)  

---

## 🔑 Web Preparation  

- ✅ Create a new **MetaMask Burner Wallet** (Testnet only).  
- ✅ Request tokens from the faucet.  
- ✅ Mint **3 NFTs** using the [Mint Page](https://testnet.mawari.net/mint).  

---

## 🔄 Update Server  

```bash
sudo apt update -y && sudo apt upgrade -y
```

---

## 📦 Install Required Packages  

```bash
sudo apt install htop ca-certificates zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev tmux iptables curl nvme-cli git wget make jq libleveldb-dev build-essential pkg-config ncdu tar clang bsdmainutils lsb-release libssl-dev libreadline-dev libffi-dev jq gcc screen file unzip lz4 -y
```

---

## 🐳 Install Docker  

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
docker version
```

---

## 🛠 Install Docker Compose  

```bash
VER=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)
curl -L "https://github.com/docker/compose/releases/download/$VER/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

---

## 👤 Add User to Docker Group  

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

---

## 📝 Node Configuration  

```bash
export MNTESTNET_IMAGE=us-east4-docker.pkg.dev/mawarinetwork-dev/mwr-net-d-car-uses4-public-docker-registry-e62e/mawari-node:latest
```

- Replace `OWNER_ADDRESS` with your **wallet address** (the same one you used for minting & faucet).  

```bash
export OWNER_ADDRESS=0xyourwalletaddresshere
```

---

## 🚀 Run Mawari Node  

```bash
mkdir -p ~/mawari && docker run -d --pull always -v ~/mawari:/app/cache -e OWNERS_ALLOWLIST=$OWNER_ADDRESS $MNTESTNET_IMAGE
```

---

## 🔍 Check Node Logs  

1. Get container ID:  

```bash
docker ps -a
```

2. View logs:  

```bash
docker logs -f <container_id>
```

---

## 🧩 Delegation  

1. Visit [Mawari Delegate](https://app.testnet.mawari.net/licenses)  
2. Select all **3 Licenses** → Click **Delegate**  
3. Paste your **Burner Wallet Address** → Confirm with MetaMask  

✅ Your node is now **active & delegated**  

---

## 🔐 Backup Burner Wallet Private Key  

```bash
cat ~/mawari/flohive-cache.json
```

⚠️ Store the private key **securely**.  

---

✨ Congratulations! Your Mawari Node is now up & running 🎉
