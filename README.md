# Wayfire-dots
Wayfire is a 3D Wayland compositor
## Warning 
- This guide is for Archlinux and it doesn't provide any installer. Some steps might not be completed.

- The ```bin``` and ```config``` folders are not preceded by a dot, as they should be. However,
  since GitHub does not support dragging files with a dot prefix (hidden files), they must be added manually.

- For more information, please refer to the Wayfire wiki [Wayfire wiki](https://github.com/WayfireWM/wayfire/wiki)
## Screenshot with Pixdecor
![screenshot_wayfire_2_dec_2024ver2](https://github.com/user-attachments/assets/6ce465da-e8a9-45d5-a87c-8932cd7ae366)

## Screenshot with a mix of GTK4 apps and Pixdecor 
![GTK4_pixdecor](https://github.com/user-attachments/assets/58606e37-6f79-4ad9-b1cf-20cef66b1213)


[Install Wayfire on Youtubes](https://youtu.be/abtU54uMXH0)

## Details
- [Wayfire](https://github.com/WayfireWM/wayfire) is a 3D wayland compositor
- [Pixdecor](https://github.com/soreau/pixdecor) Decorator plugin for wayfire, pixdecor features antialiased rounded corners with shadows and optional animated effects.
- [Ironbar](https://github.com/JakeStanger/ironbar) A customisable and feature-rich GTK bar for wlroots compositors, written in Rust.
- [eww](https://github.com/elkowar/eww) Widget on the left
- [Mako](https://github.com/emersion/mako) notification
- [Tokyonight-Dark](https://github.com/Fausto-Korpsvart/Tokyo-Night-GTK-Theme) command: ./install.sh -d ~/.local/share/themes -c dark -l --tweaks black
- [Tela-circle-icon-theme](https://github.com/vinceliuice/Tela-circle-icon-theme#tela-circle-icon-theme) or [Aretha-Dark-Icons](https://www.gnome-look.org/p/2180417) 
- [Fish shell](https://github.com/fish-shell/fish-shell) Command line shell
- [Startship prompt](https://starship.rs/) Customizable prompt
- [Catnip](https://github.com/iinsertNameHere/catnip) A minimalistic and fast system fetch
- [SwayOSD](https://github.com/ErikReider/SwayOSD) A OSD window for common actions like volume and capslock.
- [Lite XL](https://lite-xl.com/) A lightweight, simple, fast, feature-filled, and extremely extensible text editor
- [Ulauncher](https://ulauncher.io/) Application launcher for Linux
- [Grimshot-pv](https://github.com/ferdiebergado/grimshot-pv) Script with added screenshot preview on the notification
- [Xava](https://github.com/nikp123/xava#programming-opengl-shaders) Audio Visualizer
- [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) Terminal Music player
- [Swappy](https://github.com/jtheoof/swappy) A Wayland native snapshot and editor tool
- Caskaydiacove nerd font

## Workflow
- [Video on Youtubes](https://youtu.be/5dzgKCZbSlA)

## Install steps
- [Install Archlinux Gnome desktop](https://youtu.be/5dzgKCZbSlA)
(It is not necessary to install GNOME if you want a minimal desktop; you should look for an alternative method.)
  
## Dependencies for Archlinux
```
sudo pacman -S freetype2 glm libdrm libevdev libgl libinput libjpeg libpng libxkbcommon libxml2 pixman wayland-protocols wlroots meson cmake doctest doxygen nlohmann-json libnotify base-devel pkg-config autoconf gobject-introspection gtk-layer-shell scour libdbusmenu-gtk3 gtkmm3 glib2-devel boost
```

## Install the latest Wayfire with the scripts
```
git clone https://github.com/WayfireWM/wf-install
cd wf-install
./install.sh --prefix /opt/wayfire --stream master
```
## Install Pixdecor
```
git clone https://github.com/soreau/pixdecor.git
cd pixdecor
PKG_CONFIG_PATH=/opt/wayfire/lib/pkgconfig meson setup build --prefix=/opt/wayfire
ninja -C build
ninja -C build install
```
## Configuration
- Edit $HOME/.config/wayfire.ini
- Edit $HOME/.config/wf-shell.ini


## Running
- Log out and select Wayfire in GNOME Display Manager (GDM) then log back in.

## Follow focus and inactive-alpha
-Create the file and set environment variable ~/.config/environment.d/environment.conf
```
WAYFIRE_SOCKET=/tmp/wayfire-wayland-1.socket
```
- Copy the script from here [inactive-alpha.py](https://github.com/WayfireWM/pywayfire/tree/main/scripts) and wayfire_socket.py to the same directory somewhere.
- Example ~/.config/ipc-scripts/*.py
- Edit and add to $HOME/.config/wayfire.ini the following two line 
- plugins = ipc ipc-rules follow-focus (ipc must be first)
- [autostart] launcher = ~/.config/ipc-scripts/inactive-alpha.py
![output](https://github.com/bluebyt/Wayfire-dots/assets/18442224/7d4a0a2a-c415-488a-8063-2e72946b823a)
