import csv
from blogs.models import Blogs


def run():
    fhand = open('blogs/blogs.csv', encoding="utf8")
    reader = csv.reader(fhand)
    next(reader)

    for row in reader:
        print(row)

        r = Blogs(title=row[1], decription=row[2],  readtiem=row[3],
                  authname=row[4], designation=row[5], image=row[6])
        r.save()
