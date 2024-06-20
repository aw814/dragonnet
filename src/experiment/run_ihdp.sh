#!/usr/bin/env bash


options=(
    dragonnet
    tarnet

)



for i in ${options[@]}; do
    echo $i
    python -m experiment.ihdp_main --data_base_dir /Users/anniewang/Desktop/dragonnet/dat/ihdp/csv\
                                 --knob $i\
                                 --output_base_dir /Users/anniewang/Desktop/dragonnet/result/ihdp\


done