# Nexus III CLI Setup Guide

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Nexus Twitter(https://x.com/NexusLabs)


```
screen -S nexus
```
```
mkdir nexus
```
```
cd nexus
```
```
curl https://cli.nexus.xyz/ | sh
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
nexus-network start --node-id  xxxxx
```





### EVDE ÇALIŞTIRACAKLAR İÇİN
```
sudo nano /etc/docker/daemon.json
```
```
JSON

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
nexus-network start --node-id  xxxxx
```
Hazırlayan :  * [Twitter(https://x.com/onchainakira)
