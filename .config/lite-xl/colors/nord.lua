local style = require "core.style"
local common = require "core.common"
local config = require "core.config"

style.background = { common.color "#2E3440" }
style.background2 = { common.color "#2E3440" }
style.background3 = { common.color "#3B4252" }
style.text = { common.color "#D8DEE9" }
style.caret = { common.color "#D8DEE9" }
style.accent = { common.color "#88C0D0" }
style.dim = { common.color "#d8dee966" }
style.divider = { common.color "#3B4252" }
style.selection = { common.color "#616E88CC" }
style.line_number = { common.color "#4C566A" }
style.line_number2 = { common.color "#D8DEE9" }
style.line_highlight = { common.color "#3B4252" }
style.scrollbar = { common.color "#434c5eaa" }
style.scrollbar2 = { common.color "#434c5e" }
style.good = { common.color "#72b886cc" }
style.warn = { common.color "#d08770" }
style.error = { common.color "#bf616a" }
style.modified = { common.color "#ebcb8b" }

style.syntax["normal"] = { common.color "#ECEFF4" }
style.syntax["symbol"] = { common.color "#D8DEE9" }
style.syntax["comment"] = { common.color "#616E88" }
style.syntax["keyword"] = { common.color "#81A1C1" }
style.syntax["keyword2"] = { common.color "#81A1C1" }
style.syntax["number"] = { common.color "#B48EAD" }
style.syntax["literal"] = { common.color "#81A1C1" }
style.syntax["string"] = { common.color "#A3BE8C" }
style.syntax["operator"] = { common.color "#81A1C1" }
style.syntax["function"] = { common.color "#88C0D0" }

config.highlight_current_line = "no_selection"

style.guide = { common.color "#434c5eb3" }
style.bracketmatch_color = { common.color "#8fbcbb" }

