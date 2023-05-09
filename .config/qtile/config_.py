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


import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, KeyChord
from libqtile.command import lazy
from libqtile.widget import Spacer

# import arcobattery

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


last_playing = "spotify"

qtile_path = "/home/avenortoz/.config/qtile"

keys = [
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
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
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
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master -q 5%+"),
        desc="Raise audio valume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master -q 5%-"),
        desc="Lower audio valume",
    ),
    # Key(
    #     [],
    #     "XF86MonBrightnessUp",
    #     lazy.spawn(os.path.join(qtile_path, "brightness.sh") + " 1"),
    #     desc="Keyboard brightness up",
    # ),
    # Key(
    #     [],
    #     "XF86MonBrightnessDown",
    #     lazy.spawn(os.path.join(qtile_path, "brightness.sh") + " 0"),
    #     desc="Keyboard brightness down",
    # ),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle between layouts"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "minus",
]

# FOR AZERTY KEYBOARDS
# group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

# group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "\uf89f",
]
# group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
]
# group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )


def init_layout_theme():
    return {
        "margin": 5,
        "border_width": 2,
        "border_focus": "#5e81ac",
        "border_normal": "#4c566a",
    }


layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(
        margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"
    ),
    layout.MonadWide(
        margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"
    ),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
]

# COLORS FOR THE BAR
# Theme name : ArcoLinux Default
def init_colors():
    return [
        ["#2F343F", "#2F343F"],  # color 0
        ["#3c3e3c", "#3c3e3c"],  # color 1
        ["#f0f0f0", "#f0f0f0"],  # color 2
        ["#fba922", "#fba922"],  # color 3
        ["#3384d0", "#3384d0"],  # color 4
        ["#f3f4f5", "#f3f4f5"],  # color 5
        ["#cd1f3f", "#cd1f3f"],  # color 6
        ["#62FF00", "#62FF00"],  # color 7
        ["#f58d56", "#f58d56"],  # color 8
        ["#e9e9e9", "#e9e9e9"],
    ]  # color 9


colors = init_colors()


# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(font="Noto Sans", fontsize=12, padding=2, background=colors[1])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.GroupBox(
            font="FontAwesome",
            fontsize=16,
            margin_y=2,
            margin_x=2,
            padding_y=6,
            padding_x=5,
            borderwidth=0,
            disable_drag=True,
            active=colors[9],
            inactive=colors[5],
            rounded=True,
            highlight_method="text",
            this_current_screen_border=colors[8],
            foreground=colors[2],
            background=colors[1],
        ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.WindowName(
            font="Noto Sans",
            fontsize=12,
            foreground=colors[5],
            background=colors[1],
        ),
        # widget.Net(
        #          font="Noto Sans",
        #          fontsize=12,
        #          interface="enp0s31f6",
        #          foreground=colors[2],
        #          background=colors[1],
        #          padding = 0,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.NetGraph(
        #          font="Noto Sans",
        #          fontsize=12,
        #          bandwidth="down",
        #          interface="auto",
        #          fill_color = colors[8],
        #          foreground=colors[2],
        #          background=colors[1],
        #          graph_color = colors[8],
        #          border_color = colors[2],
        #          padding = 0,
        #          border_width = 1,
        #          line_width = 1,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # # do not activate in Virtualbox - will break qtile
        # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # arcobattery.BatteryIcon(
        #          padding=0,
        #          scale=0.7,
        #          y_poss=2,
        #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        #          update_interval = 5,
        #          background = colors[1]
        #          ),
        # # battery option 2  from Qtile
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.Battery(
        #          font="Noto Sans",
        #          update_interval = 10,
        #          fontsize = 12,
        #          foreground = colors[5],
        #          background = colors[1],
        #          ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.CurrentLayout(
            font="Noto Sans Bold", foreground=colors[5], background=colors[1]
        ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.TextBox(
            font="FontAwesome",
            text="  ",
            foreground=colors[6],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        # widget.ThermalSensor(
        #     foreground=colors[5],
        #     foreground_alert=colors[6],
        #     background=colors[1],
        #     metric=True,
        #     padding=3,
        #     threshold=80,
        # ),
        # widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.TextBox(
            font="FontAwesome",
            text="  ",
            foreground=colors[4],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.Memory(
            font="Noto Sans",
            format="{MemUsed: .0f}MB",
            update_interval=1,
            fontsize=12,
            foreground=colors[5],
            background=colors[1],
        ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.TextBox(
            font="FontAwesome",
            text="  ",
            foreground=colors[3],
            background=colors[1],
            padding=0,
            fontsize=16,
        ),
        widget.Clock(
            foreground=colors[5],
            background=colors[1],
            fontsize=12,
            format="%Y-%m-%d %H:%M",
        ),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.Sep(linewidth=1, padding=10, foreground=colors[2], background=colors[1]),
        widget.Systray(
            background=colors[1],
            icon_size=20,
            padding=4,
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


widgets_screen1 = init_widgets_screen1()


def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=0.75, margin=5)
        )
    ]


screens = init_screens()

# MOUSE CONFIGURATION
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
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #####################################################################################
    ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
    #####################################################################################
    d[group_names[0]] = []
    d[group_names[1]] = []
    d[group_names[2]] = ["code", "Code", "brackets"]
    d[group_names[3]] = ["google-chrome-stable", "Chrome"]
    d[group_names[4]] = ["discord", "Discord"]
    d[group_names[5]] = [
        "Spotify",
        "Pragha",
        "Clementine",
        "Deadbeef",
        "Audacious",
        "spotify",
        "pragha",
        "clementine",
        "deadbeef",
        "audacious",
    ]
    d[group_names[6]] = ["atom", "subl", "geany", "Atom"]
    d[group_names[7]] = [
        "Thunar",
        "Nemo",
        "Caja",
        "Nautilus",
        "org.gnome.Nautilus",
        "Pcmanfm",
        "Pcmanfm-qt",
        "PdfRanger",
        "thunar",
        "nemo",
        "caja",
        "nautilus",
        "org.gnome.nautilus",
        "pcmanfm",
        "pcmanfm-qt",
        "pdfranger",
    ]
    d[group_names[8]] = [
        "Evolution",
        "Geary",
        "Mail",
        "Thunderbird",
        "evolution",
        "geary",
        "mail",
        "thunderbird",
        "gimp",
        "Gimp",
    ]
    d[group_names[9]] = ["Vlc", "vlc", "Mpv", "mpv", "Obs Studio"]
    #     ######################################################################################
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


# @hook.subscribe.startup_once
# def start_once():
#     home = os.path.expanduser("~")
#     subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


# @hook.subscribe.startup
# def start_always():
#     # Set the cursor to something sane in X
#     subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


# @hook.subscribe.client_new
# def set_floating(window):
#     if (
#         window.window.get_wm_transient_for()
#         or window.window.get_wm_type() in floating_types
#     ):
#         window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


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
        Match(wm_class="Arcolinux-welcome-app.py"),
        Match(wm_class="Arcolinux-tweak-tool.py"),
        Match(wm_class="Arcolinux-calamares-tool.py"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(wm_class="arcolinux-logout"),
        Match(wm_class="xfce4-terminal"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
