import re
import requests

def search_lyrics(artist : str, title : str):
    print((f'https://api.lyrics.ovh/v1/{artist}/{title}')       )
    request = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
    result  = dict(request.json())
    if "No lyrics found" in result.values() :
        return None
    else :
        return result["lyrics"]