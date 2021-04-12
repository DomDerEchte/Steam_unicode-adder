#   Imports
from dearpygui.core import *
from dearpygui.simple import *
import pyperclip as pc

#   Some main settings
set_global_font_scale(1)
set_theme('Cherry')
WIDGET_SPACING = 8

#   Unicode
unicode_character = '󠁳'

#   Here happens all the magic as soon as the button is pressed
def button_pressed(sender, data):
    user_input = get_value(' Group tag/name')
    print(user_input)
    output = unicode_character + user_input
    pc.copy(output)

#   GUI
with window('Steam unicode-adder'):
    add_text('Type in your text and press the button!')
    add_separator()
    add_spacing(count=WIDGET_SPACING)
    add_input_text(' Group tag/name')
    add_spacing(count=WIDGET_SPACING)
    add_button('Add unicode & copy to clipboard', callback=button_pressed)
    add_spacing(count=64)
    add_text('Have fun faking groups lol')

    #   Some window properties
    set_primary_window('Steam unicode-adder', True)
    set_main_window_resizable(False)
    set_main_window_title('Steam unicode-adder')
    set_main_window_size(width=350, height=200)

    #   Start the GUI
    start_dearpygui()
