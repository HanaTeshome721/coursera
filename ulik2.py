import urllib.request
import ssl
from bs4 import BeautifulSoup


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter URL: ").strip()
count = int(input("Enter count: ").strip())
position = int(input("Enter position: ").strip())  


for i in range(count):
    print("Retrieving:", url)
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
 
    tags = soup('a')



    tag = tags[position - 1]
    url = tag.get('href', None)
    name = tag.text

print("The answer to the assignment for this execution is", f'"{name}".')
