# creating a Login GUI using Py simple GUI 

#import module Pysimple Gui and named as SG
import PySimpleGUI as sg

# determined the theme for your GUI 
# there are about 8 themes given in pysimple GUI you can get detailes on that by running 
# "sg.theme_previewer()"
sg.theme('DarkAmber')

#determined font for the GUI 
font = ("Times New Roman", 20)

#creating a Layout for our GUI
layout = [
    [sg.Text("A simple login UI Example.",size=(68, 2), justification='centre', font=font)],
    [sg.Text('Enter username : ',size=(20, 1),justification='centre', font=font), sg.InputText(size=(28, 1),enable_events=True, key="-USR-", font=font)],
    [sg.Text('Enter password : ',size=(20, 1),justification='centre', font=font), sg.InputText(size=(28, 1),enable_events=True, key="-PSS-", font=font, password_char='*')],
    [sg.Button('LOGIN',size=(34, 1), font=font,key="-LGN-"),sg.Button('Exit',size=(34,1),font=font)]
]

# Create the window
window = sg.Window("Title is given here", layout,enable_close_attempted_event=True,finalize=True)
#the string is pointed to the title of the UI
#finalize=True determines that the layout is not going to changed at further default it is false 
#setting it true lets you editing the values of buttons, textbox or even the text field
saved_once = False
# Create an event loop
while True:
    # adding events to window.
    event, values = window.read()
    # creating an event for upload button.
    if event == "-LGN-" :
        #getting values from text box.
        usr_nm = str(values["-USR-"])
        pass_ss = str(values["-PSS-"])
        if usr_nm == '':
            # check for username field.
            sg.popup('Notice!!',"username is empty !!")
            continue
        elif pass_ss == '':
            # check for password field.
            sg.popup('Notice!!',"password field is empty!!")
            continue
    # creating an event for exit button
    elif (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        #if the user select exit this loop will be ended
        break

window.close()
