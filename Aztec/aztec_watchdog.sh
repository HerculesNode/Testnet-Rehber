#!/bin/bash

SCREEN_NAME="aznode"
AZTEC_CMD=$'aztec start --node --archiver --sequencer --network alpha-testnet --l1-rpc-urls RPC_URL --l1-consensus-host-urls BEACON_URL --sequencer.validatorPrivateKeys 0xYourPrivateKey --sequencer.coinbase 0x381929D0Ce1Ebb278448e1E4061b517B87b60e6F --p2p.p2pIp IP --p2p.maxTxPoolSize 1000000000\n'

while true; do
  if docker ps --format '{{.Image}}' | grep -q "aztecprotocol/aztec:latest"; then
    echo "[INFO] $(date) - Kontrol edildi, çalışıyor."
  else
    echo "[WARNING] $(date) - Container durmuş, aznode screen içinde yeniden başlatılıyor!"
    
    # aznode screen içindeki aztec sürecini CTRL+C ile sonlandırmaya çalış
    screen -S "$SCREEN_NAME" -p 0 -X stuff $'\003'
    sleep 2

    # ardından yeniden başlatma komutunu gönder
    screen -S "$SCREEN_NAME" -p 0 -X stuff "$AZTEC_CMD"
  fi
  sleep 30
done
