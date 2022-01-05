import urllib.request
import json

while True:
    ballposx = float(input("Enter X Coordinate of ball: "))
    if ballposx == 999999:
        break
    ballposy = float(input("Enter Y coordinate of ball: "))
    paddlepos = float(input("Enter Y coordinate of paddle: "))
    gradient = str(input("Enter direction which ball is travelling: "))
    if (gradient.upper == "UP"):
        gradient = 0.4
    else:
        gradient = -0.4
        
    data = {
            "Inputs": {
                    "input1":
                    [
                        {
                                'ballposx': ballposx,   
                                'ballposy': ballposy,   
                                'paddlepos': paddlepos,   
                                'gradient': gradient,   
                                'value': "0",   
                        }
                    ],
            },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/48af135904464923b9e7302995639f8f/services/0a9c64eed01a4da9b4ca30537bea37db/execute?api-version=2.0&format=swagger'
    api_key = '0d3Nsv2U9uy5pVFmACJSetWcUTHtg6qZdPFyUOK8EClzUVzWEy+hxXFIpMUeA+AJcTDnxuskf32+AfLyZ7bNVg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        display = json.loads(result)
        value = round(float(display['Results']['output1'][0]['Scored Labels']))
        if value == 1:
            print("Move Up")
        else:
            print("Move Down")
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
