import argparse
import requests
import random
import json

API_TOKEN = "1228-0ed0d8c1-39c7-4245-b15b-f8c2058713d7"
headers = {'X-Figma-Token': API_TOKEN}

parser = argparse.ArgumentParser(description='Draw an image with Figma symbols.')
parser.add_argument('file_key', type=str, help='file key from Figma for symbols')
args = parser.parse_args()
guid = '0:381'

url = "https://api.figma.com/v1/images/{}?ids={}&format=png&scale=0.0625".format(args.file_key, guid)
resp = requests.get(url, headers=headers)

imageURL = resp.json()['images'][guid]