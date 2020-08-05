#!/bin/sh

for i in $(seq -f "%02g" 1 24)
do
  echo $i
  python convert_wavs.py raw_data/Actor_$i data/Actor_$i
done