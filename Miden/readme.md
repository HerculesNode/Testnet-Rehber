
### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Miden Twitter](https://x.com/0xMiden)

💡 Miden Nedir?
Miden, client-side (istemci taraflı) çalışan bir blokzincirdir. Yani kullanıcılar işlemlerini merkeziyetsiz biçimde kendileri işleyip ispatlayabilir. Bu yaklaşım sayesinde işlem yükü ağdan alınarak kullanıcıya kaydırılır.



# 🇹🇷 Miden Testnet Rehberi



## 📦 Kurulum

### 1. Screen içinde işlemleri yapalım. Rustc yükleyelim (1 e tıklayın) Gerekli dizini oluşturun


```bash
screen -S miden
```
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
```bash
source $HOME/.cargo/env
```
```bash
mkdir miden-client
cd miden-client
```

### 2. Miden CLI'ı yükleyin

```bash
cargo install miden-cli
```

Versiyonu kontrol edin:

```bash
miden --version
# Örn: Miden 0.9.0
```

---

## 🌐 Testnet'e Katılın

```bash
miden init --network testnet
```

Bu komut, testnet yapılandırmasıyla `miden-client.toml` dosyasını oluşturur.

---

## 👛 Hesap Oluşturun

```bash
miden new-wallet --mutable
miden account -l
```
![miden1](https://github.com/user-attachments/assets/f940972a-32d5-45c2-9f85-1bd787016627)

Çıktıdaki **Account ID** değerini not edin. Addresi de not edin bu adres ile token isteyeceğiz.

---

## 💰 Faucet'ten Token Alın

1. Siteye gidin:(https://faucet.testnet.miden.io/)
2. Faucet id adresinizi girin." miden account -l " ile Address kısmındaki address
3. "Send Private Note" seçeneğine tıklayın.  
4. İndirilen `note.mno` dosyasını kaydedin.
5. Kaydettiğiniz dosyayı sunucuya atın.

---

## 📥 Notu İçeri Aktarın

```bash
miden import <dosya-yolu>/note.mno
miden notes
```
Succesfully imported note olarak gözükecektir.
Not “Expected” olarak listelenecektir. İşlemi tamamlamak için ağı senkronize etmeniz gerekir.

---

## 🔄 Rollup Senkronizasyonu

```bash
miden sync
```

---

## 🔓 Notu Tüketin

```bash
miden consume-notes --account <Account-ID> <Note-ID>
```
## 🔓 Faucet aldığınız zaman aşağıda kodlar direk çıkıyor.
Not durumu önce `Processing` olarak görünür. Ağı tekrar senkronize edin:

```bash
miden sync
miden notes
```

---

## 💳 Varlıkları Görüntüleyin

```bash
miden account --show <Account-ID>
```

---

## ✅ Başarıyla Tamamlandı!

- [x] İstemci kuruldu  
- [x] Hesap oluşturuldu  
- [x] Faucet'ten token alındı  
- [x] ZKP üretildi ve gönderildi  
- [x] Fonlar başarıyla hesaba geçti  

---

## 🔗 Kaynaklar

- [Miden GitHub](https://github.com/0xMiden)
- [Faucet](https://faucet.testnet.miden.io/)


---

> Hazırlayan: [onchainakira](https://x.com/onchainakira)

