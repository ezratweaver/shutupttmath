"""Mute Annoying Math Application"""
from sys import argv
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from os import chdir, path
from pycaw import pycaw

exe_dir = path.dirname(argv[0])
chdir(exe_dir)


OUTPUT_PATH = exe_dir
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    """connecting input to correct path"""
    return ASSETS_PATH / Path(path)


main_window = Tk()

main_window.geometry("222x139")
main_window.configure(bg="#009DDC")


main_canvas = Canvas(
    main_window,
    bg="#009DDC",
    height=139,
    width=222,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
main_canvas.place(x=0, y=0)


image_bg_lines = PhotoImage(file=relative_to_assets("bg_lines.png"))
image_button_bg = PhotoImage(file=relative_to_assets("button_bg.png"))
image_title_bg = PhotoImage(file=relative_to_assets("title_bg.png"))
image_title = PhotoImage(file=relative_to_assets("title.png"))
image_mute = PhotoImage(file=relative_to_assets("mute.png"))
image_unmute = PhotoImage(file=relative_to_assets("unmute.png"))

bg_lines = main_canvas.create_image(111, 70, image=image_bg_lines)
button_bg = main_canvas.create_image(108.0, 108.0, image=image_button_bg)
title_bg = main_canvas.create_image(111.0, 38.0, image=image_title_bg)
title = main_canvas.create_image(112.0, 40.0, image=image_title)

APP_NAME = "Algebra1.exe"
SOUND_TOGGLE = True


def toggle_sound(toggle, app):
    """Toggle Sound"""
    global SOUND_TOGGLE
    SOUND_TOGGLE = not SOUND_TOGGLE
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == app:
            volume.SetMute(toggle, None)
            if toggle:
                button_1.config(image=image_unmute)
                return False
            button_1.config(image=image_mute)
            return True


button_1 = Button(
    image=image_mute,
    borderwidth=0,
    bg="#F58025",
    activebackground="#F58025",
    highlightthickness=0,
    command=lambda: toggle_sound(SOUND_TOGGLE, APP_NAME),
    relief="flat",
)
button_1.place(x=77.0, y=94.6, width=64.0, height=24.0)

main_window.iconbitmap("shutup.ico")
main_window.title("Shut Up")
main_window.resizable(False, False)
main_window.mainloop()
