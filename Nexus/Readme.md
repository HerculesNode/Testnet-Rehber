# Nexus III CLI Setup Guide

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Nexus Twitter](https://x.com/NexusLabs)


```
screen -S nexus
```
```
mkdir nexus
```
```
cd nexus
```

### Ubuntu 24 olanlar direk nexus-network start --node-id xxx ile başlayabilir.
```
nano Dockerfile
```

```
FROM ubuntu:24.04

RUN apt update && apt install -y curl bash libssl-dev ca-certificates

RUN curl https://cli.nexus.xyz/ | sh

ENV PATH="/root/.nexus/bin:$PATH"

CMD ["/bin/bash"]
```

Ctrl  x y ile kaydedin.

### Evdeki pc de ubuntu 22 de çalıştıracaklar sayfanın sonundan devam etsin.
```
docker build -t nexus-debug .
```
```
docker run -it --rm nexus-debug
```
### XXX yazan yere siteden aldığınız CLI numarasını yazıyorsunuz.

```
curl https://cli.nexus.xyz/ | sh
```
```
source /root/.profile
```

- Buradan id alın aşağıda xxx olan yere idi yazıp komutu çalıştırın : https://app.nexus.xyz/nodes

```
nexus-network start --node-id  xxxxx
```


![image](https://github.com/user-attachments/assets/c4b0a04f-e0e5-4ea8-bde9-55c6126f5c25)



### EVDE ÇALIŞTIRACAKLAR İÇİN
```
sudo nano /etc/docker/daemon.json
```


```
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```
```
sudo systemctl restart docker
```
```
docker build --network=host -t nexus-debug .
```
```
docker run -it --rm nexus-debug
```
```
curl https://cli.nexus.xyz/ | sh
```
```
source /root/.profile
```
```
nexus-network start --node-id  xxxxx
```
Hazırlayan :  * [Twitter](https://x.com/onchainakira)


### Eğer bunlara rağmen portalda gözükmüyorsa aşağıdaki kodları uygulayın.
```
nexus-network register-user --wallet-address <your-wallet-address>
```
```
nexus-network register-node
```
```
nexus-network start
```



