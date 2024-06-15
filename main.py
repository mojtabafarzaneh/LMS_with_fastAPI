from fastapi import FastAPI

app = FastAPI(
    title="Fast API MLS",
    description="MLS for managing studants and courses",
    version="0.0.1",
    license_info={
        "name": "MIT"
    },
)


@app.get("/users")
async def get_user():
    return {"message": "welcome"}
