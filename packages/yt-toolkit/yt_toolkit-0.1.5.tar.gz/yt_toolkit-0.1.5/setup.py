from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="yt_toolkit",
    version="0.1.5",
    description="A library for retrieving and processing YouTube data (API, scraping, transcripts, heatmaps).",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MartaAlet/yt-toolkit",
    author="MartaAlet",
    author_email="m.aletpuig@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "google-api-python-client>=2.0.0",
        "google-auth>=2.0.0",
        "selenium>=4.0.0",
        "beautifulsoup4>=4.9.0",
        "lxml>=4.6.0",
        "youtube_transcript_api>=0.4.0",
        "svgpathtools>=1.4.0",
        "trio-websocket==0.11.1",
    ],
    python_requires=">=3.11",
)
