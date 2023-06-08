import json
import os

from src import app

if __name__ == "__main__":
    if not os.path.isdir("./dist"): os.mkdir("./dist")
    with open("./dist/openapi.json", "w") as f:
        openapi_schema = app.openapi()
        f.write(json.dumps(openapi_schema))
        f.close()
        quit(0)
            
