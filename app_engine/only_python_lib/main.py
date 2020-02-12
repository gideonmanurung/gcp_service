import os
import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api_name', methods=['POST'])  # api_name is for specific api
def api_name():                            # function name is must same with api_name
    """Endpoint for recognizing the car plate (if any)
    
    Returns:
        [json] -- the result 
    """

    # ------------------------------ #
    # Handling for options method    #
    # ------------------------------ #
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
        }
        return ('', 204, headers)
    
    # ---------------------------- #
    # Set response header          #
    # ---------------------------- #
    headers = {}
    headers['Access-Control-Allow-Origin'] = '*'
    headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS, POST'
    headers['Access-Control-Allow-Credentials'] = 'true'
    headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    headers['Content-Type'] = 'application/json'


    response = {}
    response['data'] = {}
    
    try: 
        # ------------------------------ #
        # Get request data               #
        # ------------------------------ #
        json_data = request.get_json()

        # Create a process here
        # Set the response status before exit this function : 200 , 400 , 500

        response['status'] = 200
        response['data']['status'] = 'Success'
        response['message'] = 'Success to process request'
        

    except Exception as e:
        response['status'] = 410
        response['error'] = str(e)
        response['message'] = 'Failed to process request '

    return Response(json.dumps(response), mimetype='application/json', headers=headers)


if __name__ == "__main__":
    app.run(threaded=True)