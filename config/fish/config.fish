set fish_greeting
#neofetch --off --block_range 0 7
#neofetch
#neofetch --block_range 0 7
#alias c="clear; neofetch --off --block_range 0 7"
#neofetch --config ~/.config/neofetch/config_def.conf
alias c="neofetch --block_range 0 7"
#alias c="neofetch --kitty ~/Pictures/Nord/unsplash20.png"
nitch
alias n='nitch'
#alias c="clear; neofetch --block_range 0 7"
#export PATH="$"PATH":/home/bluebyt/.local/bin"
set -x PATH $PATH ~/.local/bin
set -x PATH $PATH ~/.local/bin/eww
set -x PATH $PATH ~/.local/bin/go/bin/
set -x PATH $PATH ~/.cargo/bin
alias work='$HOME/.bin/cleanup_after_start.sh'
alias update='sudo pacman -Syu'
alias pipe='$HOME/Active/color-scripts/color-scripts/./pipes2'
alias unlock='sudo rm /var/lib/pacman/db.lck'    # remove pacman lock
alias play='ncmpcpp'
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias pacmandir='pacman -Ql' #To retrieve a list of the files installed by a package
alias pacmanR='pacman -Rs' #To remove a package and its dependencies
alias pacmanQ='pacman -Qs' #To search for already installed packages
alias pacmanQi='pacman -Qi' #To display information about locally installed packages
alias unlock='sudo rm /var/lib/pacman/db.lck'    # remove pacman lock
alias cleanup='sudo pacman -Rns (pacman -Qtdq)'  # remove orphaned packages
alias clean='sudo pacman -Sc' #removing old packages from cache
#alias extract='for i in *.rar; do unrar x -o+ "$i"; end' 
. ~/.config/fish/functions/noti.fish
starship init fish | source
