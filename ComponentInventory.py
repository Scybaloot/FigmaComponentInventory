import argparse
import requests
import random
import json

#for downloading
import urllib
import os

def download(component_type, file_name, image_url):
    dir_name = component_type

    #check if directory exists
    if os.path.exists("components/" + dir_name) is False:
        os.mkdir("components/" + dir_name)

    #save image from url to component type directory
    file_location = "components/" + dir_name + '/' + file_name
    urllib.urlretrieve(image_url, file_location+".jpg")


if __name__ == '__main__':
    #get file_key variable from command line
    parser = argparse.ArgumentParser(description='Draw an image with Figma symbols.')
    parser.add_argument('file_key', type=str, help='file key from Figma for symbols')
    args = parser.parse_args()

    #make "components directory if it doesn't exist yet"
    if os.path.exists("components") is False:
        os.mkdir("components/")

    #set variables
    API_TOKEN = "1228-0ed0d8c1-39c7-4245-b15b-f8c2058713d7"
    url = "https://api.figma.com/v1/files/{}".format(args.file_key)
    headers = {'X-Figma-Token': API_TOKEN}

    #make call for JSON and process it
    resp = requests.get(url, headers=headers)
    string_response = resp.json()
    node_list = string_response.get("document").get("children")[0].get("children")

    #make dictionary for storing all the component info
    component_types = {}

    for i in node_list:
        if i["type"] == "COMPONENT":
            #get variables from JSON
            raw_component_name = i["name"]
            name_list = raw_component_name.split("/")
            guid = i["id"]

            #process variables from JSON to get component type and component name
            if len(name_list) > 1:
                component_type = name_list[0]
                component_name = "_".join(name_list[1:len(name_list)])
            else:
                component_type = name_list[0]
                component_name = name_list[0]

            #get URL for image file for each component
            url = "https://api.figma.com/v1/images/{}?ids={}&format=jpg&scale=1".format(args.file_key, guid)
            resp = requests.get(url, headers=headers)
            image_url = resp.json()['images'][guid]

            #download the image and provide name and type of component
            download(component_type, component_name, image_url)

            #output a dictionary of all the components, organized by component type
            name_and_id = [component_name, guid, image_url]
            if name_list[0] in component_types:
                component_types[name_list[0]].append(name_and_id)
            else:
                component_types[name_list[0]] = [name_and_id]

        else:
            print "not component"
    print component_types

        
