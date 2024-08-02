## Bu betik otomatik versiyon kontrolü yapar. 


```shell
screen -S otokontrol
```

```shell
cd ~/hubble
```

```shell
cat > versiyon.txt
```

```shell
chmod +x versiyon.txt
```

```shell
nano warpcontrol.sh
```

## Aşağıdaki komutu tek seferde kopyalayın CTRL + X + Y ile kaydedin

```shell
#!/bin/bash


VERSION_FILE="current_version.txt"


if [ ! -f "$VERSION_FILE" ]; then
  echo "1.14.2" > "$VERSION_FILE"
fi


check_and_upgrade() {

  URL="https://github.com/farcasterxyz/hub-monorepo/releases"


  CURRENT_VERSION=$(cat "$VERSION_FILE")

 
  LATEST_VERSION=$(curl -s $URL | grep -oP 'v[0-9]+\.[0-9]+\.[0-9]+' | head -1)


  if [ "$LATEST_VERSION" != "v$CURRENT_VERSION" ]; then
    cd hubble
 
    screen -S warp -X stuff $'./hubble.sh upgrade\n'

   
    echo "${LATEST_VERSION#v}" > "$VERSION_FILE"
  else
    echo "Sürüm güncel: $CURRENT_VERSION"
  fi
}

while true; do
  check_and_upgrade
  # Günde 2 kex herculesnode
  sleep 43200
done

```

```shell
chmod +x warpcontrol.sh
```

```shell
./warpcontrol.sh
```
