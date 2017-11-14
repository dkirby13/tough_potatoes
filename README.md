Setting up python for windows

First, download Ubunu Linux Emulator here:
https://www.microsoft.com/en-us/store/p/ubuntu/9nblggh4msv6

Then once downloaded open up the command window


Note: all the stuff in blocks below just means type this at the ubuntu command line

Download python on ubuntu:

getting python dependencies:
        sudo apt-get install build-essential checkinstall
        sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
        
downloading python:
    
        version=2.7.13
        cd ~/Downloads/
        wget https://www.python.org/ftp/python/$version/Python-$version.tgz
 
 
 extracting the zip and going to the directory:
 
        tar -xvf Python-$version.tgz
        cd Python-$version
configuring python for your system:
        
        ./configure
        make
        sudo checkinstall  #your sudo password is just your unix password
        
        
getting pygame(the gaming module):
        sudo apt-get install python-pygame
        
getting the github command line interface:
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install git

once you have a github account, let me know and I'll share the directory with you.
clone this directory with this command:

        git clone https://github.com/dkirby13/tough_potatoes.git
        
Then type in your github username and password

If you have any questions either ask me or look it up online. There is a ton of online about this stuff.

