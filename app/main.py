from fastapi import FastAPI, Request
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/")
async def get_time_and_ip(request: Request):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.client.host
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
