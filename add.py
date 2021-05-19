import csv
import sys
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('postgresql://postgres:asifnadish@localhost:5432/img', echo=True)        ## img is the name of database on which your image is stored
db=scoped_session(sessionmaker(bind=engine))                                                    ## "asifnadish" is my password and you can use your password

def readImage():
    fin = open("asif.jpg", "rb")
    img = fin.read()
    return img

   

data = readImage()
binary = psycopg2.Binary(data)                                                                  ## converting the image into binary format
db.execute("INSERT INTO images(img_data) VALUES (:bin)", {"bin":binary} )
db.commit()