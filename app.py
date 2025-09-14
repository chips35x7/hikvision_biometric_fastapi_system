# import json

from fastapi import FastAPI, Request, Response
# from datetime import datetime

app = FastAPI()

LOG_FILE = 'fingerprint_logs.json' # Json file that will hold data during testing
# !!!NOTE: After Initial tests with json are successfull, will switch to SQLITE/MYSQL OR free SUPABASE POSTGRES ClOUD DB for final test presentation!!! 

@app.post('/fingerprint-event')
async def receive_event(request:Request):
    """Demo API to simulate erp endpoint for biometric system"""
    try:
        body = await request.body()
        content_type = request.headers.get('content-type')
        print(f'Received POST Request | Content-Type: {content_type}')
        print(body.decode())
        # !!! COME BACK HERE TO SIMULATE DATA LOGGING IN JSON FILE AFTER INITIAL TESTING IS SUCCESSFUL!!!
        with open('response.xml') as file:
            xml_response = file.read()

        return Response(content=xml_response, media_type='application/xml')
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
            }
