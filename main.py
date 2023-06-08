import json
import os

import uvicorn
from dotenv import load_dotenv
from src import app

load_dotenv()

HOST= os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
IS_DEV_ENV = os.getenv("ENV", "development").startswith("dev")
GET_OPENAPI_JSON = os.getenv("GET_OPENAPI_JSON", "false").lower() == "true"

if __name__ == "__main__":
    if GET_OPENAPI_JSON:
        if not os.path.isdir("./dist"): os.mkdir("./dist")
        with open("./dist/openapi.json", "w") as f:
            openapi_schema = app.openapi()
            f.write(json.dumps(openapi_schema))
            f.close()
            quit(0)
            
    uvicorn.run("src:app", host=HOST, port=PORT, reload=IS_DEV_ENV, )
