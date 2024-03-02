import webbrowser
import mpv
import vlc

from codebase.search import search_gogo_vid

def stream_web(anime,ep):
    link=search_gogo_vid(anime,ep)
    webbrowser.open(link,new=0,autoraise=True)

def stream_mpv(anime,ep):
    link=search_gogo_vid(anime,ep)
    player=mpv.MPV(ytdl=True)
    player.play(link)
    player.wait_for_playback()

def stream_vlc(anime,ep):
    link="https://www104.vipanicdn.net/streamhls/7673f8861e546cdca7c5923f1132e5d1/ep.24.1703908265.1080.m3u8"
    Instance=vlc.Instance()
    player=Instance.media_player_new()
    Media=Instance.media_new(link)
    Media.get_mrl()
    player.set_media(Media)
    # player.set_title(f"{anime} - {ep}")
    player.play()