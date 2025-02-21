import unittest
import sys
sys.path.append("./")
from src.transcripts import find_longest_contiguous_match_transcripts
from src.heatmap_tools import get_heatmap, extract_replay_heatmap_data
from src.video_scraping import is_youtube_short, get_linked_videoID_if_short

YOUTUBE_SHORT_VIDEO_ID = "wxYxF6lmfQM"  
YOUTUBE_REGULAR_VIDEO_ID = "gXSd96hFd_A" 
VIDEO_WITH_SUBTITLES_ID = "gXSd96hFd_A"
class GeneratorTest(unittest.TestCase):
    #########################################
    # Tests for Transcript Processing
    #########################################

    def test_find_longest_contiguous_match_transcripts(self):
        """
        Test that the transcript matching function correctly finds the
        contiguous matching segment.
        """
        # Sample "large" transcript
        large_transcript = [
            {'text': 'Hey there', 'start': 7.58, 'duration': 6.13},
            {'text': 'how are you', 'start': 14.08, 'duration': 7.58},
            {'text': 'I am fine', 'start': 21.66, 'duration': 5.32},
            {'text': 'thanks for asking', 'start': 27.00, 'duration': 4.20},
            {'text': 'this is a large transcript with many sentences', 'start': 31.20, 'duration': 7.00},
            {'text': 'it contains various clips from different videos', 'start': 38.20, 'duration': 6.50},
            {'text': 'this particular example is meant to demonstrate text comparison', 'start': 44.70, 'duration': 8.30},
            {'text': 'sometimes, texts are modified slightly and spread across multiple parts', 'start': 53.00, 'duration': 9.50},
            {'text': 'this makes the detection of original extracts more challenging', 'start': 62.50, 'duration': 7.50},
            {'text': 'additional sentences are here to provide more context', 'start': 70.00, 'duration': 6.50},
            {'text': 'each part of the transcript adds more information', 'start': 76.50, 'duration': 5.50},
            {'text': 'another sentence for good measure', 'start': 82.00, 'duration': 4.00},
            {'text': 'more sentences to simulate a longer transcript', 'start': 86.00, 'duration': 6.00},
            {'text': 'continuing to expand the transcript', 'start': 92.00, 'duration': 4.50},
            {'text': 'still more text to analyze', 'start': 96.50, 'duration': 4.00},
            {'text': 'even more sentences to ensure a thorough test', 'start': 100.50, 'duration': 6.00},
            {'text': 'sentences continue to be added', 'start': 106.50, 'duration': 5.00},
            {'text': 'testing with a substantial amount of text', 'start': 111.50, 'duration': 7.00},
            {'text': 'another line here', 'start': 118.50, 'duration': 3.00},
            {'text': 'and another one here', 'start': 121.50, 'duration': 3.00},
            {'text': 'the transcript keeps growing', 'start': 124.50, 'duration': 4.50},
            {'text': 'more and more text', 'start': 129.00, 'duration': 4.00},
            {'text': 'yet another sentence', 'start': 133.00, 'duration': 3.50},
            {'text': 'further expanding the transcript', 'start': 136.50, 'duration': 5.00},
            {'text': 'text continues', 'start': 141.50, 'duration': 2.50},
            {'text': 'sentence number 22, which will be used', 'start': 144.00, 'duration': 5.00},
            {'text': 'final sentence to wrap up', 'start': 149.00, 'duration': 4.00}
        ]
        # Sample modified transcript that is a contiguous subset of the large transcript
        modified_transcript = [
            {"text": "this is a large transcript with many sentences", "start": 31.20, "duration": 7.00},
            {"text": "it contains various clips from different videos", "start": 38.20, "duration": 6.50},
            {"text": "sentence number 22, which will be used", "start": 144.00, "duration": 5.00},
        ]
        start_time, end_time, extract = find_longest_contiguous_match_transcripts(
            large_transcript, modified_transcript
        )
        self.assertEqual(start_time, 31.20)
        self.assertEqual(end_time, 38.2 + 6.50)
        self.assertEqual(len(extract), 2)


    #########################################
    # Tests for Heatmap 
    #########################################

    def test_get_heatmap(self):
        """
        Test that get_heatmap returns the SVG path data for a YouTube video.
        """
        valid_video_id = "AvXZ5CvzdTY"
        invalid_video_id = "invalid_video_id"
        
        result = get_heatmap(valid_video_id)
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("M"))

        result = get_heatmap(invalid_video_id)
        self.assertIn("Error finding element: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\".ytp-heat-map-path\"}",
                        result)

    def test_extract_replay_heatmap_data(self):
        """
        Test that process_heatmap returns a list of (time, retention) tuples.
        """
        valid_svg_path = "M 0.0,100.0 C 1.0,96.1 2.0,82.3 5.0,80.3 C 8.0,78.3 11.0,88.1 15.0,90.0"
        video_duration = 300
        
        result = extract_replay_heatmap_data(valid_svg_path, video_duration)
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 10)
        first_item = result[0]
        self.assertIsInstance(first_item, tuple)
        self.assertEqual(len(first_item), 2)
        self.assertEqual(first_item[0], 0.0)
        self.assertEqual(first_item[1], 0.0)
        first_item = result[-1]
        self.assertIsInstance(first_item, tuple)
        self.assertEqual(len(first_item), 2)
        self.assertEqual(first_item[0], 4.5)
        self.assertEqual(first_item[1], 10.000000000000014)


    #########################################
    # Tests for Scraping Helpers
    #########################################

    def test_is_youtube_short(self):
        result_short = is_youtube_short(YOUTUBE_SHORT_VIDEO_ID)
        result_rv = is_youtube_short(YOUTUBE_REGULAR_VIDEO_ID)
        self.assertTrue(result_short)
        self.assertFalse(result_rv)

    def test_get_linked_videoID_if_short(self):    
        is_short, linked_videos = get_linked_videoID_if_short(YOUTUBE_SHORT_VIDEO_ID)
        self.assertTrue(is_short)
        self.assertEqual(linked_videos, (YOUTUBE_SHORT_VIDEO_ID, YOUTUBE_REGULAR_VIDEO_ID))
        
        is_short, linked_videos = get_linked_videoID_if_short(YOUTUBE_REGULAR_VIDEO_ID)
        self.assertFalse(is_short)
        self.assertIsNone(linked_videos)

