import csv
from application import db
from application.models import *

import csv
from application import db
from application.models import Players

db.drop_all()
db.create_all()

with open('players.csv') as playaz:
    csv_reader = csv.reader(playaz, delimiter=",")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count+=1
        else:
            db.session.add(Players(
                Name = row[1],
                Club = row[2],
                League = row[3],
                Position = row[4],
                Rating = int(row[5])
            ))
            db.session.commit()