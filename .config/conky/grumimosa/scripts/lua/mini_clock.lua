--[[
minimal clock for conky
based upon similar android clock widget

written by easysid
Tuesday, 03 February 2015 16:20 IST

edited by Etles_Team
Friday, 17 August 2016 21:08 WITA

To call this conky, Add this command before "TEXT" in conkyrc file:

   lua_load ~/.conky/Conky-Name/scripts/lua/min_clock.lua
   lua_draw_hook_pre main
   OR
   lua_draw_hook_post main

TEXT

]]

require 'cairo'

clock_table = {
-- clock style options
use12hourformat = false, -- 12 hr format. Set to false for 24 hrs
draw_background = false, -- set to false if you do not want a bg fill
draw_seconds    = true, -- draw the seconds ring

-- Options if above is true
seconds_ring_width       = 10,               -- seconds ring width
seconds_ring_base_color  = {0xFFFFFF, 0.8}, -- base color
seconds_ring_fill_color  = {0xFFFFFF, 0.1}, -- fill color
seconds_ring_fill_colorS = {0xFFFFFF, 0.1},

-- Main settings
xc = 125, -- centre of the clock
yc = 125,
R  = 110, -- default radius of the clock
RH = 0,  -- outher radius for hours fill ring
RM = 0,  -- outer radius for minutes fill ring
rh = 0,  -- hour ring fill raius
rm = 0,  -- minutes ring fill radius
rs = 11,  -- seconds ring fill radius
border_width = 0, -- radius border fill ring

-- Color settings. {color, alpha}
background_color = {0x2F2F2F, 0.6}, -- bgcolor id draw_background is true.
fill_color       = {0x225588, 1},   -- fill color for hour+minutes ring
fill_colorS      = {0x2F2F2F, 1},   -- fill color for seconds ring
border_colorS    = {0xFFDCDC, 1},   -- border color for seconds fill ring
border_color     = {0xFFFFFF, 1},   -- border color for hours+minutes
text_color       = {0x000000, 0},   -- color of numbers
text_colorS      = {0xEEFFFF, 0},   -- color for text seconds inside fill ring

-- Font settings, Specify the font as font:face, where face is bold, italic, bolditalic
hour_font = "Lion", hour_font_size = 11, -- font face+size for hours
min_font  = "Lion", min_font_size  = 11, -- font face+size for minutes
sec_font  = "Lion", sec_font_size  = 11, -- font face+size for seconds
day_font  = "Lion", day_font_size  = 12, -- font face+size for the day
}
-----------------------------------------------------------------------------------------------------------------------------------------------
--
-- Main function to load script
function conky_main()
if conky_window == nil then return end
local cs = cairo_xlib_surface_create(conky_window.display, conky_window.drawable, conky_window.visual, conky_window.width, conky_window.height)
cr = cairo_create(cs)
draw_clock(cr, clock_table)
end -- end main function
-----------------------------------------------------------------------------------------------------------------------------------------------
--
-- The primary function to draw the clock
function draw_clock(cr, t)
-- Hours
local divh = 12
local hour = tonumber(os.date("%I"))
local h_theta = hour*2*math.pi/divh - math.pi/2
local xh = t.xc + t.RH*math.cos(h_theta)
local yh = t.yc + t.RH*math.sin(h_theta)

-- Minutes
local divm = 60   
local minutes = tonumber(os.date("%M"))
local m_theta = minutes*2*math.pi/divm - math.pi/2 -- calculate the angle
local xm = t.xc + t.RM*math.cos(m_theta)
local ym = t.yc + t.RM*math.sin(m_theta)
    
-- Get font and font face hours + minutes
local dfont, dface = splitfont(t.day_font)
local hfont, hface = splitfont(t.hour_font)
local mfont, mface = splitfont(t.min_font)

-- Print calculate text extents
if t.use12hourformat then
hy = getheight(hour,t.hour_font, 'normal', t.hour_font_size)
end

-- Draw the outer ring
if t.draw_background then
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.background_color))
cairo_arc(cr, t.xc, t.yc, t.R, 0, 2*math.pi)
cairo_fill(cr)
end

