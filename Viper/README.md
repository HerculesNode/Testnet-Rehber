### Herculesnode Viper 1.5 Güncelleme

### İşlemleri viper bloklarının aktığı screen de yapabilirsiniz. Screen içine girdikten sonra ctry c ile durdurup devam ediniz.

### Eğer jail iseniz unjail yapın. aperator addr ile from addr kendi cüzdan adresiniz olacak.
``` shell
viper servicers unjail operatorAddr fromAddr testnet
```

### Pause durumuna geçtiyse unpause kodu. 
``` shell
viper servicers unpause operatorAddr fromAddr testnet
```

### Validator durumunuzu kontrol etmek için bu kodu uygulayın.

``` shell
curl http://127.0.0.1:26657/status
```


``` shell
sudo systemctl stop viper.service
```

```shell
rm -rf /usr/local/bin/viper
```

```shell
wget -O /usr/local/bin/viper http://37.120.189.81/viper/viper8
```


```shell
chmod +x /usr/local/bin/viper
```

```shell
sudo systemctl daemon-reload
 ```

```shell
viper network version
 ```

### AppVersion: PT-0.1.5 olacak

## 🟢 Logları kontrol edin. Eğer wrong block hatası alıyorsanız aşağıdakileri uygulayın. 

## 🟢 Log kontrol. Ctrl + c ile çıkın
```shell
journalctl -u viper -f
```

```shell
cd ~/.viper
```

```shell
rm -r data
```

```shell
sudo git clone https://github.com/vishruthsk/data.git data
```

```shell
sudo chown -R root ~/.viper/data
```



```
journalctl -u viper -f
```

