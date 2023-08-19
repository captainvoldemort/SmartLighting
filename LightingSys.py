# Import required libraries
import cv2
import os
import RPi.GPIO as GPIO
import time

# Set up Raspberry Pi GPIO
GPIO.setmode(GPIO.BOARD)

# Define PIR and relay pins
pir_pin = 18
relay_pin = 36

# Set up GPIO pins for input and output
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(relay_pin, GPIO.OUT)

# Define image paths and capture interval
image_path = './CAPTURED_IMAGES/image_cache.jpg'
save_location = "./CAPTURED_IMAGES"
capture_interval = 10  # seconds

# Capture image function
def capture_image():
    cap = cv2.VideoCapture(0)  # Open the default camera
    ret, frame = cap.read()    # Capture a frame
    cap.release()              # Release the camera
    save_path = os.path.join(save_location, "image_cache.jpg")
    cv2.imwrite(save_path, frame)  # Save the image

def detect_humans():
    image = cv2.imread(image_path)  # Read the image
    hog = cv2.HOGDescriptor()       # Initialize the HOG descriptor
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (humans, _) = hog.detectMultiScale(image, winStride=(10, 10), padding=(32, 32), scale=1.1)
    print('Human Detected:', len(humans))
    return len(humans)

def count_faces():
    image = cv2.imread(image_path)  # Load the input image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Load the face detector
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)  # Detect faces
    print('Faces Detected:', len(faces))
    return len(faces)

def pir():
    try:
        while True:
            if GPIO.input(pir_pin):
                motion_state = True
                print('Motion Detected')
                return motion_state
    except KeyboardInterrupt:
        GPIO.cleanup()

while True:
    is_motion = False
    light_state = 'OFF'
    is_motion = pir()
    
    if is_motion:
        GPIO.output(relay_pin, True)  # Turn on lights
        light_state = 'ON'
    else:
        GPIO.output(relay_pin, False)  # Turn off lights
        light_state = 'OFF'
    
    '''
    Algorithm:
    1. Check for Motion using PIR
    2. If motion == True, turn on lights and set light_state to 'ON'
    3. Otherwise, continue monitoring
    4. If light_state == 'ON', perform the following checks:
        a. Capture an image
        b. Detect the number of humans using HOG
        c. Detect the number of faces using Haar cascades
        d. Wait for the specified interval
        e. If no humans and no faces are detected:
    - Turn off lights
        #- Update light_state to 'OFF' (Optional: As it's already OFF)
    '''
    while light_state == 'ON':
        capture_image()
        num_humans = detect_humans()
        num_faces = count_faces()
        cv2.waitKey(capture_interval * 1000)  # Wait for the specified interval
        
        if num_faces == 0 and num_humans == 0:
            GPIO.output(relay_pin, False)  # Turn off lights
            #light_state = 'OFF'
