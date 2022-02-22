from guizero import App, TextBox, PushButton, Box, MenuBar

def open_file():
    file_returned = app.select_file(filetypes=[["All files", "*.*"], ["Text documents", "*.txt"]])
    if file_returned != ():
        file_name.value = file_returned
        with open(file_name.value, "r") as f:
            editor.value = f.read()
    else:
        return

def save_file():
    file_returned = app.select_file(filetypes=[["All files", "*.*"], ["Text documents", "*.txt"]], save=True)
    if file_returned != '':
        file_name.value = file_returned 
        with open(file_name.value, "w") as f:
            f.write(editor.value)
            save_button.disable()
    else:
        return
        
def enable_save():
    save_button.enable()

def exit_app():
    exit()
    
def dark_theme():
    editor.bg = "black"
    editor.text_color = "white"
    editor.tk.config(insertbackground="white")
    
def light_theme():
    editor.bg = "white"
    editor.text_color = "black"
    editor.tk.config(insertbackground="white")

def insert(key):
    editor.tk.insert(editor.cursor_position, key)
    
app = App(title = "Markdown Maker", width = "1000", height = "500")

menubar = MenuBar(app,
                  # These are the menu options
                  toplevel=["File", "Options"],
                  # The options are recorded in a nested lists, one list for each menu option
                  # Each option is a list containing a name and a function
                  options=[
                      [ ["Open", open_file], ["Save", save_file], ["Exit", exit_app] ],
                      [ ["Dark theme", dark_theme], ["Light theme", light_theme] ],
                        ])

file_controls = Box(app, align="top", width="fill", border=True)
file_name = TextBox(file_controls, text="README.md", width="fill", align="left")
save_button = PushButton(file_controls, enabled=False, text="Save", command=save_file, align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

md_buttons = Box(app, align="top", width="fill", height=30)
heading1_button = PushButton(md_buttons, text="Heading1", command=insert, args=["# "], align="left")
heading2_button = PushButton(md_buttons, text="Heading2", command=insert, args=["## "], align="left")
heading3_button = PushButton(md_buttons, text="Heading3", command=insert, args=["### "], align="left")
heading4_button = PushButton(md_buttons, text="Heading4", command=insert, args=["#### "], align="left")
itals_button = PushButton(md_buttons, text="Italics", command=insert, args=["*"], align="left")
bold_button = PushButton(md_buttons, text="Bold", command=insert, args=["__"], align="left")
cross_button = PushButton(md_buttons, text="Strike", command=insert, args=["~~"], align="left")
bullet_button = PushButton(md_buttons, text="Bullet", command=insert, args=["+ "], align="left")
bullet_indent_button = PushButton(md_buttons, text="Indent", command=insert, args=["   "], align="left")
code_button = PushButton(md_buttons, text="Code", command=insert, args=["```"], align="left")
block_quote = PushButton(md_buttons, text="Quote", command=insert, args=[">"], align="left")
line_button = PushButton(md_buttons, text="Line", command=insert, args=["___"], align="left")
link_button = PushButton(md_buttons, text="Link", command=insert, args=["[Display text](https://)"], align="left")
image_button = PushButton(md_buttons, text="Image", command=insert, args=["![alt text](<image_path>)"], align="left")


editor = TextBox(app, multiline=True, height="fill", width="fill", command=enable_save, scrollbar=True)
editor.font = "verdana"
dark_theme()

app.display()