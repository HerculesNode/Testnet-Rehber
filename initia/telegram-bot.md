### Linkler
 * [Hercules Telegram](https://t.me/HerculesNode)
 * [Hercules Twitter](https://twitter.com/Herculesnode)
 * [Hercules Web](https://herculesnode.xyz)
 * [Initia Explorer](https://explorer.herculesnode.xyz/0G-Testnet/staking)


## 🟢 Özellikleri Kuralım

```shell
sudo apt update
```
```shell
sudo apt install python3 python3-pip
```
```shell
pip3 install python-telegram-bot requests
```

```shell
pip install python-telegram-bot && \
pip install requests
```

## 🟢 dosyamızı oluşturalım

```shell
nano herculesnode.py
```

## 🟢 Telegram botunu yazalım

- TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  
- Telegramda @BotFather ile etkileşime geçin ve bot oluşturun 
- Size botun kodunu verecek bu kodu aşağıdaki yere yazın

```shell
import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def get_last_block_height():
    url = "https://b545809c-5562-4e60-b5a1-22e83df57748.initiation-1.mesa-rpc.ue1-prod.newmetric.xyz/abci_info?"
    response = requests.get(url)
    data = response.json()
    return int(data['result']['response']['last_block_height'])

def get_latest_block_height():
    result = subprocess.run(['initiad', 'status'], capture_output=True, text=True)
    if result.returncode == 0:
        data = result.stdout
        import json
        json_data = json.loads(data)
        return int(json_data['sync_info']['latest_block_height'])
    else:
        return None

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Merhaba! Bu bot blok yüksekliği kontrolü yapar. HerculesNode')

def check_block_heights(update: Update, context: CallbackContext) -> None:
    try:
        last_block_height = get_last_block_height()
        latest_block_height = get_latest_block_height()

        if latest_block_height is None:
            update.message.reply_text("Sunucuda komut çalıştırılırken bir hata oluştu.")
            return

        response_message = (
            f"Last Block Height: {last_block_height}\n"
            f"Latest Block Height: {latest_block_height}\n"
        )

        if last_block_height != latest_block_height:
            response_message += f"Fark: {abs(last_block_height - latest_block_height)}"
        else:
            response_message += "Blok yükseklikleri eşit."

        update.message.reply_text(response_message)

    except Exception as e:
        update.message.reply_text(f"Bir hata oluştu: {e}")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("check", check_block_heights))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

```

## 🟢 Çalıştıralım

```shell
chmod +x herculesnode.py
```

```shell
python3 herculesnode.py
```


## 🟢 Telegram botumuza gelelim

- /start komutu verelim

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/87c554ca-7855-497a-ba76-59f5700e1a75)


- /chech komutu verelim

![image](https://github.com/HerculesNode/Testnet-Rehber/assets/101635385/678226bb-1f46-4744-ae71-783745d25bbd)
