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

# convert image from numpy array to string
x = thompson_encoding.dumps()

# convert from string to numpy array
y = np.loads(x)

# Retrieve record from database
mycursor = conn.mydb.cursor()
mycursor.execute("SELECT * FROM `users` WHERE id=10")
myresult = mycursor.fetchone()

# Retrieve column with encoded image which is a blob
thompson_encoding_db = myresult[3]
print(np.array_equal(thompson_encoding, np.loads(thompson_encoding_db)))

# save the details to the database
"""
Since its an numpy array convert to string to save to database --- x = thompson_encoding.tostring() 
When fetched convert back to array --- np.fromstring(x, dtype=float) or np.loads(x)
"""

# save thompson
sql = """INSERT INTO `users` (`name`, `image_name`, `encoded_image`) VALUES (%s, %s, %s)"""
val = ('Thompson', 'thompson.jpeg', thompson_encoding.dumps())
mycursor.execute(sql, val)
conn.mydb.commit()
print("Last record id", mycursor.lastrowid)

# save thor
sql = """INSERT INTO `users` (`name`, `image_name`, `encoded_image`) VALUES (%s, %s, %s)"""
val = ('Thor', 'thor.jpeg', thor_encoding.tostring())
mycursor.execute(sql, val)
conn.mydb.commit()
print("Thor record id", mycursor.lastrowid)
