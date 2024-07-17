import argparse
import yt_dlp


def main(
    music_list_file_path: str,
    output_music_file_folder: str
):
    with open(music_list_file_path, 'r') as file:
        music_titles = [line.strip() for line in file]

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_music_file_folder + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    for title in music_titles:
        print(f"Searching and downloading: {title}")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([f"ytsearch1:{title}"])
            except yt_dlp.DownloadError as e:
                print(f"Failed to download {title}: {e}")

    print("Download complete.")


parser = argparse.ArgumentParser(
    prog='PyTubeToMusic',
    description='Download and convert youtube videos to music',
)

parser.add_argument('music_list_file_path')
parser.add_argument('output_music_file_folder')
args = parser.parse_args()

main(
    music_list_file_path=args.music_list_file_path,
    output_music_file_folder=args.output_music_file_folder
    
)
