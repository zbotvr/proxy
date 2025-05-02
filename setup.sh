

echo "Setting up environment..."

pkg update -y && pkg upgrade -y 2>/dev/null || sudo apt update -y && sudo apt upgrade -y

pkg install python -y 2>/dev/null || sudo apt install python3-pip -y

pkg install git -y 2>/dev/null || sudo apt install git -y

pip install flask gunicorn requests beautifulsoup4 html5lib

echo "Setup complete."