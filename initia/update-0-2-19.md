## 🟢 v0.2.9 güncelleme
```shell
cd $HOME
rm -rf initia
git clone https: //github.com/initia-labs/initia.git
cd initia
git checkout v0.2.19

make build

sudo mv build/initiad $(which initiad)
```


```shell
sudo systemctl restart initiad.service && sudo journalctl -fu initiad.service -o cat
```
