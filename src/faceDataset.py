import cv2
import os

cam = cv2.VideoCapture(0)  # first webcam
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter your user id and press <return> ==>  ')
face_firstname = input('\n Enter you first name and press <return> ==>  ')
face_lastname = input('\n Enter you last name and press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
directory = str(face_firstname)
parent_dir = 'dataset'
path = os.path.join(parent_dir, directory)
# print(path)
folderExists = os.path.exists(path)
if not folderExists:
    os.mkdir(path)
    # print("{} directory successfully created..".format(directory))
    # Initialize individual sampling face count
    count = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            print("\n [INFO] Capturing photos, Please stay steady..")
            # Save the captured image into the datasets folder
            # os.chdir(path) # to change the current directory
            imgName = str(face_firstname) + str(face_lastname) + str(count) + ".jpg", gray[y:y + h, x:x + w]
            cv2.imwrite(
                "dataset/{0}/{1}{2}{3}.jpg".format(str(face_firstname), str(face_firstname), str(face_lastname),
                                                    str(count)), gray[y:y + h, x:x + w])

            # cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            # cv2.imwrite('dataset'.format(str(face_firstname), imgName), img)
            if img is not None:
                print("Image successfully saved..")
            else:
                print("Unable to save image..")
            cv2.imshow('Image', img)
            cv2.imshow('GrayScale', gray)
        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 50:  # Take 50 face samples and stop video
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff..")
    cam.release()
    cv2.destroyAllWindows()
else:
    print("{} already exists,Try again with another person's face..".format(face_firstname))
    cam.release()
    cv2.destroyAllWindows()
