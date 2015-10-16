#!/bin/bash
mkdir /tmp/.brainteaser
cp -arvf * /tmp/.brainteaser
cp -arvf /tmp/.brainteaser/ ~/
chmod 755 ~/.brainteaser/main.py
echo "PATH=$PATH:~/.brainteaser/" >>~/.bashrc
echo "alias braint='python ~/.brainteaser/main.py'">> ~/.bashrc
rm -rvf /tmp/.brainteaser
echo ""
echo ""
echo "   >>installed<<"
echo " restart terminal"
echo ' use cmd " braint " '


