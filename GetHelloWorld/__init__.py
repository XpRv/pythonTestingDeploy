import logging, json

import azure.functions as func
from services.todo_service import get_incidents

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    title = req.params.get('title')
    if not title:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            title = req_body.get('title')

    if title:
            logging.info('Python HTTP trigger function processed a request for title ${title}.')

            data = get_incidents()
            return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a title in the query string or in the request body for a personalized response.",
             status_code=200
        )
