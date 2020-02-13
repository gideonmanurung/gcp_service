import json
import base64
import requests
import binascii
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def google_ocr(image_b64):
    """[Function for extract text from image using google OCR]
    
    Arguments:
        image_b64 {[string]} -- [String of base64 image]
    
    Returns:
        text_annotation[string] -- [Extracted text from image]
    """    

    uri = "" # API for Google OCR
    header = {
        'Content-type': 'application/json'
    }
    
    payload = {}
    
    image = {}
    image['image'] = {}
    image['image']['content'] = image_b64
    image['features'] = []
    
    feature = {}
    feature['type'] = "TEXT_DETECTION"
    image['features'].append(feature)
    
    request_image = []
    request_image.append(image)
    payload['requests'] = request_image
    
    response = requests.request("POST", uri, data=json.dumps(payload), headers=header)

    response_json = json.loads(response.text)
    response = response_json['responses'][0]

    """
    text_annotation = response['fullTextAnnotation']['text']
    if 'textAnnotations' in response.keys():
        text_annotation = response['fullTextAnnotation']['text']
    else:
        text_annotation = 

    return text_annotation
    """
    return response