import urllib, sys, httplib, os
from urlparse import urlparse

MAX = 2913

def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400

def makeLink(i):
    string = str(i)
    num = "0002"

    if len(string) <= 1:
        num = "000" + str(i)
    elif len(string) == 2:
        num = "00" + str(i)
    elif len(string) == 3:
        num = "0" + str(i)
    elif len(string) == 4:
        num = str(i)

    return "http://tutorial-haartraining.googlecode.com/svn/trunk/data/negatives/neg-" + num + ".jpg"

def getImages(i):
    if i > MAX:
        i = MAX

    i = i + 2
    num = 2

    if not os.path.exists("negative_images/"):
        os.makedirs("negative_images/")

    while num < i:
        theURL = makeLink(num)

        if checkUrl(theURL) is True:
            perc = 100 * float(num) / float(i)
            sys.stdout.write("Download progress: %d%%   \r" % (perc) )
            sys.stdout.flush()
            urllib.urlretrieve(theURL, "negative_images/neg-" + str(num) + ".jpg")
            num += 1
        else:
            num += 1
            i += 1

    print "Finished: " + str(num) + " images downloaded."

getImages(600)
