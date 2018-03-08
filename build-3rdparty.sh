#!/bin/bash

# general
root_directory=$(pwd)
project_directory=$root_directory/xylophone
sources_directory=$root_directory/thirdparty

# python
python_source=$sources_directory/cpython
python_target=$project_directory/python

# pygame
pygame_source=$sources_directory/pygame
pygame_target=$project_directory/pygame

#==============================
echo "cleaning"

if [ -d $pygame_target ]; then
    rm -rf $pygame_target
fi

if [ -d $python_target ]; then
    rm -rf $python_target
fi

#===============================
echo "============"
echo "Build python"
echo "============"

cd $python_source
./configure --enable-optimization
make

# ------------------
mkdir $python_target
python_files=(python pybuilddir.txt libpython* Modules Lib build)

for f in "${python_files[@]}"; do
    cp -r $f $python_target
done

#===============================
echo "============"
echo "Build pygame"
echo "============"
sleep 1

cd $pygame_source
python setup.py build

# ------------------
mkdir $pygame_target
cd build/lib.linux*
cp -r pygame/* $pygame_target

cd $rootdir
