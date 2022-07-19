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

    name = 'cpu', arg = 'cpu', max = 1,
    bg_colour = 0x111111, bg_alpha = 0,
    fg_colour = 0x111111, fg_alpha = 0.6,
    x = 35, y = 35,
    radius = 32, thickness = 6,
    start_angle = 0, end_angle = 360

}

function conky_main()
    if conky_window == nil then
        return
    end
    local cs = cairo_xlib_surface_create(conky_window.display,
        conky_window.drawable,
        conky_window.visual,
        conky_window.width,
        conky_window.height)
    cr = cairo_create(cs)
    local updates = tonumber(conky_parse('${updates}'))
    if updates > 10 then
        --print ("conky_main counted >5 updates to its window")
        draw_simple_ring(cr)
    end
    cairo_destroy(cr)
    cairo_surface_destroy(cs)
    cr = nil
end

function draw_text(cr)
    cairo_select_font_face(cr, font, font_slant, font_face);
    cairo_set_font_size(cr, font_size)
    cairo_set_source_rgba(cr, red, green, blue, alpha)
    cairo_move_to(cr, xpos, ypos)
    cairo_show_text(cr, text)
    cairo_stroke(cr)

end

function draw_simple_ring(cr)
    local w, h = conky_window.width, conky_window.height
    local ring_center = { x = w / 2, y = 117 }
    local ring_radius = 110
    local ring_width = 3

    -- blue
    local ring_battery_color = { r = 59 / 255, g = 205 / 255, b = 252 / 255, a = 1 }
    -- white
    local ring_outer_color = { r = 1, g = 1, b = 1, a = 1 }

    -- Indicator value settings.
    local value = conky_parse("${battery_percent}")
    local max_value = 100
    cairo_set_line_width(cr, ring_width)

    -- Outer ring
    cairo_set_source_rgba(cr, ring_outer_color.r, ring_outer_color.g, ring_outer_color.b, ring_outer_color.a)
    cairo_arc(cr, ring_center.x, ring_center.y, ring_radius + 5, 0, 2 * math.pi)
    cairo_stroke(cr)
    -- Battery ring
    cairo_set_source_rgba(cr, ring_battery_color.r, ring_battery_color.g, ring_battery_color.b, ring_battery_color.a)
    cairo_arc(cr, ring_center.x, ring_center.y, ring_radius, 0, 2 * math.pi / max_value * value)
    cairo_stroke(cr)
end
