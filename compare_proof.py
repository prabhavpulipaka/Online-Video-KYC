import cv2
import dlib

# Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load face recognition model
face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load images
image1_path = "image1.jpg"
image2_path = "image2.jpg"

# Read images
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Detect faces
faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Extract face embeddings
face_descriptors1 = []
for (x, y, w, h) in faces1:
    face = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
    face_descriptor = face_recognizer.compute_face_descriptor(image1, face)
    face_descriptors1.append(face_descriptor)

face_descriptors2 = []
for (x, y, w, h) in faces2:
    face = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
    face_descriptor = face_recognizer.compute_face_descriptor(image2, face)
    face_descriptors2.append(face_descriptor)

# Compare face descriptors
if face_descriptors1 and face_descriptors2:
    # Assuming only one face is detected in each image
    distance = dlib.vector(face_descriptors1[0]) - dlib.vector(face_descriptors2[0])
    similarity = dlib.length(distance)
    if similarity < 0.6:  # Adjust threshold based on your requirement
        print("Images belong to the same person.")
    else:
        print("Images belong to different persons.")
else:
    print("No face detected in one or both images.")