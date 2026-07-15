#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Root access needed"
   exit 1
fi

path="/usr/lib/Blackjack"
bin_path="/usr/local/bin"

if [[ -d $path ]]; then
  sudo rm -rf $path
  echo "Game file deleted from $path"
else
  echo "Game not found at $path"
fi

if [[ -d $bin_path ]]; then
  sudo rm $bin_path/blackjack
  echo "Bin file deleted from $bin_path"
else
  echo "Bin file not found at $bin_path/blackjack"
fi
