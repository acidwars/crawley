#!/usr/bin/env python3.5
import requests
import crowley
import re
import os,getopt,sys
""" Pr0l0ader """
BASE = 'https://pr0gramm.com'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:a", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-a":
            getcategorys(0)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()

def getcategorys(start):
    try:
        counter = 0
        for i in range(start, 210044, 60):
            url= 'https://pr0gramm.com/static/top/'+ str(i)
            print("[+] " + url)
            fetch(url)
            counter +=1
        print("Total downloads: " +counter)
    except KeyboardInterrupt:
        sys.exit(0)

def fetch(url):
    soup = crowley.crawlsite(url)
    for link in soup.find_all('a', href=re.compile('\/static\/\d{1,8}')):
        test = re.findall('\/static\/\d{1,8}', str(link))
        url = BASE+''.join(test)
        getlink(url)

def getlink(url):
    soup = crowley.crawlsite(url)
    for link in soup.find_all(['video', 'img']):
        download(link["src"])
        """
    for link in soup.find_all('image'):
        print("[+] found image!")
        print(link["src"])
        download(link["src"])"""

def download(url):
    try:
        url = 'https:' + url
        r = requests.get(url)
        name = re.findall('[a-z0-9]{4,}\.', url)
        typ = re.findall('[a-z0-9]+\.(mp4|jpg|gif|png)', url)
        try:
            filename = ''.join(name[1]+''.join(typ))
        except IndexError:
            print('Error with following URL!')
            print(url)
            print(name)
        if typ[0] == 'mp4':
            directory = 'clips/'
        else:
            directory = 'image/'
        if os.path.isfile(directory+filename) == True:
            print("  [-] Skipping " + filename)
        else:
            try:
                with open(directory + filename, "wb") as code:
                    code.write(r.content)
                print('  [-] Finished ' + str(filename))
            except UnboundLocalError:
                print('error :(')
    except KeyboardInterrupt:
        sys.exit(0)



getcategorys()
