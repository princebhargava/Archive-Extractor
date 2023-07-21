import PySimpleGUI as sg
from zip_extractor import extract_archive
sg.theme("Black")
label1 = sg.Text("Select Archive to Extract:")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose",key="Archive")

label2 = sg.Text("Select Destination folder:")
input2 = sg.Input()
button2= sg.FolderBrowse("Choose",key="dest_dir")

extract_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compresser",
                   layout = [[label1,input1,button1],
                             [label2,input2,button2],
                             [extract_button,output_label]])
while True:
    event,values = window.read()
    if event == sg.WINDOW_CLOSED:
        exit()
    print(event,values)
    archivepaths=values["Archive"]
    dest_dir=values["dest_dir"]
    extract_archive(archivepaths,dest_dir)
    window["output"].update(value="Extraction successful!!!")

window.close()