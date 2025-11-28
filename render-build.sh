#!/usr/bin/env bash
set -o errexit

# Update and install tools
apt-get update
apt-get install -y wget gnupg unzip

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb

# Install ChromeDriver matching Chrome major version
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d'.' -f1)
DRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}")
wget "https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver

# Verify installation
google-chrome --version
chromedriver --version
