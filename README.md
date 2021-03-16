# audio-to-video

A Python project to convert a .mp3 audio file into a .mp4 video file. Used to convert podcast episodes into videos to upload to YouTube.

## To convert .mp3 into .mp4 using an image

Clone the repo and move into the main repo directory.

Create a conda env, activate and install ffmpeg:

```text
conda create -y -n audio-to-video
conda activate audio-to-video
conda install -y -c conda-forge ffmpeg gooey
```

Run the Gooey app:

```text
python run.py
```

If this doesn't work, the raw ffmpeg command is below:

```text
ffmpeg -loop 1 -i image.png -i audio.mp3 -c:a copy -c:v libx264 -shortest video.mp4
```
