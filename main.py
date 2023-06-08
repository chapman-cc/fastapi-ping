import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

HOST= os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
IS_DEV_ENV = os.getenv("ENV", "development").startswith("dev")

if __name__ == "__main__":
    uvicorn.run("src:app", host=HOST, port=PORT, reload=IS_DEV_ENV, )
