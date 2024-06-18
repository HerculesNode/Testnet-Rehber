

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)



## 🟢 Ön Bilgilendirme
- Herkese açık işlemdir. Olası bir ödül için yapılması gerekiyor. Ubuntu 22.04 gerekiyor




## 🟢 Güncellemeler
```shell
sudo apt update -y
```

```shell
sudo apt upgrade -y
```

```shell
sudo apt-get install curl -y
```

## 🟢 Prof indirelim

```shell
curl -L https://raw.githubusercontent.com/yetanotherco/aligned_layer/main/batcher/aligned/install_aligned.sh | bash
```

```shell
source /root/.bashrc
```

## 🟢 Kanıt Dosyası indirelim

```shell
curl -L https://raw.githubusercontent.com/yetanotherco/aligned_layer/main/batcher/aligned/get_proof_test_files.sh | bash
```


## 🟢 Bu kodu tek seferde girin

```shell
rm -rf ~/aligned_verification_data/ &&
aligned submit \
--proving_system SP1 \
--proof ~/.aligned/test_files/sp1_fibonacci.proof \
--vm_program ~/.aligned/test_files/sp1_fibonacci-elf \
--aligned_verification_data_path ~/aligned_verification_data \
--conn wss://batcher.alignedlayer.com
```

- Bu işlemden sonra size bir çıktı verecek aşağıdaki resimdeki gibi orada tx adresi var onu kopyalayın 

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/63d1c72f-ce18-4b57-8c38-0b4aa01687f6)


- Holesky çıktısı

```shell
aligned verify-proof-onchain \
--aligned-verification-data ~/aligned_verification_data/*.json \
--rpc https://ethereum-holesky-rpc.publicnode.com \
--chain holesky
```

## 🟢 Twitter hesabınızda paylaşın

Aşağıdaki tx adresine kendi adresinizi yazın

```shell
Just submitted a proof via @alignedlayer 

I am now #aligned ✅
https://explorer.alignedlayer.com/batches/0xf8657184e0f7dc58b28f31e051196b44124d411d2a1f7bf511850d01d5090ec4
```

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/73c05ee7-cf11-419f-b961-44dfd33d8c60)


## 🟢 Discord Testnet kanalında x gönderinizin linkini paylaşın

Discod : https://discord.gg/alignedlayer

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/cb7f592d-e282-4209-b9a3-e6655dc5ac20)


