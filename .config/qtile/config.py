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

from webbrowser import get
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from subprocess import Popen
import os

# ===============================================================================
# ---------------------------------GLOBALS---------------------------------------
# ===============================================================================

qtile_path = os.path.dirname(__file__)
home = os.getenv("HOME") or ""

autost = os.path.join(qtile_path, "autostart.sh")
bluetooth_prompt = os.path.join(qtile_path, "dmenu_bluetooth.sh")
locker = "slock"
screenshot = "flameshot gui"
second_monitor_script_path = os.path.join(qtile_path, "screen.sh")


@hook.subscribe.startup_once
def autostart():
    processes = [
        # ["feh", "--bg-scale", home + "/Pictures/10.png"],
        # ["xset", "r", "rate", "250", "40"],
        # ["setxkbmap", "-layout", "us,ua", "-option", "\'grp:alt_shift_toggle\'"],
        # ["picom", "-b"],
        # ["mpd"],
    ]
    for p in processes:
        Popen(p)
    Popen(["bash", autost])


# @hook.subscribe.client_new
# def floating_dialogs(window):
#     if(window.name == "kitty"):
#         window.floating = True


# TODO add polkit for pamac to authinticate
mod = "mod4"
# terminal = guess_terminal()
terminal = "kitty"

# ===============================================================================
# ---------------------------------KEYBINDINGS-----------------------------------
# ===============================================================================
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "y", lazy.shutdown(), desc="Shutdown Qtile"),
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
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn(os.path.join(qtile_path, "brightness.sh") + " 1"),
        desc="Keyboard brightness up",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn(os.path.join(qtile_path, "brightness.sh") + " 0"),
        desc="Keyboard brightness down",
    ),
    Key(
        [mod],
        "c",
        lazy.spawn(
            "rofi -modi \"clipboard:greenclip print\" -show clipboard -run-command '{cmd}'"
        ),
        desc="Toggle clipboard selection",
    ),
    Key(
        [mod, "control"],
        "m",
        lazy.spawn("kitty ncmpcpp"),
        desc="Open music player",
    ),
    Key(
        [mod, "control"],
        "p",
        lazy.spawn("kitty ping -c5 google.com"),
        desc="Open music player",
    ),
    Key(
        [mod],
        "b",
        lazy.spawn("firefox"),
        desc="Browser",
    ),
    Key([mod, "control"], "w", lazy.spawn(screenshot)),
    Key([mod, "control"], "z", lazy.spawn(locker), desc="Toggle maximize"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle between layouts"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod], "a", lazy.layout.maximize(), desc="Toggle maximize"),
    Key([mod, "control"], "a", lazy.layout.swap_main(), desc="Toggle maximize"),
    Key([mod], "g", lazy.layout.reset(), desc="Toggle maximize"),
    Key(
        [mod, "control"],
        "s",
        lazy.spawn(second_monitor_script_path),
        desc="Toggle second monitor if one is present.",
    ),
    Key(
        [mod],
        "slash",
        lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh")),
        desc="Run rofi as the powermenu",
    ),
]

# ===============================================================================
# ------------------------------------LAYOUTS------------------------------------
# ===============================================================================
layouts = [
    # layout.Columns(border_focus_stack=["#3B4252", "#2E3440"], border_width=3),
    layout.MonadTall(
        border_focus="5e81ac",
        border_normal="b48ead",
        border_width=3,
        margin=5,
    ),
    layout.Columns(
        border_focus="5e81ac",
        border_normal="b48ead",
        border_width=3,
        margin=5,
    ),
    # layout.MonadWide(
    #     border_focus="5e81ac",
    #     border_normal="b48ead",
    #     border_width=3,
    #     margin=5,
    # ),
    layout.Max(
        border_focus="5e81ac",
        border_normal="b48ead",
        border_width=3,
        margin=5,
    ),
    layout.MonadThreeCol(
        border_focus="5e81ac",
        border_normal="b48ead",
        border_width=3,
        margin=5,
    ),
    layout.Stack(
        border_focus="5e81ac",
        border_normal="b48ead",
        border_width=3,
        margin=5,
    ),
]
layouts[0].cmd_reset(0.60, redraw=False)
# layouts[2].cmd_reset(0.80, redraw=False)

