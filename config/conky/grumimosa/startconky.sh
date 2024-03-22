#!/bin/bash

killall conky
sleep 3s
		
#conky -c $HOME/.conky/Edasich/Edasich.conf &> /dev/null &
conky -c $HOME/.conky/grumimosa/Mimosa.conf &> /dev/null &
