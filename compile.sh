#!/bin/bash

if [ -z "$1" ]; then
    echo "Uso: $0 <archivo_python>"
    exit 1
fi

filename=$(basename -- "$1")
name="${filename%.*}"

wine pyinstaller --onefile --clean --noconsole --icon=icon.ico "$1"
mv "dist/$name.exe" .
rm -rf dist/ build/ "$name.spec"
rm "$name.py"
