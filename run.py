"""
run.py

This script produces a GUI window that converts a .mp3 audio file and an image
into a .mp4 video

@author: peter.kazarinoff
"""

from pathlib import Path
import subprocess

from gooey import Gooey, GooeyParser


@Gooey(dump_build_config=True, program_name="Audio to Video Conversion Tool")
def main():
    desc = "A Python GUI App to convert a .mp3 and an image into a .mp4"
    mp3_select_help_msg = "Select a .mp3 audio file to process"
    image_select_help_msg = "Select an image file (.png or .jpg) to use in the video"

    my_parser = GooeyParser(description=desc)
    my_parser.add_argument(
        "mp3_to_convert", help=mp3_select_help_msg, widget="FileChooser"
    )
    my_parser.add_argument(
        "image_to_convert", help=image_select_help_msg, widget="FileChooser"
    )
    my_parser.add_argument(
        "output_dir", help="Directory to save output", widget="DirChooser"
    )

    args = my_parser.parse_args()

    # construct the .mp3 input audio file path
    mp3_to_convert_Path = Path(args.mp3_to_convert)

    # construct image file path
    image_to_convert_Path = Path(args.image_to_convert)

    # construct output .mp4 file path
    mp4_outfile_name = str(mp3_to_convert_Path.stem) + ".mp4"
    mp4_outfile_Path = Path(args.output_dir, mp4_outfile_name)

    # Determine ffmpeg executable file path
    """
    where ffmpeg
    """
    ffmpeg_path_bytes = subprocess.check_output(
        "where ffmpeg", shell=True
    )  # returns bytes
    ffmpeg_executable_path = ffmpeg_path_bytes.decode().strip()
    print("ffmpeg_executable_path: ", ffmpeg_executable_path)

    # create the ffmpeg command
    """
    ffmpeg -loop 1 -i image.png -i audio.mp3 -c:a copy -c:v libx264 -shortest video.mp4
    """

    ffmpeg_command = f"-loop 1 -i {image_to_convert_Path} -i {mp3_to_convert_Path} -c:a copy -c:v libx264 -shortest {mp4_outfile_Path}"
    cmd_command = f"{ffmpeg_executable_path} {ffmpeg_command}"

    print(f"input .mp3 file \n {mp3_to_convert_Path}")
    print()
    print(f"input image file \n {image_to_convert_Path}")
    print()
    print(f"output .mp4 file \n {mp4_outfile_Path}")
    print()
    print("cmd prompt command: ")
    print()
    print(cmd_command)

    # call ffmpeg
    returned_value = subprocess.call(
        cmd_command, shell=True
    )  # returns the exit code in unix
    print("returned value:", returned_value)


if __name__ == "__main__":
    main()
