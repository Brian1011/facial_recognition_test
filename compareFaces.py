# import database connection
import dbConnection as conn
import face_recognition
import numpy


# Retrieve the encoded image
def retrieveImage(user_id):
    mycursor = conn.mydb.cursor()
    sql = """SELECT * FROM `users` WHERE id=%(value)s"""
    params = {'value': user_id}
    mycursor.execute(sql, params)
    myresult = mycursor.fetchone()
    return myresult[3]


# get the encoded image of a particular individual
thompson_encoded_db = retrieveImage(17)

# convert the learnt image from the db to numpy array
thompson_encoded = numpy.loads(thompson_encoded_db)

# compare images
unknown_image = ""
thompson_images = ['thom1.png', 'thom3.jpg', 'thom4.jpeg', 'thor1.jpeg', 'ariana.jpeg', 'thor2.jpg']

for x in thompson_images:
    # load the unknown image
    load_image = face_recognition.load_image_file("images/unknown/"+x)

    # encode the image
    unknown_image_encoding = face_recognition.face_encodings(load_image)[0]

    # compare unkown image with the learnt model
    comparison_results = face_recognition.compare_faces([thompson_encoded],unknown_image_encoding)

    # the results is a list data type
    print("Results ", comparison_results[0])
