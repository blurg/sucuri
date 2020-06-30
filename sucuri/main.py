from fastapi import FastAPI

def get_app():
    from .views import profile_view
    app = FastAPI()
    app.include_router(profile_view.router)
    return app
