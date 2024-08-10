import PySimpleGUI as sg

result = sg.popup_yes_no("あなたは犬が好きですか？")

if result == "Yes":
    sg.popup("犬良いですよね")

if result == "No":
    sg.popup("猫派ですか...")