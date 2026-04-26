from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() # initializing my API

fake_db = {
    1: {"name": "Alice", "role": "admin"},
    2: {"name": "Bob", "role": "user"}
}



# the @ symbol is a decorator that tells the API
# if someone visits the /users/{id} URL, run this specific function

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # We look up the user in the dictionary
    if user_id in fake_db:
        return fake_db[user_id]
    return {"error" : "User not found"}


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>My FastAPI Home</title>
        </head>
        <body>
            <h1>Welcome to my Homepage</h1>
            <p>This is being served directly from Python!</p>
        </body>
    </html>
        """



# To run this, use uvicorn firstapi:app --reload