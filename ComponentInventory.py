import argparse
import requests
import random
import json
# from PIL import Image
# from io import BytesIO

BLOCK_W = 8
BLOCK_H = 8


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
            component_name = i["name"]
            name_list = component_name.split("/")
            name_and_id = [component_name, i["id"]]
            if name_list[0] in component_types:
                component_types[name_list[0]].append(name_and_id)
            else:
                component_types[name_list[0]] = [name_and_id]

        else:
            print "not component"
    print component_types

        
