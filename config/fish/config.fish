set fish_greeting
# source ~/.config/lscolors.csh
# Set up fzf key bindings

#neofetch --off --block_range 0 7
#neofetch
#neofetch --block_range 0 7
alias c="clear"
# alias c="clear; neofetch --off --block_range 0 7"
# neofetch --config ~/.config/neofetch/config_def.conf
# alias c="neofetch --block_range 0 7"
# alias c="neofetch --kitty ~/Pictures/Nord/unsplash20.png"
# nitch
alias n='nitch'
alias fox='catnip -c ~/.config/catnip/config_fox.toml'
alias fox2='catnip -c ~/.config/catnip/config_fox2.toml'
alias fox3='catnip -c ~/.config/catnip/config_fox3.toml'

# alias ls='lsd -a'
# alias ll='lsd -ahl'
alias icat='kitten icat'
alias cat='catnip' 
catnip
export LS_COLORS="*.ini=31:*.ttf=36:*.toml=35"
alias ls='exa --icons -a'
alias ll='exa --icons -ahl'
alias exa1='exa --tree --level=1'
alias exa2='exa --tree --level=2'
alias exa3='exa --tree --level=3'

#alias c="clear; neofetch --block_range 0 7"
#export PATH="$"PATH":/home/bluebyt/.local/bin"
set -x PATH $PATH ~/.bin
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
#. ~/.config/fish/functions/noti.fish

set -x STARSHIP_CONFIG ~/.config/starship/starship.toml
starship init fish | source
zoxide init fish | source
fzf --fish | source
