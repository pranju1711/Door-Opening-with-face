import cv2 # type: ignore
import os

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Create 'datasets' directory if it doesn't exist
if not os.path.exists("datasets"):
    os.makedirs("datasets")

# Ask for user ID
user_id = input("Enter user ID :")

# Start webcam
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]

        # Save image in datasets folder
        cv2.imwrite(f"datasets/user.{user_id}.{count}.jpg", face)

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Capturing Faces", frame)

    # Break after 50 images
    if count >= 50:
        break

    if cv2.waitKey(1) == 27:  # ESC key to stop
        break

cap.release()
cv2.destroyAllWindows()
print("Dataset collection complete.")
