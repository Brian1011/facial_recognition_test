# import database file
import dbConnection as conn
import face_recognition
import numpy as np


# load the images
def load_images(image_name):
    return face_recognition.load_image_file("images/"+image_name)


# encode the faces
def face_encoding(loaded_image):
    return face_recognition.face_encodings(loaded_image)[0]


# examples
thompson = load_images('thompson.jpeg')
thor = load_images("thor.jpeg")

# encoded images
thompson_encoding = face_encoding(thompson)
thor_encoding = face_encoding(thor)

# save the details to the database
"""
Since its an numpy array convert to string to save to database
When fetched convert back to array
"""
mycursor = conn.mydb.cursor()

# thompson
# sql = "INSERT INTO `users` (`id`, `name`, `image_name`, `encoded_image`) VALUES (NULL, 'Thompson', 'thompson.jpeg', '[ss]')"
print(type(thompson_encoding))
x = thompson_encoding.tostring()
print(len(x))
print(np.fromstring(x, dtype=float))
print(thompson_encoding)
print(np.array_equal(np.fromstring(x, dtype=float), thompson_encoding))
