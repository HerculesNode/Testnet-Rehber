# ⚡ Aztec Node Docker Kurulumu ve Oylama Rehberi<p align="center"><img width="700" src="https://github.com/user-attachments/assets/24374de1-d735-4754-ad05-1220d897724b" alt="Aztec Docker"></p><br><h2>🌐 Bağlantılar</h2><ul><li>🧩 <a href="https://t.me/HerculesNodeTG">Hercules Telegram</a></li><li>🐦 <a href="https://twitter.com/Herculesnode">Hercules Twitter</a></li></ul><br><h2>🧱 Kurulum Adımları</h2><h3>1️⃣ Klasör oluşturun</h3><pre><code>mkdir aztec && cd aztec</code></pre><h3>2️⃣ .env dosyası oluşturun</h3><pre><code>nano .env</code></pre><p>İçine şunu yazın 👇</p><pre><code>ETHEREUM_RPC_URL=SEPOLIA_URLINIZI_YAZIN
CONSENSUS_BEACON_URL=BEACON_URLINIZI_YAZIN
VALIDATOR_PRIVATE_KEY=0XPRIVATEKEY
COINBASE=0x76e78677E1e2312f37D0079ED332386B5908A802
P2P_IP=SUNUCU_IP_ADRESINIZ
</code></pre><h3>3️⃣ docker-compose.yml oluşturun</h3><pre><code>nano docker-compose.yml</code></pre><p>İçine şunu yazın 👇</p><pre><code>services:
  aztec-node:
    container_name: aztec-sequencer
    image: aztecprotocol/aztec:2.0.3
    network_mode: host 
    restart: unless-stopped
    environment:
      ETHEREUM_HOSTS: ${ETHEREUM_RPC_URL}
      L1_CONSENSUS_HOST_URLS: ${CONSENSUS_BEACON_URL}
      DATA_DIRECTORY: /data
      VALIDATOR_PRIVATE_KEY: ${VALIDATOR_PRIVATE_KEY}
      COINBASE: ${COINBASE}
      P2P_IP: ${P2P_IP}
      LOG_LEVEL: debug
    entrypoint: >
      sh -c 'node --no-warnings /usr/src/yarn-project/aztec/dest/bin/index.js start --network testnet --node --archiver --sequencer'
    ports:
      - 40400:40400/tcp
      - 40400:40400/udp
      - 8080:8080
      - 8880:8880
    volumes:
      - /root/.aztec/testnet/data/:/data
</code></pre><h3>4️⃣ Node’u başlatın 🚀</h3><pre><code>docker-compose down -v && rm -rf ~/.aztec/testnet/data/ && docker-compose up -d</code></pre><p align="center"><img width="900" src="https://github.com/user-attachments/assets/a761a1e8-9420-4531-9392-9abb7c7aa260" alt="docker logs"></p><h3>5️⃣ Log’ları izleyin</h3><pre><code>docker-compose logs -fn 1000</code></pre><h2>🗳️ Oylamaya Katılın</h2><pre><code>curl -X POST http://localhost:8880 \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc":"2.0",
    "method":"nodeAdmin_setConfig",
    "params":[{"governanceProposerPayload":"0x9D8869D17Af6B899AFf1d93F23f863FF41ddc4fa"}],
    "id":1
  }'
</code></pre><p align="center"><img width="650" src="https://github.com/user-attachments/assets/913e9c44-7368-4873-b5ed-1816d8b9e21d" alt="voting response"></p><h2>🧰 CLI Üzerinden Çalıştırmak İsterseniz</h2><pre><code>aztec start --node --archiver --sequencer \
  --network testnet \
  --l1-rpc-urls RPC_URL \
  --l1-consensus-host-urls BEACON_URL \
  --sequencer.validatorPrivateKeys 0xPK1,0xPK2,etc \
  --sequencer.publisherPrivateKey 0xYourPrivateKey \
  --sequencer.coinbase 0xYourAddress \
  --sequencer.governanceProposerPayload 0x9D8869D17Af6B899AFf1d93F23f863FF41ddc4fa \
  --p2p.p2pIp YOUR_IP
</code></pre><h2>🧭 Ek Bilgiler</h2><ul><li>📘 Docker versiyonu: >= 20.10</li><li>🧾 Aztec versiyonu: 2.0.3</li><li>⚙️ Network: testnet</li><li>💾 Data path: /root/.aztec/testnet/data</li></ul><hr><p>Pull Request açabilir veya geliştirmeler için issue oluşturabilirsiniz 💙</p><p align="center">Hazırlayan: <a href="https://twitter.com/Herculesnode">Hercules Node</a></p>
