

### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.com)



## 🟢 Ön Bilgilendirme
- Ubuntu ve diğer Linux dağıtımlarında, swap alanı (veya takas alanı), bellek yönetimi için kullanılan bir depolama alanıdır. Swap alanı, sistemin RAM'i (Random Access Memory) dolduğunda, geçici olarak bellek yükünü hafifletmek için kullanılır. Bu alan, fiziksel RAM'in yeterli olmadığı durumlarda sistemin daha stabil çalışmasını sağlar.

## 🟢 Swap Alanının İşlevleri
## 🟢 Bellek Taşması (Memory Overflow): RAM'in tamamı kullanıldığında, swap alanı devreye girerek aktif olmayan süreçlerin belleğini geçici olarak depolar. Bu sayede sistem çökmelerinin ve performans kayıplarının önüne geçilir.

## 🟢 Hibernation (Uyku Modu): Sistem hibernation moduna geçtiğinde, tüm RAM içeriği swap alanına yazılır. Sistem tekrar açıldığında, RAM'deki veriler swap alanından geri yüklenir.

## 🟢 Swap Alanı Türleri
Swap Bölümü (Partition): Sabit diskte oluşturulan özel bir bölüm, yalnızca swap için ayrılmıştır. Bu yöntem, genellikle daha hızlıdır ve daha iyi performans sağlar.

## 🟢 Swap Dosyası: Mevcut bir dosya sistemi üzerinde oluşturulan bir dosya, swap alanı olarak kullanılır. Bu yöntem, daha esnek bir yapı sunar çünkü swap alanını büyütmek veya küçültmek daha kolaydır.

## 🟢 Swap Alanı Yönetimi
Ubuntu'da swap alanını yönetmek için birkaç temel komut bulunmaktadır:

## 🟢 Swap Alanı Boyutu Ne Kadar Olmalı?
Swap alanının boyutu, sistemin kullanım senaryosuna ve RAM miktarına bağlı olarak değişir. Geleneksel olarak, swap alanının boyutu şu şekilde önerilmektedir:

## 🟢Ne olmalı

RAM 4 GB veya daha az ise: RAM'in 2 katı.
RAM 4-8 GB arası ise: RAM'in 1.5 katı.
RAM 8-16 GB arası ise: RAM ile aynı boyutta.
RAM 16 GB ve üzeri ise: İhtiyaca göre ayarlanabilir, genellikle RAM'in yarısı kadar yeterlidir.
Ancak, hibernation kullanıyorsanız, swap alanının en az RAM kadar veya daha fazla olması önerilir.

	Ubuntu swap alanı, sistem performansını artırmada ve bellek yönetimini optimize etmede önemli bir rol oynar. Swap alanının doğru yapılandırılması, özellikle sınırlı RAM'e sahip sistemlerde, daha akıcı ve kararlı bir deneyim sunar.



## 🟢 Swap Alanını Görüntüleme: Bu komut, aktif swap alanlarını gösterir.


```shell
swapon --show
```

## 🟢 Swap Alanı Eklemek (Dosya Olarak): Bu komutlar, 2 GB boyutunda bir swap dosyası oluşturur ve etkinleştirir.2G yerine tavsiye edilen biktar girilebilir. 8 GB ram var ise 12GB vb.


```shell
sudo fallocate -l 2G /swapfile
```
```shell
sudo chmod 600 /swapfile
```
```shell
sudo mkswap /swapfile
```
```shell
sudo swapon /swapfile
```

## 🟢 Swap Alanını Kalıcı Yapmak: Bu komut, sistem her başladığında swap dosyasının otomatik olarak etkinleştirilmesini sağlar.


```shell
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

## 🟢 Swap Alanını Devre Dışı Bırakma: Bu komut, tüm swap alanlarını devre dışı bırakır.

```shell
sudo swapoff -a
```

## 🟢 Swap Alanını görüntüleme:

```shell
htop
```
```shell
free -m
```
```shell
sudo swapon -s
```