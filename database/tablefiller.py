import csv
from application import db
from application.models import Players

with open('FIFA20.csv') as playaz:
    csv_reader = csv.reader(playaz, delimiter=",")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count+=1
        else:
            db.session.add(Players(Name = row[0], Club = row[1], League = row[2], Position = row[3],
                    Tier = row[4], Rating = int(row[5]), Pace = int(row[5]),
                    Shooting = int(row[6]), Passing = int(row[7]), Dribbling = int(row[8]),
                    Defending = int(row[9]), Physical = int(row[10])))
            db.session.commit()

