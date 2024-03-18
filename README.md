# Wayfire-dots
Wayfire is a 3D Wayland compositor
Warning: This installation guide is for my future self. Some steps might not be completed.


![Nordcity9mars](https://github.com/bluebyt/Wayfire-dots/assets/18442224/4cab8d3d-9370-4257-abf9-a33cd1dcdb94)

![screenshotNordgithubnouveau2](https://github.com/bluebyt/Wayfire-dots/assets/18442224/9704b05f-0a7c-4abe-9ac4-0be1d0f57134)

[Install Wayfire on Youtubes](https://youtu.be/abtU54uMXH0)

## Details
- [Wayfire](https://github.com/WayfireWM/wayfire) is a 3D wayland compositor
- [Ironbar](https://github.com/JakeStanger/ironbar) A customisable and feature-rich GTK bar for wlroots compositors, written in Rust.
- [Waybar](https://github.com/Alexays/Waybar) Customizable Wayland bar
- [eww](https://github.com/elkowar/eww) Widget on the left
- [Mako](https://github.com/emersion/mako) notification
- [Graphite-gtk-theme](https://github.com/vinceliuice/Graphite-gtk-theme) command: ./install.sh -c dark -l --tweaks nord
- [Tela-circle-icon-theme](https://github.com/vinceliuice/Tela-circle-icon-theme#tela-circle-icon-theme)
- [Fish shell](https://github.com/fish-shell/fish-shell) Command line shell
- [Startship prompt](https://starship.rs/) Customizable prompt
- [nitch](https://github.com/ssleert/nitch) Fast system fetch
- [SwayOSD](https://github.com/ErikReider/SwayOSD) A OSD window for common actions like volume and capslock.
- [Text editor](https://apps.gnome.org/TextEditor/) The new text editor for Gnome. Command to install the custom Nord theme : $sudo cp nord.xml /usr/share/gnome-text-editor/styles/
- [Ulauncher](https://ulauncher.io/) Application launcher for Linux
- [Grimshot-pv](https://github.com/ferdiebergado/grimshot-pv) Script with added screenshot preview on the notification
- [Xava](https://github.com/nikp123/xava#programming-opengl-shaders) Audio Visualizer
- [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) Terminal Music player
- [G4music](https://github.com/neithern/g4music) Music player
- Caskaydiacove nerd font 

## Workflow
- [Video on Youtubes](https://youtu.be/NwBcCH1cJRI)

## Install steps
- [Install Archlinux Gnome desktop](https://www.youtube.com/watch?v=3ndsDxlkTrw)
  
## Dependencies for Archlinux
```
sudo pacman -S freetype2 glm libdrm libevdev libgl libinput libjpeg libpng libxkbcommon libxml2 pixman wayland-protocols wlroots meson cmake doctest doxygen nlohmann-json libnotify base-devel pkg-config autoconf gobject-introspection gtk-layer-shell scour
```

## Install scripts
```
git clone https://github.com/WayfireWM/wf-install
cd wf-install
./install.sh --prefix /opt/wayfire --stream master
```

## Configuration
- Edit $HOME/.config/wayfire.ini
- Edit $HOME/.config/wf-shell.ini


## Running
- Log out and select Wayfire in GNOME Display Manager (GDM) then log back in.

## Follow focus and inactive-alpha
-Set environment variable ~/.config/environment.d/environment.conf
```
WAYFIRE_SOCKET=/tmp/wayfire-wayland-1.socket
```
- Copy the script from here [inactive-alpha.py](https://github.com/WayfireWM/wayfire/tree/master/ipc-scripts) and wayfire_socket.py to the same directory somewhere.
- Example ~/.config/ipc-scripts/*.py
- Edit and add to $HOME/.config/wayfire.ini the following two line 
- plugins = ipc ipc-rules follow-focus (ipc must be first)
- [autostart] launcher = ~/.config/ipc-scripts/inactive-alpha.py
![output](https://github.com/bluebyt/Wayfire-dots/assets/18442224/7d4a0a2a-c415-488a-8063-2e72946b823a)
