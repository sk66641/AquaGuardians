################################################################################
## Initialization
################################################################################

## Offset Initialization to make sure this is loaded first
init offset = -2

## Initialize GUI
init python:
    gui.init(1920, 1080)

## Enable property conflict checks
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################

## Colors ######################################################################
## Update color scheme to match space-themed UI.

define gui.accent_color = '#00ccff'           ## Neon cyan for accents
define gui.idle_color = '#4d4d4d'             ## Dark grey for idle buttons
define gui.idle_small_color = '#b3b3b3'       ## Light grey for small idle text
define gui.hover_color = '#00ffcc'            ## Bright cyan for hover effects
define gui.selected_color = '#ffffff'         ## White for selected buttons
define gui.insensitive_color = '#2e2e2e7f'    ## Muted grey for disabled buttons
define gui.muted_color = '#1f1f1f'            ## Darker grey for muted elements
define gui.hover_muted_color = '#005757'      ## Deep teal for hover on muted
define gui.text_color = '#ffffff'             ## Bright white for text
define gui.interface_text_color = '#b3e6ff'   ## Light cyan for interface text

## Fonts and Font Sizes ########################################################
## Use a more futuristic font

define gui.text_font = "Orbitron-Regular.ttf"    ## Futuristic font for dialogue
define gui.name_text_font = "Orbitron-Regular.ttf"
define gui.interface_text_font = "Orbitron-Regular.ttf"

define gui.text_size = 35                        ## Slightly larger text
define gui.name_text_size = 50                   ## Larger name text for emphasis
define gui.interface_text_size = 35
define gui.label_text_size = 40
define gui.notify_text_size = 28
define gui.title_text_size = 85                  ## Bold and large title text

## Main and Game Menus #########################################################
## Space-themed background images for the menus

define gui.main_menu_background = "gui/space_main_menu.png"
define gui.game_menu_background = "gui/space_game_menu.png"


## Dialogue ####################################################################
## Adjust the textbox to have a more minimal and sleek look

define gui.textbox_height = 250                ## Slightly reduced textbox height
define gui.textbox_yalign = 1.0                ## Align textbox to the bottom

define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0

define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
## Neon effects for buttons to enhance the sci-fi theme

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = '#4d4d4d'
define gui.button_text_hover_color = '#00ffcc'
define gui.button_text_selected_color = '#ffffff'
define gui.button_text_insensitive_color = '#2e2e2e7f'

define gui.button_text_xalign = 0.5             ## Center-align button text

## Customizing buttons
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)

## Neon hover effects for quick menu
define gui.quick_button_text_size = 22
define gui.quick_button_text_idle_color = '#888888'
define gui.quick_button_text_hover_color = '#00ffcc'
define gui.quick_button_text_selected_color = '#ffffff'


## Choice Buttons ##############################################################
## Widening the choice buttons for better readability and touch interactions

define gui.choice_button_width = 1200
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#00ffcc"
define gui.choice_button_text_insensitive_color = '#8888887f'


## File Slot Buttons ###########################################################
## Add more sci-fi style to save slots

define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = '#4d4d4d'
define gui.slot_button_text_hover_color = '#00ffcc'
define gui.slot_button_text_selected_idle_color = '#ffffff'
define gui.slot_button_text_selected_hover_color = '#00ffcc'

define config.thumbnail_width = 384
define config.thumbnail_height = 216


## Bars, Scrollbars, and Sliders ###############################################
## Clean, glowing progress bars and sliders

define gui.bar_size = 40
define gui.slider_size = 40
define gui.scrollbar_size = 20

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)


## History and NVL-Mode ########################################################
## Use the same fonts and colors for history and NVL mode

define gui.history_name_xpos = 233
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 255
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 180
define gui.nvl_spacing = 20

define gui.nvl_name_xpos = 640
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 680
define gui.nvl_text_width = 900
define gui.nvl_text_xalign = 0.0

define gui.nvl_button_xpos = 680
define gui.nvl_button_xalign = 0.0
