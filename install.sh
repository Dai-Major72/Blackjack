#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Root access needed"
   exit 1
fi

path="/usr/lib/Blackjack"
bin_path="/usr/local/bin"

if [[ -d $path ]]; then
  echo "Game found and updated"
else
  sudo mkdir -p $path
fi

sudo cp blackjack.py bj_cards.py $path

if [[ -e $bin_path/blacjack ]]; then
  echo "Bin file already exist"
else
  mkdir -p $bin_path
fi

ln -s $path/blackjack.py $bin_path/blackjack

sudo chmod +x $path/blackjack.py
