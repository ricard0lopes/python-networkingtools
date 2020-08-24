import urllib.request

"""
Access URL
"""

print("Downloading html code from python.org ...")
# create headers variable
headers = {}
# define user agent
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"

# make a request to python.org (download html code)
r = urllib.request.Request("https://www.python.org", headers=headers)
# store the html code in the html variable
html = urllib.request.urlopen(r).read()
# create the file to write the html code
f_name = "pythonorg.txt"
_file = open(f_name, "w+")
_file.write(html.decode())
_file.close()
print("Download Complete.")

"""
Downloading FIles
"""

print("\n\nDownloading wordpress...")
# make a request to wordpress.org
rsp = urllib.request.urlopen("https://wordpress.org/latest.zip")
# read the response and store it into the data variable
data = rsp.read()

# create a file to write the wordpress data
filename = "latest.zip"
file_ = open(filename, "wb")
# write the data into the file
file_.write(data)
# close the file
file_.close()
print("Download Complete.")
