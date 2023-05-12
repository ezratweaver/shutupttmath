from pycaw import pycaw
from pygame import mixer

mixer.init()
click_sound = mixer.Sound('assets/click.mp3')

def get_mute_state(app_name):
    """Check if the specified app is muted or not, returns boolean"""
    all_current_sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in all_current_sessions:
        audio_volume = session._ctl.QueryInterface(pycaw.ISimpleAudioVolume)
        if session.Process and session.Process.name() == app_name:
            return audio_volume.GetMute(), True
    return False, False

def toggle_sound(app_name, muted_state):
    """Toggle Sound"""
    muted_state = not muted_state
    click_sound.play()
    sessions = pycaw.AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == app_name:
            volume.SetMute(muted_state, None)
        return muted_state