# Convert Video to Gif
from moviepy import VideoFileClip

clip = VideoFileClip("10SecVid.mp4")
clip.write_gif("10SecVid.gif", fps=10)