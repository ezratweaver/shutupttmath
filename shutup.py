"""Mute Annoying Math Application"""
from sys import argv
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from os import chdir, path
from audio_utilities import get_mute_state, toggle_sound

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

OUTPUT_PATH = EXE_DIR
ASSETS_PATH = OUTPUT_PATH / Path("assets")
APPLICATION_TARGET = "GeometryDesktop.exe"



def relative_to_assets(path: str) -> Path:
    """connecting input to correct path"""
    return ASSETS_PATH / Path(path)


class ShutUpTTMath:
    """Main Class"""
    def __init__(self, app_name):
        self.app_name = app_name

        self.app_muted = None

        self.main_window = Tk()
        self.main_window.geometry("287x171")
        self.main_window.configure(bg="#009DDC")

        self.main_canvas = Canvas(
            self.main_window,
            bg="#FFFFFF",
            height=171,
            width=287,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.main_canvas.place(x=0, y=0)

        self.image_button_bg = PhotoImage(
            file=relative_to_assets("button_bg.png"))
        self.image_title_bg = PhotoImage(
            file=relative_to_assets("title_bg.png"))
        self.image_title = PhotoImage(
            file=relative_to_assets("title.png"))
        self.image_mute = PhotoImage(
            file=relative_to_assets("mute.png"))
        self.image_unmute = PhotoImage(
            file=relative_to_assets("unmute.png"))
        self.image_app_active = PhotoImage(
            file=relative_to_assets("app_active.png"))
        self.image_app_inactive = PhotoImage(
            file=relative_to_assets("app_inactive.png"))

        self.button_bg = self.main_canvas.create_image(
            144.0, 131.0, image=self.image_button_bg)
        self.title_bg = self.main_canvas.create_image(
            145.0, 41.0, image=self.image_title_bg)
        self.title = self.main_canvas.create_image(
            145.0, 44.0, image=self.image_title)
        self.app_status = self.main_canvas.create_image(
            270, 156, image=self.image_app_inactive)

        self.button_1 = Button(
            image=self.image_mute,
            borderwidth=0,
            bg="#5A82B9",
            activebackground="#5A82B9",
            highlightthickness=0,
            command=lambda: toggle_sound(APPLICATION_TARGET, self.app_muted),
            relief="flat",
        )
        self.button_1.place(x=92.0, y=113.6, width=104.0, height=30.0)
             
        def on_enter(event):
            self.button_1.config(cursor="hand2")

        def on_leave(event):
            self.button_1.config(cursor="")

        self.button_1.bind("<Enter>", on_enter)
        self.button_1.bind("<Leave>", on_leave)

        self.main_window.iconbitmap("shutup.ico")
        self.main_window.title("Shut Up TT Math")
        self.main_window.resizable(False, False)
            

    def change_mute_button_image(self, toggle):
        """Changes Mute Button Image According to Toggle"""
        if toggle:
            self.button_1.config(image=self.image_unmute)
        else:
            self.button_1.config(image=self.image_mute)

    def change_status_image(self, toggle):
        """Changes Status Image According to Toggle"""
        if toggle:
            self.main_canvas.itemconfigure(
                self.app_status, image=self.image_app_active)
        else:
            self.main_canvas.itemconfigure(
                    self.app_status, image=self.image_app_inactive)  

    def constant_mute_check(self):
        """Method constantly ran to see if app is muted, repeats every 100ms"""
        self.app_muted, self.app_active = get_mute_state(self.app_name)
        self.change_mute_button_image(self.app_muted)
        self.change_status_image(self.app_active)
        self.main_canvas.after(100, self.constant_mute_check)


    def run(self):
        """Prerequisites to start app"""
        self.constant_mute_check()
        self.main_window.mainloop()


if __name__ == '__main__':
    app = ShutUpTTMath(APPLICATION_TARGET)
    app.run()
