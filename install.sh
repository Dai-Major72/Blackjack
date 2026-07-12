#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Nécessite root"
   exit 1
fi

path="/usr/lib/Blackjack"
bin_path="/usr/local/bin"

if [[ -d $path ]]; then
  echo "Creation fichier lib"
else
  sudo mkdir -p $path
fi

sudo cp blackjack.py modules.py $path

if [[ -d $bin_path ]]; then
  echo "Création fichier bin"
else
  mkdir -p $bin_path
fi

ln -s $path/blackjack.py $bin_path/blackjack

sudo chmod +x $path/blackjack.py