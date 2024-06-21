## 🟢 v0.2.21 güncelleme
```shell
cd $HOME
rm -rf initia
git clone https://github.com/initia-labs/initia.git
cd initia
git checkout v0.2.21

make build

sudo mv build/initiad $(which initiad)
```


```shell
sudo systemctl restart initiad.service && sudo journalctl -fu initiad.service -o cat
```
