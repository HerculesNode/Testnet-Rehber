
### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [DataGram Twitter](https://twitter.com/DGramNetwork)
 * [DataGram Discord](https://discord.com/invite/datagramnetwork)
## First Register Datagram Network ##
  1. Register use email : [https://dashboard.datagram.network](https://dashboard.datagram.network?ref=913903416) 
  2. Copy your Keys in `Wallet Licenses` Sağ tarafta request var oradan key alıyoruz. [https://dashboard.datagram.network/wallet?tab=licenses]




### Servis olarak çalıştırmak

```
mkdir datagram
```
```
cd datagram
```
```
wget -O datagram-installer.sh https://raw.githubusercontent.com/HerculesNode/Testnet-Rehber/refs/heads/main/Datagram/datagram-installer.sh
```
```
chmod +x datagram-installer.sh
```
```
sudo bash datagram-installer.sh
```
Burada size key soracak onu girdikten sonra enter deyin. Datagram servis dosyası arka planda çalışacak.

**restart-datagram**                         # Restart service

**status-datagram**                         # Check online/offline and connection status

**sudo journalctl -u datagram.service -f**   # View live logs

**sudo bash datagram-installer.sh --uninstall**  # Uninstall all components

Ayrıca direk pc üzerinden de aşağıdaki linkten indirebilirsiniz.

**https://dashboard.datagram.network/#nodeOperator**




