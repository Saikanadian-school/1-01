

import ui

def mother_teresa(sender):
    view['school_name_label'].text = 'Mother Teresa HS'
    view['mascot_label'].text = 'Titans'
    
def st_joe(sender):
    view['school_name_label'].text = 'St. Joe HS'
    view['mascot_label'].text = 'Jaguars'
    
def st_mark(sender):
    view['school_name_label'].text = 'St. Mark HS'
    view['mascot_label'].text = 'Lions'

view = ui.load_view()
view.present('full_screen')
