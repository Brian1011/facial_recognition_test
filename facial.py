import face_recognition
from PIL import Image

# load image name
image = face_recognition.load_image_file("images/1.jpg")

# recognise faces and their locations (coordinates)
face_locations = face_recognition.face_locations(image)

print(face_locations)
print(type(face_locations))
print("Faces found ", len(face_locations))

'''
To crop your image, you need top-left and right-bottom coordinates (top, left, right, bottom)
our face locations is organized differently (top, right, bottom, left)
'''
for face_location in face_locations:
    # get the coordinates of the image
    top, right, bottom, left = face_location

    # Extract the region of the image that contains the face
    face_image = image[top:bottom, left:right]
    img = Image.fromarray(face_image)
    img.show()

