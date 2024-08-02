## Bu betik otomatik versiyon kontrolü yapar. 

## Güncelse birşey yapmaz

![image](https://github.com/user-attachments/assets/e5774e44-506c-4f26-af89-302d50a171b8)

## Güncel değilse çalışır

![image](https://github.com/user-attachments/assets/25a741f8-32b6-4fc7-9b98-306a6eee6e88)


```shell
screen -S otokontrol
```

```shell
cd ~/hubble
```

```shell
sudo apt install python3
```

```shell
sudo apt install python3-pip
```

```shell
pip install packaging
```

```shell
nano warpcontrol.sh
```


## farcaster logları için hangi SCREEN kullanıyorsanız aşağıdaki kodda bulunan screen -S warp olan yeri değiştirin. daha sonra kopyalayın CTRL + X + Y ile kaydedin

```shell
#!/bin/bash


VERSION_FILE="versiyon.txt"


if [ ! -f "$VERSION_FILE" ]; then
  echo "@farcaster/hubble@1.14.1" > "$VERSION_FILE"
fi


compare_versions() {
  python3 -c "
from packaging import version
import sys

v1 = sys.argv[1]
v2 = sys.argv[2]

if version.parse(v1) > version.parse(v2):
    print('1')  # v1 > v2
else:
    print('0')  # v1 <= v2
" "$1" "$2"
}


check_and_upgrade() {

  URL="https://github.com/farcasterxyz/hub-monorepo/releases"


  LATEST_VERSION=$(curl -s $URL | grep -oP '@farcaster/hubble@[0-9]+\.[0-9]+\.[0-9]+' | head -1)

  
  CURRENT_VERSION=$(cat "$VERSION_FILE")


  LATEST_VERSION_NO_PREFIX="${LATEST_VERSION#@farcaster/hubble@}"
  CURRENT_VERSION_NO_PREFIX="${CURRENT_VERSION#@farcaster/hubble@}"

  echo "Mevcut Sürüm: $CURRENT_VERSION"
  echo "En Son Sürüm: $LATEST_VERSION"


  if [ -n "$LATEST_VERSION" ]; then
    COMPARE_RESULT=$(compare_versions "$LATEST_VERSION_NO_PREFIX" "$CURRENT_VERSION_NO_PREFIX")
    if [ "$COMPARE_RESULT" -eq 1 ]; then
      echo "Yeni sürüm bulundu: $LATEST_VERSION. Güncelleniyor..."

      
    
      screen -S warp -X stuff $'./hubble.sh upgrade\n'

   
      echo "$LATEST_VERSION" > "$VERSION_FILE"
    else
      echo "Sürüm güncel: $CURRENT_VERSION"
    fi
  else
    echo "En son sürüm bilgisi alınamadı."
  fi
}

while true; do
  check_and_upgrade
  # 1 kere günde HerculesNode
  sleep 84600
done



```

```shell
chmod +x warpcontrol.sh
```

```shell
./warpcontrol.sh
```
