from fastapi import FastAPI, Request, HTTPException, Depends
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from starlette.routing import Match

class UserIdMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, valid_user_ids, excluded_paths):
        super().__init__(app)
        self.valid_user_ids = valid_user_ids
        self.excluded_paths = excluded_paths

    async def dispatch(self, request: Request, call_next):
        if any(request.url.path.startswith(path) for path in self.excluded_paths):
            return await call_next(request)
        
        user_id = request.headers.get("X-User-ID")
        
        if not user_id:
            return JSONResponse(status_code=400, content={"detail": "Missing X-User-ID header"})
        
        if user_id not in self.valid_user_ids:
            return JSONResponse(status_code=403, content={"detail": "Invalid X-User-ID header value"})
        
        request.state.user_id = user_id
        response = await call_next(request)
        return response