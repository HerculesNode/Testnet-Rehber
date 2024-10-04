###  öncelikle Domaininiz üzerinden 3 tane alan adı açacaksınız ve bunları sunucunuzun ip adresine yönlendireceksiniz. <br> Hosting varsa Cpanel üzerinden yapabilir yoksa domain aldığınız yerden alt ( sub domain şeklinde ekleyebilirsiniz

- 1- dymrollapp-api.domainAdresiniz.co
- 2- dymrollapp-evm.domainAdresiniz.co
- 3- dymrollapp-rpc.domainAdresiniz.co

```
sudo apt -q update
sudo apt -qy install curl git jq lz4 build-essential snapd unzip nginx
sudo apt -qy upgrade
```

###  Api yapma

```
sudo nano /etc/nginx/sites-enabled/dymrollapp-api
```

- `dymrollapp-api.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim

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

- `dymrollapp-rpc.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim

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

- `dymrollapp-evm.domainAdresiniz.com` burayı kendi domaininiz ile değiştirin içine aşağıdaki kodu yazıp kaydedelim

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
