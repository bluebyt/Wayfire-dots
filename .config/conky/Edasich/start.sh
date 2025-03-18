#!/bin/bash

killall conky
sleep 2s
		
# conky -c $HOME/.config/conky/Edasich/Edasich.conf &> /dev/null &
conky -c $HOME/.config/conky/grumosa/Mimosa.conf &> /dev/null &
