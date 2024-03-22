#!/bin/bash

killall conky
sleep 2s
		
conky -c $HOME/.config/conky/grumimosa/Mimosa.conf &> /dev/null &
conky -c $HOME/.config/conky/grumimosa/Grumium2.conf &> /dev/null &
