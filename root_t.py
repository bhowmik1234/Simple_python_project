import csv
from gmplot import gmplot

g_map = gmplot.GoogleMapPlotter(28.68435, 77.435345)

 gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv', 'r') as p:
    reader = csv.reader(p)
    k = 0
    for row in reader:
       lat = float(row[0])
       long = float(row[1])
    
    if(k == 0):
       gmap.marker(lat, long, 'yellow')
       k = 1
    else:
       gmap.marker(lat, long, 'blue')

gmap.marker(lat, long, 'red')
gamp.draw("mymap.html")