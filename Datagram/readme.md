
### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [DataGram Twitter](https://twitter.com/DGramNetwork)
 * [DataGram Discord](https://discord.com/invite/datagramnetwork)
## First Register Datagram Network ##
  1. Register use email : [https://dashboard.datagram.network](https://dashboard.datagram.network?ref=913903416) 
  2. Copy your Keys in `Wallet Licenses` Sağ tarafta request var oradan key alıyoruz. [https://dashboard.datagram.network/wallet?tab=licenses]




İlk Yöntem
```
mkdir datagram
```
```
cd datagram
```
```
https://raw.githubusercontent.com/HerculesNode/Testnet-Rehber/refs/heads/main/Datagram/datagram-installer.sh
```
```
chmod +x datagram-installer.sh
```
```
sudo bash datagram-installer.sh
```
Burada size key soracak onu girdikten sonra enter deyin. Datagram servis dosyası arka planda çalışacak.

**  restart-datagram                         # Restart service
  status-datagram                          # Check online/offline and connection status
  sudo journalctl -u datagram.service -f   # View live logs
  sudo bash datagram-installer.sh --uninstall  # Uninstall all components
**
--------------------------------------------------
## Create Folder Datagram ##
  1. Create Folder Datagram- Klasör oluşturuyoruz.

    mkdir datagram
    cd datagram
    
  2. Download CLI Datagram- Cli indiriyoruz. 

    
    wget https://github.com/Datagram-Group/datagram-cli-release/releases/latest/download/datagram-cli-x86_64-linux && chmod +x datagram-cli-x86_64-linux
    
## Running Datagram CLI ##
  1. Create Screen
     ```
     screen -S datagram
     ```
  2. Change `YOUR_API_KEY` in Wallet Licenses after Done you can Detached press `CTRL+A+D`
     ```
     ./datagram-cli-x86_64-linux run -- -key YOUR_API_KEY
     ```
  3. To see your screen
     ```
     screen -r datagram
     ```
-------------------------------------