# ===============================================================================
# ------------------------------------GROUPS-------------------------------------
# ===============================================================================
groups = [Group(i) for i in "123456789"]
groups[0] = Group(
    name="code",
    label=" ",
    layout="monadtall",
    layouts=[layouts[0], layouts[1], layouts[2]],
)
groups[1] = Group(
    name="util",
    label="",
    layout="columns",
)
groups[2] = Group(
    name="vscode",
    label=" ",
    # label="3",
    layout="max",
    matches=[
        Match(wm_class=["code"]),
    ],
)
groups[4] = Group(
    name="zoom",
    label="5",
    layout="columns",
    matches=[Match(wm_class=["zoom"])],
)
groups[5] = Group(
    name="telegram",
    label="6",
    layout="monadwide",
    matches=[Match(wm_class=["TelegramDesktop"])],
)
groups[6] = Group(
    name="docs",
    label=" ",
    layout="max",
    matches=[
        Match(wm_class=["zeal"]),
        Match(wm_class=["Zathura"]),
    ],
)
groups[7] = Group(
    name="browser", label=" ", layout="max", matches=[Match(wm_class=["firefox"])]
)
groups[8] = Group(
    name="music", label="", layout="columns", matches=[Match(wm_class=["Ncmpcpp"])]
)


def toscreen(qtile, group_name):
    if group_name == qtile.current_screen.group.name:
        qtile.current_screen.set_group(qtile.current_screen.previous_group)
    else:
        for i in range(len(qtile.groups)):
            if group_name == qtile.groups[i].name:
                qtile.current_screen.set_group(qtile.groups[i])
                break


