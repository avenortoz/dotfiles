-- This is a lua script for use in Conky.
require 'cairo'

font = "Mono"
font_size = 12
text = "hello world"
xpos, ypos = 100, 100
red, green, blue, alpha = 1, 1, 1, 1
font_slant = CAIRO_FONT_SLANT_NORMAL
font_face = CAIRO_FONT_WEIGHT_NORMAL

settings_table = {
    
        name='cpu', arg='cpu', max=1,
      bg_colour=0x111111, bg_alpha=0,
      fg_colour=0x111111, fg_alpha=0.6,
      x=35, y=35,
      radius=32, thickness=6,
      start_angle=0, end_angle=360
    
}

function conky_main ()
    if conky_window == nil then
        return
    end
    local cs = cairo_xlib_surface_create (conky_window.display,
                                         conky_window.drawable,
                                         conky_window.visual,
                                         conky_window.width,
                                         conky_window.height)
    cr = cairo_create (cs)
    local updates = tonumber (conky_parse ('${updates}'))
    if updates > 10 then
        --print ("conky_main counted >5 updates to its window")
        draw_sample_ring(cr)
    end
    cairo_destroy (cr)
    cairo_surface_destroy (cs)
    cr = nil
end

function draw_text(cr)
    cairo_select_font_face (cr, font, font_slant, font_face);
    cairo_set_font_size (cr, font_size)
    cairo_set_source_rgba (cr, red, green, blue, alpha)
    cairo_move_to (cr, xpos, ypos)
    cairo_show_text (cr, text)
    cairo_stroke (cr)

end

function draw_sample_ring(cr)
    -- SETTINGS
    -- rings size
    local w,h=conky_window.width,conky_window.height
    ring_center_x = w/2 
    ring_center_y = 117 
    ring_radius = 110
    ring_width = 3 

    -- Colors.

    -- Set background colors, 1, 0, 0, 1 = fully opaque red.
    ring_bg_red = 1
    ring_bg_green = 0
    ring_bg_blue = 0
    ring_bg_alpha = 1

    -- Set indicator colors, 1, 1, 1, 1 = fully opaque white.
    ring_in_red = 1
    ring_in_green = 1
    ring_in_blue = 1
    ring_in_alpha = 1

    -- Indicator value settings.
    value = conky_parse ("${cpu}")
    max_value = 100

    -- Draw background.
    cairo_set_line_width (cr, ring_width)
    cairo_set_source_rgba (cr, ring_in_red, ring_in_green, ring_in_blue, ring_in_alpha)
    cairo_arc (cr, ring_center_x, ring_center_y, ring_radius, 0, 2 * math.pi)
    cairo_stroke (cr)
end

function draw_ring(cr,t,pt)
   local w,h=conky_window.width,conky_window.height
 
   local xc,yc,ring_r,ring_w,sa,ea=pt['x'],pt['y'],pt['radius'],pt['thickness'],pt['start_angle'],pt['end_angle']
   local bgc, bga, fgc, fga=pt['bg_colour'], pt['bg_alpha'], pt['fg_colour'], pt['fg_alpha']
 
   local angle_0=sa*(2*math.pi/360)-math.pi/2
   local angle_f=ea*(2*math.pi/360)-math.pi/2
   local t_arc=t*(angle_f-angle_0)
 
   -- Draw background ring
 
   cairo_arc(cr,xc,yc,ring_r,angle_0,angle_f)
   cairo_set_source_rgba(cr,rgb_to_r_g_b(bgc,bga))
   cairo_set_line_width(cr,ring_w)
   cairo_stroke(cr)
 
   -- Draw indicator ring
 
   cairo_arc(cr,xc,yc,ring_r,angle_0,angle_0+t_arc)
   cairo_set_source_rgba(cr,rgb_to_r_g_b(fgc,fga))
   cairo_stroke(cr)     
end
