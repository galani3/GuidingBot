#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import urllib.request
import os
from optparse import OptionParser

#Initiate options for user to use
parser = OptionParser()
parser.add_option("-u", "--url", type="string", dest="url", help="URL link to retrieve images from")
parser.add_option("-i", "--index", type = "int", dest="index", help="Specify index to start numbering images")
parser.add_option("-p", "--prefix", type="string", dest="prefix", help="Specify prefix to name images under")
(options, args) = parser.parse_args()

#Check if user provided any index
if options.index == None:
    img_number = 1
else:
    img_number = options.index

#Retrieve images as long as a URL and a prefix name is provided
if options.prefix != None and options.url != None:

    if not os.path.exists('retrieved_negatives'):
        os.makedirs('retrieved_negatives')
        
    prefix_name = options.prefix
    url_link = options.url

    response = urllib.request.urlopen(url_link).read().decode()
    split_response = response.split('\n')

    for number in range(0, 2000):
        print(split_response[number].replace('\r', ''), end=' ')
        try:
            urllib.request.urlretrieve(split_response[number], 'retrieved_negatives/' + prefix_name + str(img_number) + '.jpg')
            print("OK", end=' ')
            print(prefix_name + str(img_number) + '.jpg')
            img_number += 1
        except urllib.error.URLError as e:
            print(e.reason)

#Check if the prefix or URL is missing if not provided
else:       
    if options.url == None:
        print("Provide a URL to retrieve images from")
    if options.prefix == None:
        print("Provide a name to save images under")
