### Herculesnode Scannerx Initia RPC alma

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)


## 🟢 Sorgulama Yapın 
```shell
RPC="$(wget -qO- eth0.me)$(grep -A 3 "\[rpc\]" ~/.initia/config/config.toml | egrep -o ":[0-9]+")" && echo $RPC
```

![image](https://github.com/HerculesNode/initia/assets/101635385/b0e4d258-5e09-4670-9116-26e6f2a19e5b)

- RPC sorgulayın bu hatayı alırsanız gerekli düzenleme yapmamız gerekiyor.

```shell
curl $RPC/status
```

![image](https://github.com/HerculesNode/initia/assets/101635385/fc4f6f68-8d4f-4156-bf71-66d378cdf87b)

- Aşağıdaki kodu girin 127 olan yeri 0.0.0.0 olarak açık hale getirecek.  daha sonra buradan kontrol edin .initia/config/config.toml laddr olarak aratın değiştiğini göreceksiniz. 

```shell
sed -i 's/^laddr = "tcp:\/\/127\.0\.0\.1:/laddr = "tcp:\/\/0.0.0.0:/' $HOME/.initia/config/config.toml
```

- yeniden başlatın

```shell
sudo systemctl restart initiad
```

- Sorgulayın bir sürü çıktı alacaksınız.

```shell
curl $RPC/status
```


## 🟢 Explorer açın 

- http://İP-ADRESİNİZ:15657 bu şekilde girin artık rpc hazır. Ben Explorer kurduğum için böyle çıkıyor sizin ip olarak çıkacak

![image](https://github.com/HerculesNode/initia/assets/101635385/1b2dccb2-a268-4f54-99bc-5534065d0139)



- http://İP-ADRESİNİZ:15657/status? bu şekilde girin rpc detaylarını göreceksiniz. 






