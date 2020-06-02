# facial_recognition_test
This is a small system I created when I was experimenting with facial recognition technology.
The main objective was to be able to scan a face, generate a faceprint (unique features within each face like fingerprints), 
store the faceprint in a database(mysql) and retrieve the faceprints to compare with other face prints in future.

# How it works
Upload an image (images have to be within the images folder) with a one face, its then scanned, a face print is then stored in the database (mysql database). Once saved in the database, the next step is to compare an image with the data stored in the database. To achieve this upload or add the new image (you want to compare with) to the images folder. This new image is then scanned and a face print is generated, the system then fetches the face print from the database and compares with new image faceprint and checks for similarity.

# youtube link
This is a demo where I embedded a similar technology to an attendance system
https://www.youtube.com/watch?v=MC2kSAR3Ud4

# Note
This is a sample system that can help individuals looking into facial recognition technology to get started.
Have a nice coding experience :-)
