#!/bin/bash
cd "/home/calum/Documents/Coding/Deluge Work/deluge/deluge/plugins/ipstatusbar"
mkdir temp
export PYTHONPATH=./temp
python setup.py build develop --install-dir ./temp
cp ./temp/IPstatusbar.egg-link /home/calum/.config/deluge/plugins
rm -fr ./temp
