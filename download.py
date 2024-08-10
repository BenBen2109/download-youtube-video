import pytubefix
from moviepy.editor import VideoFileClip


def download_and_cut_video(url, video_name):
  """Downloads a YouTube video and cuts it to 10 seconds if longer."""

  try:
    # Download the video
    yt = pytubefix.YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream is None:
      return
    stream.download(output_path='./input', filename= video_name)


    # Get the video file name
    video_file = f'./input/{video_name}'

    # # Get video duration
    # clip = VideoFileClip(video_file)
    # duration = clip.duration

    # # Cut the video if it's longer than 10 seconds
    # if duration > 10:
    #   new_clip = clip.subclip(0, 10)
    #   new_clip.write_videofile("cut_" + video_file)
    #   print("Video cut to 10 seconds.")
    # else:
    #   print("Video is already shorter than 10 seconds.")

  except Exception as e:
    print("An error occurred:", e)

# Example usage
url = "https://www.youtube.com/watch?v=yaBMNgAcBWA"
name = "gif2.mp4"
download_and_cut_video(url, name)