from agents.cleo import cleo_response
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create an instance of FastAPI.
app = FastAPI()

#Defining the request BaseModel using pydantic.
class MessageRequest(BaseModel):
    message: str

# Root endpoint.
@app.get("/")
def read_root():
    return {"message": "Mainframe."}

# Gets the response from Cleo.
@app.post("/get-cleo-response")
async def get_cleo_response(request: MessageRequest):
    llm_response = cleo_response(request.message)
    return {"response": llm_response}

# Run the API.
if __name__ == "__main__":
    uvicorn.run("main_cleo_api:app", host="127.0.0.1", port=8000, reload=True)
