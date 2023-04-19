"""Mute Annoying Math Application"""
from sys import argv
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from os import chdir, path
from pycaw import pycaw
from pygame import mixer

exe_dir = path.dirname(argv[0])
chdir(exe_dir)

OUTPUT_PATH = exe_dir
ASSETS_PATH = OUTPUT_PATH / Path("assets")
APPLICATION_TARGET = "Algebra1.exe"

mixer.init()

def relative_to_assets(path: str) -> Path:
    """connecting input to correct path"""
    return ASSETS_PATH / Path(path)


class ShutUpTTMath:
    """Main Class"""
    def __init__(self, app_name):
        self.app_name = app_name

        self.app_muted = self.is_app_muted(self.app_name)

        self.main_window = Tk()
        self.main_window.geometry("222x139")
        self.main_window.configure(bg="#009DDC")

        self.click_sound = mixer.Sound('assets/click.mp3')

        self.main_canvas = Canvas(
            self.main_window,
            bg="#009DDC",
            height=139,
            width=222,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.main_canvas.place(x=0, y=0)

        self.image_bg_lines = PhotoImage(file=relative_to_assets("bg_lines.png"))
        self.image_button_bg = PhotoImage(file=relative_to_assets("button_bg.png"))
        self.image_title_bg = PhotoImage(file=relative_to_assets("title_bg.png"))
        self.image_title = PhotoImage(file=relative_to_assets("title.png"))
        self.image_mute = PhotoImage(file=relative_to_assets("mute.png"))
        self.image_unmute = PhotoImage(file=relative_to_assets("unmute.png"))

        self.bg_lines = self.main_canvas.create_image(111, 70, image=self.image_bg_lines)
        self.button_bg = self.main_canvas.create_image(108.0, 108.0, image=self.image_button_bg)
        self.title_bg = self.main_canvas.create_image(111.0, 38.0, image=self.image_title_bg)
        self.title = self.main_canvas.create_image(112.0, 40.0, image=self.image_title)

        self.button_1 = Button(
            image=self.image_mute,
            borderwidth=0,
            bg="#F58025",
            activebackground="#F58025",
            highlightthickness=0,
            command=self.toggle_sound,
            relief="flat",
        )
        self.button_1.place(x=77.0, y=94.6, width=64.0, height=24.0)

        def on_enter(event):
            self.button_1.config(cursor="hand2")

        def on_leave(event):
            self.button_1.config(cursor="")

        self.button_1.bind("<Enter>", on_enter)
        self.button_1.bind("<Leave>", on_leave)

        self.main_window.iconbitmap("shutup.ico")
        self.main_window.title("Shut Up")
        self.main_window.resizable(False, False)

    def toggle_sound(self):
        """Toggle Sound"""
        self.app_muted = not self.app_muted
        self.click_sound.play()
        sessions = pycaw.AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.app_name:
                volume.SetMute(self.app_muted, None)
                self.change_mute_button_image(self.app_muted)

    def change_mute_button_image(self, toggle):
        """Change Mute Button Image According to Toggle"""
        if toggle:
            self.button_1.config(image=self.image_unmute)
        else:
            self.button_1.config(image=self.image_mute)

    def is_app_muted(self, app_name):
        """Check if the specified app is muted or not."""
        all_current_sessions = pycaw.AudioUtilities.GetAllSessions()
        for session in all_current_sessions:
            audio_volume = session._ctl.QueryInterface(pycaw.ISimpleAudioVolume)
            if session.Process and session.Process.name() == app_name:
                return audio_volume.GetMute()
        return False


    def run(self):
        """Run Function"""
        self.main_window.mainloop()


if __name__ == '__main__':
    app = ShutUpTTMath(APPLICATION_TARGET)
    app.change_mute_button_image(app.is_app_muted(APPLICATION_TARGET))
    app.run()
