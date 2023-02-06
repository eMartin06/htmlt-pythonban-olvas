import urllib.request
import sys

def download_function(url):
    try:
        #now we download the content from url:
        content = urllib.request.urlopen(url)
        page_content = content.read()
        #now we write the content to a file
        file = open("page_content.txt",'wb')
        file.write(page_content)
        file.close()
        print("Content download successfully")
    except:
        print("Something went wrong")

url = input("Please insert the url")
download_function(url)