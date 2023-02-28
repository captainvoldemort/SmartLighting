# import required libraries
import cv2
import os

#defining paths
image_path = 'C:\\Users\\yasht\\OneDrive\\Desktop\\SmartLighting\\image1.jpg'
save_location = "C:\\Users\\yasht\\OneDrive\\Desktop\\SmartLighting\\Images"

#capture image function
def capture_image():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Capture a frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Save the image as "image1.jpg" in the specified location
    save_path = os.path.join(save_location, "image1.jpg")
    cv2.imwrite(save_path, frame)

def detect_humans():
    # Reading the Image
    image = cv2.imread(image_path)

    # initialize the HOG descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # detect humans in input image
    (humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
    padding=(32, 32), scale=1.1)

    # getting no. of human detected
    print('Human Detected : ', len(humans))

    return len(humans)
    # # loop over all detected humans
    # for (x, y, w, h) in humans:
    #    pad_w, pad_h = int(0.15 * w), int(0.01 * h)
    #    cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

    # # display the output image
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def count_faces():
    # Load the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the face detector (Haar cascades)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    print('Faces Detected : ', len(faces))
    # Return the number of faces found
    return len(faces)
capture_image()
detect_humans()
count_faces()