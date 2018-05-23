import argparse
import requests
import random
import json

#for downloading
import urllib
import os

def download(component_name, file_name, image_url):
    dir_name = component_name
    if os.path.exists(dir_name) is False:
        os.mkdir(dir_name)
    file_location = dir_name + '/' + file_name
    urllib.urlretrieve(image_url, file_location+".jpg")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw an image with Figma symbols.')
    parser.add_argument('file_key', type=str, help='file key from Figma for symbols')
    args = parser.parse_args()

    API_TOKEN = "1228-0ed0d8c1-39c7-4245-b15b-f8c2058713d7"

    url = "https://api.figma.com/v1/files/{}".format(args.file_key)
    headers = {'X-Figma-Token': API_TOKEN}
    resp = requests.get(url, headers=headers)
    
    print "yas got the request"

    string_response = resp.json()
   # parsed_json = json.loads(string_response)
    node_list = string_response.get("document").get("children")[0].get("children")

    component_types = {}

    for i in node_list:
        if i["type"] == "COMPONENT":
            raw_component_name = i["name"]
            name_list = raw_component_name.split("/")

            guid = i["id"]
            #get URL for image file
            url = "https://api.figma.com/v1/images/{}?ids={}&format=jpg&scale=0.0625".format(args.file_key, guid)
            resp = requests.get(url, headers=headers)
            image_url = resp.json()['images'][guid]

            if len(name_list) > 1:
                component_type = i[0]
                component_name = "_".join(i[1:len(i)])
            else:
                component_type = i[0]
                component_name = i[0]

            download(component_types, component_name, image_url)

            name_and_id = [component_name, guid, image_url]
            if name_list[0] in component_types:
                component_types[name_list[0]].append(name_and_id)
            else:
                component_types[name_list[0]] = [name_and_id]

        else:
            print "not component"
    print component_types

        
