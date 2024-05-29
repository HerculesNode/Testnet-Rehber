### Herculesnode Viper Güncelleme

### işlemleri viper bloklarının aktığı screen de yapabilirsiniz. screen içine girdikten sonra ctry c ile durdurup devam ediniz.
### Eğer jail iseniz "viper servicers unjail <operatorAddr> <fromAddr> testnet" kodu ile unjail yapın.



``` 
sudo systemctl stop viper.service
```

```
rm -rf /usr/local/bin/viper
```

```
sudo wget -O  ~/viper.tgz  https://github.com/HerculesNode/Testnet-Rehber/raw/main/Viper/viper.tgz
```

```
tar -xvf ~/viper.tgz
```

```
rm -rf ~/viper.tgz
```

```
cp ~/viper /usr/local/bin/
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

