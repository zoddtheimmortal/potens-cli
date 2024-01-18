import webbrowser
import mpv

from codebase.search import search_gogo_vid

def stream_web(anime,ep):
    link=search_gogo_vid(anime,ep)
    webbrowser.open(link,new=0,autoraise=True)

def stream_mpv(anime,ep):
    link=search_gogo_vid(anime,ep)
    player=mpv.MPV(ytdl=True)
    player.play("https://youtu.be/DOmdB7D-pUU")
    player.wait_for_playback()