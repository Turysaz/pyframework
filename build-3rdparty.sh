#!/bin/bash

rootdir=$(pwd)
pybindir=$rootdir/pygamework/python
pygamedir=$rootdir/pygamework/pygame

cd thirdparty

echo "Build python"
echo "============"
sleep 1

cd cpython
./configure --enable-optimization
make
cp python $pybindir/
cp pybuilddir.txt $pybindir/
cp libpython* $pybindir/
cp -r Modules $pybindir/
cp -r Lib $pybindir/
cp -r build $pybindir/

cd ..

echo "done."
echo 
echo "Build pygame"
echo "============"
sleep 1

cd pygame
python setup.py build
cd build/lib.linux*
cp -r pygame $pygamedir

cd $rootdir

