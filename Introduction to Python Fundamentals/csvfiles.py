#
# https://docs.python.org/3/library/csv.html 
#

import csv
with open('test.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print('|'.join(row))



# reading a csv from a URL. Works but not for google or dropbox, because they will reformat it for vieing in a browser

import csv
import io
import urllib.request

url = "https://raw.github.com/datasets/gdp/master/data/gdp.csv"
url = 'https://drive.google.com/open?id=0BzBVcktvddLkaXJTWEpDMno2bTQ'
url = 'https://www.dropbox.com/s/4xnzewhp22ncbu0/data.csv?dl=0'
webpage = urllib.request.urlopen(url)
datareader = csv.reader(io.TextIOWrapper(webpage))
for row in datareader:
    print(row)




# dropbox file download
# https://stackoverflow.com/questions/39984800/downloading-a-file-using-the-dropbox-python-library

import dropbox
access_token = '0BzBVcktvddLkaXJTWEpDMno2bTQ'
dbx = dropbox.Dropbox(access_token)

with open("Test.csv", "w") as f:
    metadata, res = dbx.files_download(path="Test.csv")
    f.write(res.content)


# for csv stored on google drive. This is for python 2.x need to fix it

import requests
import csv    
import io

headers={}
headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
headers["DNT"]= "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Encoding"] = "deflate"
headers["Accept-Language"]= "en-US,en;q=0.5"
lines = []

file_id="19Y_Oi5_riecwonPbtxN4sfDntZO62s_vJbXoogFFp9o"
url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)

r = requests.get(url)

data = {}
cols = []

sio = io.StringIO( r.text, newline=None)
reader = csv.reader(sio, dialect=csv.excel)
rownum = 0

for row in reader:
    if rownum == 0:
        for col in row:
            data[col] = ''
            cols.append(col)

    else:
        i = 0
        for col in row:
            data[cols[i]] = col
            i = i +1

        print(data)
    rownum = rownum + 1

