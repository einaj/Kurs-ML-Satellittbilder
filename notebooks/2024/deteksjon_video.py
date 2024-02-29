from ultralytics import YOLO
import cv2
from PIL import Image
from pathlib import Path
import torch

if torch.cuda.is_available():
    device="cuda"
else:
    device="cpu"

# velg modell

model = YOLO("yolov8n.pt")

# sett path til videofil (støtter flere videoformater, mp4, avi, etc)
video = Path("path/til/video.mp4") # sett video=0 for å bruke webcam

# om videoen skal lagres
save_video = True
save_path = Path("videos/test.mp4")


# om deteksjonene skal vises frem underveis
show_video = False

cap = cv2.VideoCapture(str(video.absolute()))
grabbed, frame = cap.read() # les en frame
if not grabbed:
    print("Cannot read video")
    exit()


if save_video:
    save_path.parent.mkdir(parents=True,exist_ok=True)
    fps = cap.get(cv2.CAP_PROP_FPS)
    grabbed, frame = cap.read()
    h, w, c = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    print(f"Writing video to {str(save_path.absolute())}")
    video_writer = cv2.VideoWriter(str(save_path.absolute()), fourcc, fps, (w, h))


while grabbed:
    grabbed, frame = cap.read()
    # gjør til RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = model.predict(image,device=device)[0]

    out = result.plot()

    if show_video:
        cv2.imshow("detections",out)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    if save_video:
        video_writer.write(out)



video_writer.close()
cv2.destroyAllWindows()