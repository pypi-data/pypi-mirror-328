import requests
from bs4 import BeautifulSoup
import json
from typing import Tuple
import re

def is_youtube_short(video_id: str) -> bool:
    """Determine if a video is a YouTube Short by checking the URL response."""
    shorts_url = f"https://www.youtube.com/shorts/{video_id}"
    response = requests.head(shorts_url, allow_redirects=False)
    if response.status_code == 200:
        return True
    elif response.status_code == 303:
        return False
    else:
        print(response.status_code, response)
        return None

def get_youtube_html(video_id: str, is_short: bool=True) -> str:
    """Retrieve the HTML of a YouTube video page."""
    if is_short:
        url = f"https://www.youtube.com/shorts/{video_id}"
    else:
        url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to retrieve HTML"

def get_linked_videoID_if_short(video_id: str) -> Tuple[bool, Tuple[str, str]]:
    """Determine if the video is a Short and try to extract a linked video on the lower bar."""
    shorts_url = f"https://www.youtube.com/shorts/{video_id}"
    response = requests.get(shorts_url, allow_redirects=False)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        script_tag = soup.find('script', string=re.compile('ytInitialData'))

        if script_tag:
            try:
                json_text = re.search(r'var ytInitialData = ({.*?});', script_tag.string)
                if json_text:
                    v = json.loads(json_text.group(1))
                    linked_videoID = (
                        v['overlay']['reelPlayerOverlayRenderer']['metapanel']['reelMetapanelViewModel']
                        ['metadataItems'][1]['reelMultiFormatLinkViewModel']['command']['innertubeCommand']
                        ['watchEndpoint']['videoId']
                    )
                    return (True, (video_id, linked_videoID))
                else:
                    return (True, None)
            except (KeyError, json.JSONDecodeError) as e:
                print(f"Error parsing JSON: {e}")
                return (True, None)
        else:
            return (True, None)
    
    elif response.status_code == 303:
        # Status code 303 with a redirect indicates it's not a Short
        return (False, None)
    
    else:
        print(f"Unexpected status code: {response.status_code}")
        return (None, None)