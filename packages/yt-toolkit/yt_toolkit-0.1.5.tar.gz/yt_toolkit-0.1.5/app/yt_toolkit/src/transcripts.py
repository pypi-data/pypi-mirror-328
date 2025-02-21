import difflib
from typing import Dict, List, Tuple
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

def get_subtitles(video_id: str) -> List[Dict]:
    """Retrieve the subtitles for a given YouTube video."""
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except NoTranscriptFound:
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def find_longest_contiguous_match_transcripts(large_transcript: List[Dict], modified_transcript: List[Dict])-> Tuple[float, float, List[Dict]]:
    """
    Given a full transcript and a modified transcript,
    find the longest contiguous matching segment.
    """
    large_texts = [segment["text"] for segment in large_transcript]
    modified_texts = [segment["text"] for segment in modified_transcript]

    match_indices = []
    for mod_text in modified_texts:
        closest_matches = difflib.get_close_matches(mod_text, large_texts, n=1, cutoff=0.5)
        if closest_matches and len(closest_matches[0].split()) >= 3:
            match_index = large_texts.index(closest_matches[0])
            match_indices.append(match_index)

    if not match_indices:
        return None, None, None

    longest_sequence = []
    current_sequence = [match_indices[0]]
    for i in range(1, len(match_indices)):
        if match_indices[i] == match_indices[i - 1] + 1:
            current_sequence.append(match_indices[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [match_indices[i]]
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    original_extract = [large_transcript[i] for i in longest_sequence]
    start_time = original_extract[0]["start"]
    end_time = original_extract[-1]["start"] + original_extract[-1]["duration"]

    return start_time, end_time, original_extract