-- The primary function to draw the clock if draw seconds
if t.draw_seconds then
local divs = 60
local seconds = tonumber(os.date("%S"))
local s_theta = seconds*2*math.pi/divs - math.pi/2 -- calculate the angle
local xs = t.xc + t.R*math.cos(s_theta)
local ys = t.yc + t.R*math.sin(s_theta)
local sfont, sface = splitfont(t.sec_font)

cairo_set_line_width(cr, t.seconds_ring_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_base_color))

-- Draw the base ring for seconds
cairo_arc(cr, t.xc, t.yc, t.R, 0, 2*math.pi)
cairo_stroke(cr)

-- Draw the seconds indicator circle
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_fill_colorS))
cairo_arc(cr, t.xc, t.yc, t.R, -math.pi/2, s_theta)
cairo_stroke(cr)

-- Draw the seconds ring fill
cairo_set_line_width(cr, t.border_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.fill_colorS))
cairo_arc(cr, xs, ys, t.rs, 0, 2*math.pi)
cairo_fill(cr)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.border_colorS))
cairo_arc(cr, xs, ys, t.rs, 0, 2*math.pi)
cairo_stroke(cr)

-- Output text for seconds
out({x=xs,y=ys,f=sfont,face=sface,fs=t.sec_font_size,c=t.text_colorS,txt=seconds,hj='c',vj='m'})
else
cairo_set_line_width(cr, t.border_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.border_color))
cairo_arc(cr, t.xc, t.yc, t.R, 0, 2*math.pi)
cairo_stroke(cr)
end
------------------------------------------------------------------------------------------------
--
-- Hours
cairo_set_line_width(cr, t.seconds_ring_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_base_color))

-- Draw the base ring for hours
cairo_arc(cr, t.xc, t.yc, t.RH, 0, 2*math.pi)
cairo_stroke(cr)

-- Draw the hours indicator circle
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_fill_color))
cairo_arc(cr, t.xc, t.yc, t.RH, -math.pi/2, h_theta)
cairo_stroke(cr)

-- Draw the hours ring fill
cairo_set_line_width(cr, t.border_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.fill_color))
cairo_arc(cr, xh, yh, t.rh, 0, 2*math.pi)
cairo_fill(cr)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.border_color))
cairo_arc(cr, xh, yh, t.rh, 0, 2*math.pi)
cairo_stroke(cr)
---------------------------------------------------------------------
--
-- Minutes
cairo_set_line_width(cr, t.seconds_ring_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_base_color))

-- Draw the base ring minutes
cairo_arc(cr, t.xc, t.yc, t.RM, 0, 2*math.pi)
cairo_stroke(cr)

-- Draw the minutes indicator circle
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.seconds_ring_fill_color))
cairo_arc(cr, t.xc, t.yc, t.RM, -math.pi/2, m_theta)
cairo_stroke(cr)

-- Draw the minutes ring fill
cairo_set_line_width(cr, t.border_width)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.fill_color))
cairo_arc(cr, xm, ym, t.rm, 0, 2*math.pi)
cairo_fill(cr)
cairo_set_source_rgba(cr, rgba_to_r_g_b_a(t.border_color))
cairo_arc(cr, xm, ym, t.rm, 0, 2*math.pi)
cairo_stroke(cr)
---------------------------------------------------------------------
--
-- Check the time format
if t.use12hourformat then
hour = tonumber(os.date("%H"))
local ampm = os.date("%p")
-- Output text for the day
out({x=t.xc,y=t.yc+8,f=dfont,face=dface,fs=t.day_font_size,c=t.text_color,txt=ampm,hj='c',vj='n'})
end
-- Output text for hours
out({x=xh,y=yh,f=hfont,face=hface,fs=t.hour_font_size,c=t.text_color,txt=hour,hj='c',vj='m'})
-- Output text for
out({x=xm,y=ym,f=mfont,face=mface,fs=t.min_font_size,c=t.text_color,txt=minutes,hj='c',vj='m'})
end -- end draw_clock

