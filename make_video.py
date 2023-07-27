import os
import subprocess
from moviepy.editor import *
from pydub import AudioSegment
from moviepy.editor import TextClip


def calculate_n(image_folder, name):
    # Get the largest value of n based on image files
    image_files = os.listdir(image_folder)
    print(image_files)
    n = max([int(file.split(name)[1].split(".")[0]) for file in image_files])
    return n


def concatenate_audio_image(audio_folder, image_folder, output_folder):
    n = calculate_n(image_folder, "image")

    inputs = []

    for i in range(1, n + 1):  # Iterate over audio and image files
        image_filename = os.path.join(image_folder, f"image{i}.png")
        audio_filename = os.path.join(audio_folder, f"narration{i}.wav")

        inputs.append(ffmpeg.input(image_filename))
        inputs.append(ffmpeg.input(audio_filename))
    joined = (
        ffmpeg.concat(*inputs, v=1, a=1)
        .output(
            f"{output_folder}/output.mp4",
            vcodec="libx264",
            acodec="aac",
            pix_fmt="yuv420p",
            r=25,
        )
        .run()
    )


def generate_video():
    current_path = os.getcwd()
    image_path = os.path.join(current_path, "images")
    audio_path = os.path.join(current_path, "audio")
    n = calculate_n(image_path, "story")
    audio_folder = os.path.join(audio_path, f"story{n}")
    image_folder = os.path.join(image_path, f"story{n}")
    output_folder = os.path.join(current_path, "output")

    num_files = len(os.listdir(audio_folder))

    clips = []

    for i in range(1, num_files + 1):
        audio_path = f"{audio_folder}/narration{i}.mp3"
        image_path = f"{image_folder}/image{i}.png"
        audio = AudioSegment.from_mp3(audio_path)
        duration = len(audio) / 1000  # pydub calculates in millisec
        img_clip = ImageClip(image_path, duration=duration)
        img_clip = img_clip.set_audio(AudioFileClip(audio_path))
        clips.append(img_clip)

    final_clip = concatenate_videoclips(clips)

    final_clip.write_videofile(
        os.path.join(output_folder, "final_video.mp4"), codec="libx264", fps=24
    )
    return os.path.join(output_folder, "final_video2.mp4")
