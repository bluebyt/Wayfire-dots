#! /bin/bash
export SWWW_TRANSITION_FPS=60
export SWWW_TRANSITION_STEP=2     

# swww init

while true;
do

    files=(~/Pictures/*)     
    randomfile=$(printf "%s\n" "${files[RANDOM % ${#files[@]}]}")
    echo $randomfile
swww img --transition-type grow --transition-pos 0.854,0.977  --transition-step 90 "$randomfile"

  sleep 5

done
