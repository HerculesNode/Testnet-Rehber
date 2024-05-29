### Herculesnode Viper Güncelleme

### işlemleri viper bloklarının aktığı screen de yapabilirsiniz. screen içine girdikten sorna ctry c ile durdurup devam ediniz.
### Eğer jail iseniz "viper servicers unjail <operatorAddr> <fromAddr> testnet" kodu ile unjail yapın.


```
cd ~/.viper
```
 
``` 
sudo systemctl stop viper.service
```

```
rm -rf /usr/local/bin/viper
```

```
sudo wget -O  /usr/local/bin/viper  https://github.com/HerculesNode/Testnet-Rehber/Viper/viper.tgz

```

```
tar -xvf /usr/local/bin/viper.tgz
```

```
rm -rf /usr/local/bin/viper.tgz
```

```
 chmod +x /usr/local/bin/viper
 ```

```
cd ~/.viper
```

```
rm -r data
```

```
sudo git clone https://github.com/vishruthsk/data.git data
```

```
sudo chown -R root ~/.viper/data
```

 
```
viper network version
 ```

### AppVersion: PT-0.1.3 olacak

```
sudo systemctl daemon-reload
```

```
sudo systemctl start viper.service
```

```
journalctl -u viper -f
```

