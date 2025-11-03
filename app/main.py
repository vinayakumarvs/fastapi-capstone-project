from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API", version="1.0.0")

# Link Middleware
app.add_middleware(LoggingMiddleware)

# Link Endpoints
app.include_router(routes_auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(routes_predict.router, prefix="/predict", tags=["Prediction"])

# Monitoring with Prometheus
Instrumentator().instrument(app).expose(app)

# Register Exception Handlers
register_exception_handlers(app)
