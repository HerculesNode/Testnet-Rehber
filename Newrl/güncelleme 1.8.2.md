

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)



## 🟢 1.8.2 güncellemesi. Normalde otomatik güncelleme yapıyor. Bazı nodeler güncellenmemiş. Öncelikle aşağıdaki adresten IP aratarak versiyon 1.8.2 mi bakın. Eğer daha düşükse aşağıdaki kodları uygulayın.

```shell
https://newrlscan.io/
```


```shell
screen -X -S newrl kill
```

```shell
screen -S newrl
```

```shell
cd newrl
```

```shell
./scripts/install.sh mainnet
```

## 🟢 Eğer install.sh çalıştırdıktan sonra loglarda requirements.txt şeklinde bir hata verip versiyon 1.8.2 olmazsa sunucuda newrl klasörü içindeki requirements.txt dosyasını silin tekrar install kodunu çalıştırın.

```shell
rm -rf   "/root/newrl/requirements.txt"
```

## 🟢  Yukarıdaki hatayı vermiyorsa aşağıdaki koddan devam edebilirsiniz.

```shell
./scripts/start.sh mainnet
```

## 🟢 ctrl a + d ile çıkın. Biraz zaman sonra tarayıcıdan yine kontrol edin.






