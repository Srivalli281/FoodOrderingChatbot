from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()

inprogress_orders = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    
    if intent=="track.order-context:ongoing-tracking":
        print(parameters)
        #return track_order(parameters)
        return JSONResponse(content={
            "fullfillmentText": f"Received=={parameters}==in the backend"
            #"fulfillmentText":f"Received=={parameters}==in the backend"
            
        })
        
def track_order(parameters: dict):
    order_id = int(parameters['order_id'])
    order_status = db_helper.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })