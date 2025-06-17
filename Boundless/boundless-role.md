
### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Boundless Twitter](https://twitter.com/boundless_xyz)
 * [Boundless Discord](https://discord.gg/nqRgP9VJEu)


## Boundless Dev ve Prove Rolü alma rehberi ( Gerekli şeyler ) Buradaki işlemler Sözleşme ile etkileşime girmek için Node çalıştırmak için değildir !

## 1 usdc ile olduğunu da belirttiler isterseniz aşağıda 1 usdc ile deneyebilirsiniz olmaz ise 10 usdc deneyin

  1. işlemler Base mainnet üzerinde yapılmaktadır.
  2. Hesabınızda base ağında 10 USDC ve azıcık eth olması gerekiyor. 
  3. Discord hesabınızın 6 aydan eski olması gerekiyor.
  4. github hesabınızın 6 aydan eski olması gerekiyor.
  5. Guild hesabınızın bağlı olduğu tilki cüzdan adresinizin private keyi gerekiyor
  6. Alchemy üzerinden base mainnet rpc almanız gerkeiyo ( ücretsiz )




### Kurulum

```
apt update
```

```
sudo apt install -y curl git build-essential cmake protobuf-compiler
```

```
screen -S boundless
```

```
git clone https://github.com/boundless-xyz/boundless
```
```
cd boundless
```

### Rust Kurulumu
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
```
source $HOME/.cargo/env
```

### RISC Zero Kurulumu
```
curl -L https://risczero.com/install | bash
```
```
source ~/.bashrc
```
```
rzup install
```

### Bento Client Kurulumu
```
cargo install --git https://github.com/risc0/risc0 bento-client --bin bento_cli
```
```
export PATH="$HOME/.cargo/bin:$PATH"
```
```
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
```
```
source ~/.bashrc
```

### CLI Kurulumu

```
cargo install --locked boundless-cli
```

### Env Ayarları
```
nano .env.base
```
![image](https://github.com/user-attachments/assets/3b9da608-6f74-4c1f-8715-33300be91072)

- Resimdeki gibi olacak bu şekilde kaydedin.
- Alchemy üzerinden Base mainnet rpc alın.
- Cüzdanınızın private keyini alıp aşağıdaki şekilde env dosyasını değiştirin ve kaydedin.

```
# Base contract addresses
export VERIFIER_ADDRESS=0x0b144e07a0826182b6b59788c34b32bfa86fb711
export BOUNDLESS_MARKET_ADDRESS=0x26759dbB201aFbA361Bec78E097Aa3942B0b4AB8
export SET_VERIFIER_ADDRESS=0x8C5a8b5cC272Fe2b74D18843CF9C3aCBc952a760

# Public order stream URL
export ORDER_STREAM_URL="https://base-mainnet.beboundless.xyz"
export ETH_RPC_URL="ALCHEMY-BASE-MAİNNET-LİNKİ"
export PRIVATE_KEY="CÜZDANINIZIN-PRİVATE-KEYİ"

```

- Kayıt sonrası aşağıdaki kodu çalıştıırn

```
source .env.base
```

- Hesabınıza 10 usdc gönderin ve eser miktarda eth olsun 2-3$ yeter

### Prover Rolü için aşağıdaki kodu çalıştırın  ( cüzdanınızda 10 usdc olsun ) 
### ( 1 usdc ile denemek istiyorsanız burayı düzeltin account deposit-stake 1 )

```
boundless \
  --rpc-url "$ETH_RPC_URL" \
  --private-key "$PRIVATE_KEY" \
  --boundless-market-address 0x26759dbB201aFbA361Bec78E097Aa3942B0b4AB8 \
  --set-verifier-address 0x8C5a8b5cC272Fe2b74D18843CF9C3aCBc952a760 \
  --verifier-router-address 0x0b144e07a0826182b6b59788c34b32bfa86fb711 \
  --order-stream-url "https://base-mainnet.beboundless.xyz" \
  account deposit-stake 10

```

- Başarılı işlem çıktısı 

![image](https://github.com/user-attachments/assets/d331af43-f42c-493d-adf8-9c7e00138b12)




### Dev Rolü için aşağıdaki kodu çalıştırın ( cüzdanınızda 0.000001 eth olsun. Ben 0.0001 yaptım daha düşükte yapabilirsiniz )

```
boundless \
  --rpc-url "$ETH_RPC_URL" \
  --private-key "$PRIVATE_KEY" \
  --boundless-market-address 0x26759dbB201aFbA361Bec78E097Aa3942B0b4AB8 \
  --set-verifier-address 0x8C5a8b5cC272Fe2b74D18843CF9C3aCBc952a760 \
  --verifier-router-address 0x0b144e07a0826182b6b59788c34b32bfa86fb711 \
  --order-stream-url "https://base-mainnet.beboundless.xyz/" \
  account deposit 0.000001

```

- Başarılı işlem çıktısı 

![image](https://github.com/user-attachments/assets/62b2fb20-766f-4606-9c46-adaefffbfd1a)


### Guild görevini tamamlayın

- Bu adrese gidin : https://guild.xyz/boundless-xyz

- İşlemleri tamamlayın Aşağıdaki gibi olacak 

![image](https://github.com/user-attachments/assets/b47d8bf8-1e07-464d-a62d-6621b5574a37)


### Discord Sunucusuna gidin ve rolleri alın

![image](https://github.com/user-attachments/assets/1aa0c583-cb54-43a5-9137-064753492092)


- başarılı ise roller bu şekilde gözükecektir.

![image](https://github.com/user-attachments/assets/0d1b345b-0944-43be-8e1a-bb19f704f045)



Rehber için https://github.com/Himess Adresinden destek alınmıştır.  

