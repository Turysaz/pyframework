#!/bin/bash
# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

drelease=release

if [ -d $drelease]; then
    rm -rf $drelease
fi

mkdir $drelease
cp -r project $drelease/  # actual game content
cp -r python $drelease/   # interpreter executable
cp -r pygame $drelease/   # pygame library
cp -r pgw $drelease/      # framework code

cp configuration.txt $drelease/ # game init configuration
cp launcher.py $drelease/       # python root file
cp start.sh $drelease/          # linux start script
