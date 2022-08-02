import csv
from blogs.models import Blogs


def run():
    fhand = open('blogs/gym.csv')
    reader = csv.reader(fhand)
    next(reader)

    for row in reader:
        print(row)
        r = Blogs(sku=row[1], title=row[2],  short_description=row[3], price=row[4],
                  product_image=row[7])
        r.save()