function out(txj)
-- Taken from mrpeachy's wun.lua
local extents=cairo_text_extents_t:create()
tolua.takeownership(extents)
local function justify(jtxt,x,hj,y,vj,f,face,fs)
if face=="normal" then
face={f,CAIRO_FONT_SLANT_NORMAL,CAIRO_FONT_WEIGHT_NORMAL}
elseif face=="bold" then
face={f,CAIRO_FONT_SLANT_NORMAL,CAIRO_FONT_WEIGHT_BOLD}
elseif face=="italic" then
face={f,CAIRO_FONT_SLANT_ITALIC,CAIRO_FONT_WEIGHT_NORMAL}
elseif face=="bolditalic" then
face={f,CAIRO_FONT_SLANT_ITALIC,CAIRO_FONT_WEIGHT_BOLD}
else
print ('face not set correctly - "normal","bold","italic","bolditalic"')
end

cairo_select_font_face (cr,face[1],face[2],face[3])
cairo_set_font_size(cr,fs)
cairo_text_extents(cr,jtxt,extents)
local wx=extents.x_advance
local wd=extents.width
local hy=extents.height
local bx=extents.x_bearing
local by=extents.y_bearing+hy
local tx=x
local ty=y

-- Set horizontal alignment - l, c, r
if hj=="l" then x=x-bx
elseif hj=="c" then x=x-((wx-bx)/2)-bx
elseif hj=="r" then x=x-wx
else
print ("hj not set correctly - l, c, r")
end

-- vj. n=normal, nb=normal-ybearing, m=middle, mb=middle-ybearing, t=top
if vj=="n" then
y=y
elseif vj=="nb" then
y=y-by
elseif vj=="m" then
y=y+((hy-by)/2)
elseif vj=="mb" then
y=y+(hy/2)-by
elseif vj=="t" then
y=y+hy-by
else
print ("vj not set correctly - n, nb, m, mb, t")
end
return face,fs,x,y,rad,rad2,tx,ty
end -- justify local function

-- Set variables
local c=txj.c 	 or {0xffffff, 1}
local a=txj.a 	 or 1
local f=txj.f 	 or "Mono"
local fs=txj.fs 	 or 12
local x=txj.x 	 or 100
local y=txj.y 	 or 100
local txt=txj.txt 	 or "text"
local hj=txj.hj 	 or "l"
local vj=txj.vj 	 or "n"
local face=txj.face	 or "normal"
    
-- Print text
local face,fs,x,y=justify(txt,x,hj,y,vj,f,face,fs)
cairo_select_font_face (cr,face[1],face[2],face[3])
cairo_set_font_size(cr,fs)
cairo_move_to (cr,x,y)
cairo_set_source_rgba (cr,rgba_to_r_g_b_a(c))
cairo_show_text (cr,txt)
cairo_stroke (cr)
return nx
end -- function out

function rgba_to_r_g_b_a(tcolor)
local color,alpha=tcolor[1],tcolor[2]
return ((color / 0x10000) % 0x100) / 255., ((color / 0x100) % 0x100) / 255., (color % 0x100) / 255., alpha
end -- end rgba

function getheight(txt,f,face,fs)
-- Return the height of text. Needed for proper placement
local extents=cairo_text_extents_t:create()
tolua.takeownership(extents)
if face=="normal" then
face={f,CAIRO_FONT_SLANT_NORMAL,CAIRO_FONT_WEIGHT_NORMAL}
elseif face=="bold" then
face={f,CAIRO_FONT_SLANT_NORMAL,CAIRO_FONT_WEIGHT_BOLD}
elseif face=="italic" then
face={f,CAIRO_FONT_SLANT_ITALIC,CAIRO_FONT_WEIGHT_NORMAL}
elseif face=="bolditalic" then
face={f,CAIRO_FONT_SLANT_ITALIC,CAIRO_FONT_WEIGHT_BOLD}
else
print ('face not set correctly - "normal","bold","italic","bolditalic"')
end
cairo_select_font_face (cr,face[1],face[2],face[3])
cairo_set_font_size(cr,fs)
cairo_text_extents(cr,txt,extents)
return extents.height
end -- end getheight

function splitfont(s)
-- Return font and face
if s:find(':') then
return s:match("([^:]+):([^:]+)")
else
return s, nil
end
end -- end splitfont

function cairo_cleanup()
cairo_destroy(cr)
cairo_surface_destroy(cs)
collectgarbage()
cr,cs=nil
end -- cleanup
--======================= Regards, Etles_Team =============================
