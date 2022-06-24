from sanic import Blueprint, response
general_api = Blueprint("general_api", url_prefix="/api")


@general_api.get("/")
async def home(request):
    """
    Home API Route
    """
    return response.text("Welcome to the Vidup API")


@general_api.post("/hello_world")
async def hello_world(request):
    """
    Generates Text based on prompt
    """
    text = str(request.body, "utf-8")

    hello_world = f"hello {text}"
    return response.text(hello_world)