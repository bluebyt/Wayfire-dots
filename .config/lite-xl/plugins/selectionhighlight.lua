-- mod-version:3
local style = require "core.style"
local DocView = require "core.docview"
local draw_line_text = DocView.draw_line_text

function DocView:draw_line_text(line, x, y)
  local line1, col1, line2, col2 = self.doc:get_selection(true)
  if line1 == line2 and col1 ~= col2 then
    local selection = self.doc:get_text(line1, col1, line2, col2)
    if not selection:match("^%s+$") then
      local lh = self:get_line_height()
      local selected_text = self.doc.lines[line1]:sub(col1, col2 - 1)
      local current_line_text = self.doc.lines[line]
      local last_col = 1
      while true do
        local start_col, end_col = current_line_text:find(
          selected_text, last_col, true
        )
        if start_col == nil then break end
        -- don't draw box around the selection
        if line ~= line1 or start_col ~= col1 then
          local x2 = x + self:get_col_x_offset(line, end_col + 1)
          if x2 < self.position.x then goto continue end
          local x1 = x + self:get_col_x_offset(line, start_col)
          if x1 > self.position.x + self.size.x then break end
          local color = style.selectionhighlight or style.syntax.comment
          renderer.draw_rect(x1, y, x2 - x1, lh, color)
        end
        ::continue::
        last_col = end_col + 1
      end
    end
  end
  local line_height = draw_line_text(self, line, x, y)
  return line_height
end
