from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.routing import Match
from palcodeinfra.database import Database
from sqlalchemy.orm import Session
from sqlalchemy import text

class TenantIdMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, excluded_paths):
        super().__init__(app)
        self.excluded_paths = excluded_paths

    async def IsTenantIdValid(self, tenant_id):        
        DATABASE_URL = "postgresql+psycopg://palcode:Palcode!1234!!#$@palcode.ca6uzdsmv6p2.ap-south-1.rds.amazonaws.com:5432/tenants"     
        db_object = Database(DATABASE_URL)
        db_engine = db_object.get_engine()
        with db_engine.connect() as connection:
            query = text("SELECT 1 FROM tenant.tenant WHERE tenant_id = :tenant_id LIMIT 1")
            result = connection.execute(query, {"tenant_id": tenant_id})
            rows = result.fetchone()
            return rows is not None

    async def dispatch(self, request: Request, call_next):

        if any(request.url.path.startswith(path) for path in self.excluded_paths):
            return await call_next(request)
        
        tenant_id = request.headers.get("X-Tenant-ID")
        
        if not tenant_id:
            return JSONResponse(status_code=400, content={"detail": "Missing X-Tenant-ID header"})        
        
        result = await self.IsTenantIdValid(tenant_id)
        if not result:
            return JSONResponse(status_code=403, content={"detail": "Invalid X-Tenant-ID header value"})
        
        request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
    
