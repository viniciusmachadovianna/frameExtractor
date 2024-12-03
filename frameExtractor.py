import cv2 #pip install opencv-python
import os

video_path = 'demo.mp4'
cap = cv2.VideoCapture(video_path)

output_dir = 'frames/'+os.path.splitext(video_path)[0]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    fps = 1
    if frame_count % fps == 0:
        frame_filename = os.path.join(output_dir, f"frame_{frame_count}.png")
        cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
print(f"{video_path} frames > '{output_dir}'")
