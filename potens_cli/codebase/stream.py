import webbrowser

from codebase.search import search_gogo_vid

def stream_web(anime,ep):
    link=search_gogo_vid(anime,ep)
    webbrowser.open(link,new=0,autoraise=True)