for idx, i in enumerate(groups, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                # i.name,
                f"{idx}",
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                # i.name,
                f"{idx}",
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            Key(
                [mod],
                # i.name,
                f"{idx}",
                lazy.function(toscreen, i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )

# ===============================================================================
# ------------------------------------WIDGETS------------------------------------
# ===============================================================================
# Defaults: widget_defaults, extension_defaults - used by qtile
widget_defaults = dict(
    # font="Cascadia Code",
    # font="meslolgs",
    # font="powerline",
    font="MesloLGM Nerd Font",
    fontsize=20,
    padding=4,
    background="2e3440",
    # foreground="5e81ac",
    foreground="ffffff",
)
extension_defaults = widget_defaults.copy()

widget_colors = {
    "time": {"background": "a3be8c", "foreground": ""},
    "volume": {"background": "ebcb8b", "foreground": ""},
    "systray": {"background": "B48EAD", "foreground": ""},
    "battery": {"background": "5e81ac", "foreground": ""},
    "keyboard": {"background": "8fbcbb", "foreground": ""},
    # "weather": {"background": "B48EAD", "foreground": ""},
    "weather": {"background": "bf6a6a", "foreground": ""},
}


def get_bar():
    return bar.Bar(
        [
            widget.Spacer(10),
            widget.GroupBox(
                active="5e81ac",
                inactive="b48ead",
                this_current_screen_border="B48EAD",
                highlight_method="text",
                highlight_color=["2e3440", "2e3440"],
                disable_drag=True,
                # center_aligned=True,
                hide_unused=True,
                # margin=5,
                padding=0,
            ),
            widget.Spacer(15),
            widget.WindowName(
                max_chars=15,
                # foreground="5e81ac",
                foreground="B48EAD",
            ),
            # widget.Prompt(
            #     prompt="Run:",
            # ),
            # widget.TextBox(text="|", foreground="bf6a6a"),
            # widget.TaskList(
            #    foreground = "2e3440",
            #    border = "5e81ac",
            #    fontsize = 11,
            #    unfocused_border = "b48ead",
            #    highlight_method = "block",
            #    max_title_width=100,
            #    title_width_method="uniform",
            #    icon_size = 13,
            #    rounded=False,
            # ),
            widget.Bluetooth(
                hci="/dev_74_45_CE_1B_76_EB",
                mouse_callbacks={  # Dict of mouse button press callback functions. Acceps functions and lazy calls.
                    "Button1": lazy.spawn(bluetooth_prompt),
                    "Button3": lazy.spawn("blueberry"),
                },
                fmt=" ",
            ),
            widget.Spacer(bar.STRETCH),
            widget.TextBox(
                text="",
                # background=widget_colors["systray"]["background"],
                foreground=widget_colors["systray"]["background"],
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.Systray(
                background=widget_colors["systray"]["background"],
            ),
            widget.TextBox(
                text="",
                foreground=widget_colors["weather"]["background"],
                background=widget_colors["systray"]["background"],
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.OpenWeather(
                location="Ternopil",
                format="{icon}{main_temp} °{units_temperature} {humidity}%",
                background=widget_colors["weather"]["background"],
            ),
            # widget.TextBox(
            #     text="",
            #     foreground=widget_colors["keyboard"]["background"],
            #     background=widget_colors["weather"]["background"],
            #     fontsize=24,  # Font pixel size. Calculated if None.
            #     padding=0,
            # ),
            # widget.TextBox(
            #     text=" ",
            #     background=widget_colors["keyboard"]["background"],
            # ),
            # widget.KeyboardLayout(
            #     # foreground="8fbcbb",
            #     background=widget_colors["keyboard"]["background"],
            # ),
            widget.TextBox(
                text="",
                background=widget_colors["weather"]["background"],
                foreground=widget_colors["battery"]["background"],
                # background="5e81ac",
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.TextBox(
                text=" ",
                # foreground="5e81ac",
                background=widget_colors["battery"]["background"],
            ),
            widget.Battery(
                format="{percent:2.0%}",
                background=widget_colors["battery"]["background"],
            ),
            widget.TextBox(
                text="",
                foreground=widget_colors["volume"]["background"],
                background=widget_colors["battery"]["background"],
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.TextBox(
                text=" ",
                background=widget_colors["volume"]["background"],
                padding=0,
            ),
            widget.Volume(
                background=widget_colors["volume"]["background"],
            ),
            widget.TextBox(
                text="",
                foreground="88c0d0",
                background=widget_colors["volume"]["background"],
                # background="88c0d0",
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.TextBox(
                text=" ",
                # foreground="88c0d0",
                background="88c0d0",
                padding=0,
            ),
            widget.Backlight(
                # foreground="88c0d0",
                background="88c0d0",
                backlight_name="intel_backlight",
            ),
            widget.TextBox(
                text="",
                foreground=widget_colors["time"]["background"],
                background="88c0d0",
                # background="a3be8c",
                fontsize=24,  # Font pixel size. Calculated if None.
                padding=0,
            ),
            widget.TextBox(
                text=" ",
                # foreground="a3be8c",
                background=widget_colors["time"]["background"],
                padding=0,
            ),
            widget.Clock(
                format="%a %I:%M",
                background=widget_colors["time"]["background"],
            ),
            # widget.TextBox(
            #     text="",
            #     background=widget_colors["time"]["background"],
            #     foreground="bf6a6a",
            #     fontsize=24,  # Font pixel size. Calculated if None.
            #     padding=0,
            # ),
            # widget.TextBox(
            #     text=" ",
            #     # foreground="bf6a6a",
            #     background="bf6a6a",
            #     padding=0,
            # ),
            # widget.Wlan(
            #     # foreground="bf6a6a",
            #     background="bf6a6a",
            #     interface="wlo1",
            #     format="{essid}",
            # ),
        ],
        26,
        background="2e3440",
        foreground="ffffff",
        border_width=0,
        border_color="5e81ac",
        opacity=0.8,
    )


screens = [
    Screen(top=get_bar()),
    # Screen(top=get_bar()),
    Screen(),
    # Screen(top=get_bar()),
    # Screen(bottom=bar.Bar(
    # [widget.GroupBox(), widget.WindowName()], 30), ),
    # Screen(bottom=bar.Bar(
    # [widget.GroupBox(), widget.WindowName()], 30), ),
]

# ===============================================================================
# ------------------------------------MOUSE--------------------------------------
# ===============================================================================

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

# ===============================================================================
# --------------------------------OTHER CONFIGS----------------------------------
# ===============================================================================

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
        Match(wm_class="pamac-manager"),
        Match(wm_class="toipe"),
    ],
    border_focus="5e81ac",
    border_normal="b48ead",
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
