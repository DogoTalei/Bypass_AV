# Bypass_AV
Este script establece una reverse shell multiplataforma (Windows/Linux), desactiva el firewall y el Centro de Seguridad en Windows, oculta la ventana del proceso y redirige la entrada/salida de una shell remota a través de un socket TCP hacia una IP y puerto específicos. Ideal para pruebas en entornos controlados.


# Clone rep
git clone https://github.com/ArtesOscuras/AV_bypass_with_python.git

# Go inside
cd AV_bypass_with_python

# Install dependencies
sudo apt install wine
wget https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
wine python-3.9.0-amd64.exe
wine pip install pyinstaller
sudo apt install osslsigncode
