###  öncelikle Domaininiz üzerinden 3 tane alan adı açacaksınız ve bunları sunucunuzun ip adresine yönlendireceksiniz. <br> Hosting varsa Cpanel üzerinden yapabilir yoksa domain aldığınız yerden alt ( sub domain şeklinde ekleyebilirsiniz

- 1- dymrollapp-api.domainAdresiniz.com
- 2- dymrollapp-evm.domainAdresiniz.com
- 3- dymrollapp-rpc.domainAdresiniz.com

```
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential snapd unzip nginx
sudo apt -qy upgrade
```

###  Api yapma

```
sudo nano /etc/nginx/sites-enabled/dymrollapp-api
```

- `dymrollapp-api.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim Kaydetmek için : ctrl + x + Y

```
server {
listen 80;
server_name dymrollapp-api.domainAdresiniz.com;

location / {
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Max-Age 3600;
    add_header Access-Control-Expose-Headers Content-Length;
    
    proxy_pass http://0.0.0.0:1317;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
}
```

###  RPC yapma

```
sudo nano /etc/nginx/sites-enabled/dymrollapp-rpc
```

- `dymrollapp-rpc.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim Kaydetmek için : ctrl + x + Y

```
server {
listen 80;
server_name dymrollapp-rpc.domainAdresiniz.com;

location / {
    proxy_pass http://0.0.0.0:26657;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
}
```

###  EVM yapma

```
sudo nano /etc/nginx/sites-enabled/dymrollapp-rpc
```

- `dymrollapp-evm.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim Kaydetmek için : ctrl + x + Y

```
sudo nano /etc/nginx/sites-available/dymrollapp-evm


server {
listen 80;
server_name dymrollapp-evm.domainAdresiniz.com;

location / {
    proxy_pass http://0.0.0.0:8545;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
}
```


###  Cerbot kurun

```
sudo snap install --classic certbot
```

###  Cerbot ile SSL alın

1 - Yapmış olduğunuz 3 domain içinde aşağıdaki kodu tek tek çalıştırın orada domainler gözükecek Örneğin 1 tuşuna basın ve SSL alın sonra aşağıdaki kodu tekrar girin diğerini yapın.

```
sudo certbot --nginx --register-unsafely-without-email
```


### rpc kontrol

- Yukarıda yaptığınız rpc adresini girin ve kontrol edin.
- Rpc kontrol etmek için resimdeki gibi çıktı almalısınız.

```
curl https://RPC-ADRESİNİZ/health
```




###  DYM metadata değiştirin

- Burada Metadata export edin daha sonra `/root/.roller/rollapp/init/` bu klasöre girin orada `sequencer-metadata.json` dosyası olacak bunu açon ve yukarıda aldığınız domainleri yazın.

```
roller rollapp sequencer metadata export
```

###  DYM metadata kaydedin

- Aşağıdaki kodu girin ve metadata güncelleyin 10 dakika sonra güncellenir. 

```
roller rollapp sequencer metadata update
```

###  Restart atın

### ibc
dymd query ibc channel channels

### İbc yeniden başlatma.
roller eibc services restart

### relayer yeniden başlatma.
roller relayer services restart

### rollapp yeniden başlatma.
roller rollapp services restart

### Ayrıca 
journalctl -fu relayer <br>
journalctl -fu rollapp <br>
journalctl -fu eibc <br>
bu kodlar ile de bakabilirsiniz.
