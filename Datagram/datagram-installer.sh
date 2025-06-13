#!/bin/bash
set -e

# Configuration
BINARY_URL="https://github.com/Datagram-Group/datagram-cli-release/releases/latest/download/datagram-cli-x86_64-linux"
BINARY_NAME="datagram"
INSTALL_PATH="/usr/local/bin/$BINARY_NAME"
STATUS_SCRIPT_PATH="/usr/local/bin/status-datagram"
RESTART_SCRIPT_PATH="/usr/local/bin/restart-datagram"

# Uninstall Mode
if [[ "$1" == "--uninstall" ]]; then
  echo "----------------------------------------"
  echo "Uninstalling Datagram CLI and Service..."
  echo "----------------------------------------"

  if systemctl list-units --full -all | grep -Fq "datagram.service"; then
    echo "Stopping and disabling datagram.service..."
    sudo systemctl stop datagram.service
    sudo systemctl disable datagram.service
    sudo rm -f /etc/systemd/system/datagram.service
    sudo systemctl daemon-reload
  else
    echo "datagram.service not found, skipping service removal."
  fi

  sudo rm -f "$INSTALL_PATH"
  sudo rm -f "$STATUS_SCRIPT_PATH"
  sudo rm -f "$RESTART_SCRIPT_PATH"

  echo "----------------------------------------"
  echo "Datagram CLI and all related services have been removed."
  echo "----------------------------------------"
  exit 0
fi

echo "----------------------------------------"
echo "Installing Datagram CLI..."
echo "----------------------------------------"

read -p "Please enter your Datagram License Key: " LICENSE_KEY
echo "You entered: $LICENSE_KEY"
read -p "Press Enter to continue, or Ctrl+C to abort..."

sudo rm -f "$INSTALL_PATH"
curl -fsSL "$BINARY_URL" -o "$BINARY_NAME"
chmod +x "$BINARY_NAME"
sudo mv "$BINARY_NAME" "$INSTALL_PATH"

echo "----------------------------------------"
echo "Setting up systemd service with your License Key..."
echo "----------------------------------------"

sudo tee /etc/systemd/system/datagram.service > /dev/null <<EOF
[Unit]
Description=Datagram CLI Service
After=network.target

[Service]
ExecStart=$INSTALL_PATH run -- -key $LICENSE_KEY
Restart=always
RestartSec=5
User=root
WorkingDirectory=/root

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable datagram.service
sudo systemctl restart datagram.service

echo "----------------------------------------"
echo "Creating status-datagram and restart-datagram CLI utilities..."
echo "----------------------------------------"

# Enhanced Status Checker CLI
sudo tee "$STATUS_SCRIPT_PATH" > /dev/null <<'EOC'
#!/bin/bash
SERVICE="datagram.service"
status=$(systemctl is-active $SERVICE)

if [[ "$status" != "active" ]]; then
    echo "❌ Datagram Node Status: OFFLINE (Not Running)"
    exit 1
fi

log_check=$(sudo journalctl -u $SERVICE --no-pager -n 50 | grep -Ei "connected|running|ready")

if [[ -n "$log_check" ]]; then
    echo "✅ Datagram Node Status: ONLINE (Running and Connected)"
else
    echo "⚠️  Datagram Node Status: RUNNING but NOT CONNECTED"
    echo "Please check the logs for more details:"
    echo "  sudo journalctl -u $SERVICE -f"
fi
EOC

# Restart CLI with confirmation
sudo tee "$RESTART_SCRIPT_PATH" > /dev/null <<'EOR'
#!/bin/bash
echo "Restarting datagram service..."
sudo systemctl restart datagram.service
echo "✅ Datagram service restarted successfully."
EOR

sudo chmod +x "$STATUS_SCRIPT_PATH"
sudo chmod +x "$RESTART_SCRIPT_PATH"

echo "----------------------------------------"
echo "Datagram CLI installed and service started."
echo "Use the following commands to manage it:"
echo "  restart-datagram                         # Restart service"
echo "  status-datagram                          # Check online/offline and connection status"
echo "  sudo journalctl -u datagram.service -f   # View live logs"
echo "  sudo bash datagram-installer.sh --uninstall  # Uninstall all components"
echo "----------------------------------------"
