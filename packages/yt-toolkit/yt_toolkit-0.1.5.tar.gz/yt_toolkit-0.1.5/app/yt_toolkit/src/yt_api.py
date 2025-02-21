import os
from typing import Dict, List
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account

def get_youtube_object(path_client_secret_file: str | os.PathLike) -> googleapiclient.discovery.Resource:
    """Initialize and return a YouTube API client."""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    scopes = [
        "https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/youtubepartner-channel-audit",
    ]

    credentials = service_account.Credentials.from_service_account_file(
        path_client_secret_file, scopes=scopes
    )
    youtube_object = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )
    return youtube_object

def collect_videos_matching_query(youtube_object: googleapiclient.discovery.Resource, order: str ="relevance",
                                    category_id: str =None, video_duration: str ="short", start_date:str =None, 
                                    end_date: str =None, total_videos_to_retrieve: int =500) -> List[Dict]:
    """Collect a list of videos matching a query."""
    videos = []
    nextPageToken = None

    while len(videos) < total_videos_to_retrieve:
        request = youtube_object.search().list(
            order=order,
            publishedAfter=start_date,
            publishedBefore=end_date,
            part="snippet",
            maxResults=min(50, total_videos_to_retrieve - len(videos)),
            videoCategoryId=category_id,
            type="video",
            videoDuration=video_duration,
            pageToken=nextPageToken,
        )
        response = request.execute()
        videos += response.get("items", [])

        if "nextPageToken" not in response or len(videos) >= total_videos_to_retrieve:
            break

        nextPageToken = response.get("nextPageToken")

    return videos[:total_videos_to_retrieve]

def collect_all_videos_from_channel(youtube_object: googleapiclient.discovery.Resource, channel_id: str) -> List[Dict]:
    """Collect all video IDs from a given channel's uploads playlist."""
    request = youtube_object.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    next_page_token = None

    while True:
        request = youtube_object.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        videos += response.get("items", [])
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return videos

def collect_video_details(youtube_object: googleapiclient.discovery.Resource, video_id: str) -> dict:
    """Collect details for a specific video."""
    request = youtube_object.videos().list(
        part="contentDetails,id,topicDetails,snippet,liveStreamingDetails,localizations,player,recordingDetails,statistics,status",
        id=video_id
    )
    response = request.execute()
    return response

def collect_channel_metrics(youtube_object: googleapiclient.discovery.Resource, channel_id: str) -> dict:
    """Collect channel metrics."""
    request = youtube_object.channels().list(
        part="snippet,statistics,topicDetails,status,brandingSettings,auditDetails,contentOwnerDetails,localizations",
        id=channel_id
    )
    response = request.execute()
    return response["items"][0]
