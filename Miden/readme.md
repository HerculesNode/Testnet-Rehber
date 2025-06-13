
### Linkler
 * [Hercules Telegram](https://t.me/HerculesNodeTG)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Miden Twitter](https://x.com/0xMidenk)

💡 Miden Nedir?
Miden, client-side (istemci taraflı) çalışan bir blokzincirdir. Yani kullanıcılar işlemlerini merkeziyetsiz biçimde kendileri işleyip ispatlayabilir. Bu yaklaşım sayesinde işlem yükü ağdan alınarak kullanıcıya kaydırılır.



# 🇹🇷 Miden Testnet Rehberi



## 📦 Kurulum

### 1. Gerekli dizini oluşturun

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

Çıktıdaki **Account ID** değerini not edin.

---

## 💰 Faucet'ten Token Alın

1. Siteye gidin: [https://faucet.miden.xyz](https://faucet.miden.xyz)  
2. Account ID’nizi girin.  
3. "Send Private Note" seçeneğine tıklayın.  
4. İndirilen `note.mno` dosyasını kaydedin.

---

## 📥 Notu İçeri Aktarın

```bash
miden import <dosya-yolu>/note.mno
miden notes
```

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

- [Miden GitHub](https://github.com/mir-protocol/miden)
- [Faucet](https://faucet.miden.xyz)


---

> Hazırlayan: [onchainakira](https://x.com/onchainakira)

