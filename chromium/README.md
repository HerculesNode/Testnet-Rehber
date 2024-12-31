
### chromium Kurulum


### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.xyz)



## 🟢 Ön Bilgilendirme
- Bu araç ubuntu sunucunuzda chrome kullanmanıza yarar


## 🟢 kurulum
```shell
mkdir chromium
```

```shell
cd chromium
```

```shell
nano docker-compose.yaml
```

```shell
---
services:
  chromium:
    image: lscr.io/linuxserver/chromium:latest
    container_name: chromium
    security_opt:
      - seccomp:unconfined #optional
    environment:
      - CUSTOM_USER=KULLANICI-ADINIZ    
      - PASSWORD=ŞİFRENİZ    
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - CHROME_CLI=
    volumes:
      - /root/chromium/config:/config
    ports:
      - 3010:3000 
      - 3011:3001
    shm_size: "1gb"
    restart: unless-stopped
```


## 🟢 Çalıştıralım
```shell
docker compose up -d
```

