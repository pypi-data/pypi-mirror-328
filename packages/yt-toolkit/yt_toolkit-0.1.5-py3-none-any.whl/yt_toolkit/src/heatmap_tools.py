from typing import List, Tuple
from svgpathtools import parse_path
import svgpathtools
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_heatmap(video_id: str) -> str:
    """
    Retrieve the YouTube heat map element for a video using Selenium.
    Returns the SVG path data representing the replay heatmap.
    """
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Initialize WebDriver
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(60)
    except OSError as e:
        return f"Driver Initialization Error: {e}"

    # Open the webpage
    driver.get(f"https://www.youtube.com/watch?v={video_id}")

    # Find the element
    try:
        element = driver.find_element(By.CLASS_NAME, "ytp-heat-map-path")
        return element.get_attribute('d')
    except Exception as e:
        return "Error finding element: " + str(e)
    finally:
        driver.quit()  # Ensure the browser is closed even if an error occurs

def extract_replay_heatmap_data(replay_heatmap_svg: str, video_duration: int | float) -> List[Tuple[float, float]]:
    """
    This function processes the SVG path data representing viewer rewatch behavior, 
    as shown in the replay graph above the YouTube video progress bar. It returns a list of 
    (timestamp, replay_score) tuples, indicating which parts of the video have been 
    replayed the most.

    Args:
        replay_heatmap_svg (str): The SVG path data representing the replay heatmap.
        video_duration (int): The total duration of the video in seconds.

    Returns:
        list of tuples: Each tuple contains (timestamp, replay_score), where 
        replay_score reflects how often that part of the video has been rewatched.
    """
    path = parse_path(replay_heatmap_svg)
    time_points = []
    replay_scores = []
    for segment in path:
        if isinstance(segment, svgpathtools.path.CubicBezier):
            for t in [0, 0.25, 0.5, 0.75, 1]:
                point = segment.point(t)
                x, y = point.real, point.imag
                time_in_video = x / 1000 * video_duration  # adjust normalization
                replay_score = 100 - y  # adjust normalization
                time_points.append(time_in_video)
                replay_scores.append(replay_score)
    return list(zip(time_points, replay_scores))
