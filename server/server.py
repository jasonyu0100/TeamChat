import traceback
import os
import sys
import certifi
from core.api.general import general_api

from sanic import Sanic
from sanic.response import text, json
from sanic_cors import CORS

# Setup server
app = Sanic(__name__)
# Timeout functions --> if request takes too long stop (server and client)
app.config["REQUEST_TIMEOUT"] = 30
app.config["RESPONSE_TIMEOUT"] = 30
# API endpoints --> add routes as a collection in one go
app.blueprint(general_api)
# App wrapper --> authorised users only
CORS(app)

@app.listener("before_server_start")
async def init(app, loop):
    pass

@app.route("/")
async def home(request):
    return json({"message": """Welcome to the Team Chat API"""})


@app.exception(Exception)
def handle_errors(request, exception):
    try:
        status = exception.status_code
    except AttributeError:
        print(f"Exception in user code: {exception}")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)
        status = 500
    return text(
        str(exception),
        status=status,
        headers={"Access-Control-Allow-Origin": "*"}
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, workers=1)
