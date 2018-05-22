import urllib
import os

component_name = "button"
dir_name = component_name
if os.path.exists(dir_name) is False:
    os.mkdir(dir_name)
file_name = "buttonrow"
file_location = dir_name + '/' + file_name
print "stuff"
filelocation = "button"
urllib.urlretrieve("https://s3-us-west-2.amazonaws.com/figma-alpha/img/07d9/7d3a/90fbb68293137eccb1f95320e33e8598", file_location+".jpeg")

