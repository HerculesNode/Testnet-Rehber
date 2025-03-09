Gaia kurduğunuz sunucuya ikinci bir node kurmak isterseniz bu kodları kullanabilirsiniz.
Sunucu özellikleriniz iyi ise tercih edin. Çok node kurunca bazılarını offline olarak görüyor.



Kurulum

1. Klasör Oluşturma

mkdir -p gaia

2. Gaianet Kurulumu

curl -sSfL 'https://raw.githubusercontent.com/GaiaNet-AI/gaianet-node/main/install.sh' | bash -s -- --ggmlcuda 12 --base $HOME/gaia

gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/qwen2-0.5b-instruct/config.json --base $HOME/gaia

3. Port Ayarlarını Yapılandırma

gaianet config --base $HOME/gaia --port 8101

4. Node'u Başlatma

gaianet start --base $HOME/gaia

5. Node ID ve Cihaz ID Öğrenme

gaianet info --base $HOME/gaia

