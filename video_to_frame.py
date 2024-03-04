import os
import cv2
from glob import glob

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, time_gap):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get the frame rate of the video
    frame_gap = int(time_gap * fps)  # Calculate the number of frames for the given time gap

    idx = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.release()
            break

        if idx % frame_gap == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "save"
    time_gap = 1  # Time gap in seconds

    for path in video_paths:
        save_frame(path, save_dir, time_gap)
