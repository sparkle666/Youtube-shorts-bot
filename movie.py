import ffmpeg
from ffprobe import FFProbe
  
v_width = 1080
v_height = 1633

def run_video():
    overlay1 = ffmpeg.input("sukuna.gif").filter("scale", 1080, -1, height = 1633 / 2)
    overlay2 = ffmpeg.input("akaza_long.mp4").filter("scale", 1080, -1, height = 1633 / 2 )
    (
    ffmpeg.input('letsgo.mp4')
    .overlay(overlay1)
    .overlay(overlay2, x = 0, y = v_height / 2)
    .drawtext(textfile = "char_names.txt", fontfile = "/storage/emulated/0/PyFiles/Helvetica-Bold.ttf", fontcolor = "yellow", bordercolor = "black", escape_text = True, start_number = 0, fontsize = "80", x = (v_width / 2) - 130, y = v_height / 2.3, borderw = 4, line_spacing = 3)
    .output("newVideo.mp4")
    .run()
    )
    
def get_video_data(file_name = "akaza1.mp4"):
    metadata = FFProbe(file_name)
    for stream in metadata.streams:
        if stream.is_video():
            print('Stream contains {} frames.'.            format(stream.frames()))
            print(f"Duration {stream.duration}, seconds : {stream.is_audio}")
            return stream.width, stream.height, stream.duration

def make_longer():
  w, h, duration = get_video_data()
  if int(float(duration)) < 2.3:
    print("Video duration is too short...")

def concat_video(video1, video2):
  second_video = ffmpeg.input(video2)
  ffmpeg.input(video1).concat(second_video).output("added.mp4").run()
  print("added success...")
# make_longer()
# get_video_data()
# print(f'Height {h} Width {w}')
run_video()  

# concat_video("akaza_long.mp4", "akaza_long.mp4")

