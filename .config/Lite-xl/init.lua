-- put user settings here
-- this module will be loaded after everything else when the application starts
-- it will be automatically reloaded when saved

local core = require "core"
local keymap = require "core.keymap"
local config = require "core.config"
local style = require "core.style"
local command = require "core.command"


-- ignore .data/
table.insert(config.ignore_files, "^%.data/")

------------------------------ Themes ----------------------------------------

-- light theme:
-- core.reload_module("colors.summer")
core.reload_module("colors.tokyo-night")

--------------------------- Key bindings -------------------------------------

-- key binding:
-- keymap.add { ["ctrl+escape"] = "core:quit" }

-- pass 'true' for second parameter to overwrite an existing binding
-- keymap.add({ ["ctrl+pageup"] = "root:switch-to-previous-tab" }, true)
-- keymap.add({ ["ctrl+pagedown"] = "root:switch-to-next-tab" }, true)

-- ctrl+shift+t = restore-tabs
-- alt+o = open recent files

------------------------------- Fonts ----------------------------------------

style.font = renderer.font.load("/home/bluebyt/.local/share/fonts/CascadiaCode/CaskaydiaCoveNerdFont-Regular.ttf", 15 * SCALE)
style.code_font = renderer.font.load("/home/bluebyt/.local/share/fonts/CascadiaCode/CaskaydiaCoveNerdFont-Regular.ttf", 15 * SCALE, { antialiasing = "subpixel", hinting="full", bold=false, italic=false, underline=false, smoothing=true, strikethrough=false })

------------------------------ Plugins ----------------------------------------

-- disable plugin detectindent, otherwise it is enabled by default:
-- config.plugins.detectindent = false

config.plugins.minimap = true
config.plugins.selectionhighlight = true
config.plugins.autocomplete = false
config.plugins.linewrapping = { 
  enable_by_default = true, 
  mode = "word", 
  guide = false,
  indent = false,
  }

