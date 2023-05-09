# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from subprocess import Popen


@hook.subscribe.startup_once
def autostart():
    processes = [
        ['feh', '--bg-scale', '/home/avenortoz/Pictures/10.png'],
        # ['blueman-applet'],
        ["xset", "r", "rate", "250", "40"]
    ]
    for p in processes:
        Popen(p)

def get_bar():
    return bar.Bar([
        widget.GroupBox(
            active = "5e81ac",
            inactive = "b48ead",
            this_current_screen_border = "bf616a",
            highlight_method = "line",
            highlight_color=["2e3440", "2e3440"],
            center_aligned=True,
            ),
        widget.Prompt(
            prompt='Run:',
            ),
        widget.TextBox(
            text='|',
            foreground="bf6a6a"
            ),
        widget.Spacer(bar.STRETCH),
        widget.Systray(
            ),
        widget.TextBox(
            text='|',
            foreground="8fbcbb",
            ),
        widget.TextBox(
            text='',
            foreground="8fbcbb",
            ),
        widget.KeyboardLayout(
            foreground="8fbcbb",
            ),
        widget.TextBox(
            text='|',
            foreground="5e81ac",
            ),
        widget.TextBox(
            text='',
            foreground="5e81ac",
            ),
        widget.Battery(
            format = '{percent:2.0%}'
            ),
        widget.TextBox(
                text='|',
                foreground="ebcb8b",
                ),
        widget.TextBox(
                text='',
                foreground="ebcb8b",
                ),
        widget.Volume(
                foreground="ebcb8b",
                ),
        widget.TextBox(
                text='|',
                foreground="88c0d0",
                ),
        widget.TextBox(
                text='',
                foreground="88c0d0",
                ),
        widget.Backlight(
                foreground="88c0d0",
                backlight_name="intel_backlight",
                ),
        widget.TextBox(
                text='|',
                foreground="a3be8c",
                ),
        widget.TextBox(
                text='',
                foreground="a3be8c",
                ),
        widget.Clock(
                format='%a %I:%M',
                foreground = "a3be8c",
                ),
        widget.TextBox(
                text='|',
                foreground="bf6a6a",
                ),
        widget.TextBox(
                text='',
                foreground="bf6a6a",
                ),
        widget.Wlan(
                foreground="bf6a6a",
                interface="wlp3s0",
                format="{essid}",
                ),
    ], 26, background="2e3440")

# TODO add polkit for pamac to authinticate
mod = "mod4"
# terminal = guess_terminal()
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key(
        [mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "margin": 8,
    "border_width": 2,
    "border_focus": "#3B4252",
    "border_normal": "#2E3440",
}

layouts = [
    layout.Columns(border_focus_stack=["#3B4252", "#2E3440"], border_width=3),
    # layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    layout.RatioTile(),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(),
    layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(highlight_method='line'),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                # widget.Bluetooth(
                #     background='#ffffff',  # Widget background color
                #     fmt='{} ',                      # How to format the text
                #     font='cascadia code',           # Default font
                #     fontshadow=None,                # font shadow color, default is None(no shadow)
                #     fontsize=16,                    # Font size. Calculated if None.
                #     foreground='#2C3E50',            # Foreground colour
                #     hci='/dev_8C_55_4A_9A_7C_B5',
                #     markup=True,                    # Whether or not to use pango markup
                #     max_chars=5,                    # Maximum number of characters to display in widget.
                #     mouse_callbacks={               # Dict of mouse button press callback functions. Acceps functions and lazy calls.
                #         # "Button1": lazy.spawn(bluetooth_prompt),
                #         "Button3": lazy.spawn("blueberry"), },
                #     padding=3,),                      # Padding. Calculated if None.
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
