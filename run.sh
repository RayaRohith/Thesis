#!/bin/bash

VISITS=100

rm -rf results
mkdir -p results

for i in {0..99}; do
	while read url; do
        python main.py $i https://$url
		killall -9 dumpcap
		killall -9 python
    done <../url.list
done
