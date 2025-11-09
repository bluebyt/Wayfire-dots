-- mod-version:3.1
local core = require "core"
local config = require "core.config"
local common = require "core.common"
local command = require "core.command"
local keymap = require "core.keymap"

local recent_files = {}
local recent_files_path = USERDIR .. PATHSEP .. "recent_files.lua"

-- Load previous recent files and set the config table
local files_recent = io.open(recent_files_path, "r")
if files_recent then
  recent_files = load(files_recent:read("*a"))()
  files_recent:close()
end

---@class config.plugins.recentfiles
---Maximum amount of recent files to store.
---@field max_recent_files integer
config.plugins.recentfiles = common.merge({
  max_recent_files = 100,
  config_spec = {
    name = "Recent Files",
    {
      label = "Maximum Files",
      description = "The maximum amount of recent files to store.",
      path = "max_recent_files",
      type = "number",
      default = 100,
      min = 1,
      on_apply = function(max_files)
        while #recent_files > max_files do
          table.remove(recent_files, #recent_files)
        end
      end
    }
  }
}, config.plugins.recentfiles)

---Inserts the given value at the top of the table and removes any duplicates.
---@param t table Target table
---@param v string Value to insert
local function insert_unique(t, v)
  local n = #t
  for i = 1, n do
    if t[i] == v then
      table.remove(t, i)
      break
    end
  end
  table.insert(t, 1, v)
end

-- Add opened files to recent files list
local core_open_doc = core.open_doc
core.open_doc = function(filename)
  ---@type core.doc
  local doc = core_open_doc(filename)
  if doc.abs_filename then
    local file = io.open(doc.abs_filename, "r")
    if file then
      file:close()
      local file_path = common.home_encode(doc.abs_filename)
      insert_unique(recent_files, file_path)
      while #recent_files > config.plugins.recentfiles.max_recent_files do
        table.remove(recent_files, #recent_files)
      end
    end
  end
  return doc
end

-- Save recent files list on program quit
local core_run = core.run
core.run = function()
  core_run()
  if #recent_files > 0 then
    local file = io.open(recent_files_path, "w+")
    if file then
      file:write("return ", common.serialize(recent_files, {pretty = true}))
      file:close()
    end
  end
end

-- Register command and default keymap
command.add(function() return #recent_files > 0 end, {
  ["core:open-recent-file"] = function()
    core.command_view:enter("Open Recent File", {
      submit = function(text, item)
        text = item and item.text or text
        core.root_view:open_doc(core.open_doc(common.home_expand(text)))
      end,
      suggest = function(text)
        if not text or text == "" then return recent_files end
        return common.fuzzy_match(recent_files, text, true)
      end,
    })
  end,

  ["core:open-recent-file-clear"] = function()
    recent_files = {}
    os.remove(recent_files_path)
  end,
})

keymap.add({
  ["alt+o"] = "core:open-recent-file"
})


return recent_files

