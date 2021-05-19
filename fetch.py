import sys
import io
import psycopg2
from PIL import Image
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('postgresql://postgres:asifnadish@localhost:5432/img', echo=True)            ## img is the name of database on which your image is stored
db=scoped_session(sessionmaker(bind=engine))                                                        ## "asifnadish" is my password and you can use your password

img_data=db.execute("SELECT img_data FROM images").fetchall()
db.commit()

for row in img_data:
    img = io.BytesIO(row[0])
    img1=Image.open(img)
    img1.show()
