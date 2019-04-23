#!/bin/bash

set -e

python3 -u ./vanilla_gan.py 1> log/vanilla_gan.out &
python3 -u ./cycle_gan.py 1> log/cycle_gan.out &

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

echo "Training."

wait

echo "done."
