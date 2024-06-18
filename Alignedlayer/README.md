
### Airchains ZK-Rollups


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

```shell
git clone https://github.com/availproject/availup.git
```
