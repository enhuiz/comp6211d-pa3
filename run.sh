#!/bin/bash

set -e

python3 -u ./vanilla_gan.py --num_epochs 60 1> log/vanilla_gan.out &
python3 -u ./cycle_gan.py --train_iters 10000 1> log/cycle_gan.out &

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

echo "Training."

wait

echo "done."
