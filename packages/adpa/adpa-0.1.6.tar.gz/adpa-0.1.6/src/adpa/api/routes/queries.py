"""
Query routes.
"""
from typing import Optional
from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy import desc

from adpa.api.types import APIResponse
from adpa.api.routes.auth import get_current_user
from adpa.database.models import User, Query as QueryModel, QueryResult
from adpa.database.repository import Repository

router = APIRouter()

@router.post("/")
async def create_query(
    request: Request,
    natural_query: str = Query(..., description="Natural language query"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Create new query."""
    # Create query
    query = QueryModel(
        user_id=current_user.id,
        natural_query=natural_query,
        sql_query="",  # Will be generated
        status="pending"
    )
    
    # Save to database
    repo = Repository[QueryModel](request.state.db)
    query = repo.create(query)
    
    # TODO: Process query asynchronously
    
    return APIResponse(
        success=True,
        message="Query created",
        data={
            "id": str(query.id),
            "natural_query": query.natural_query,
            "status": query.status
        }
    )

@router.get("/{query_id}")
async def get_query(
    request: Request,
    query_id: str,
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Get query by ID."""
    repo = Repository[QueryModel](request.state.db)
    query = repo.get_by_id(query_id)
    
    if not query or query.user_id != current_user.id:
        return APIResponse(
            success=False,
            message="Query not found",
            error="Query not found or access denied"
        )
    
    return APIResponse(
        success=True,
        message="Query retrieved",
        data={
            "id": str(query.id),
            "natural_query": query.natural_query,
            "sql_query": query.sql_query,
            "status": query.status,
            "execution_time": query.execution_time,
            "row_count": query.row_count,
            "error_message": query.error_message,
            "created_at": query.created_at
        }
    )

@router.get("/")
async def list_queries(
    request: Request,
    current_user: User = Depends(get_current_user),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
) -> APIResponse:
    """List user queries."""
    repo = Repository[QueryModel](request.state.db)
    queries = repo.filter(
        {"user_id": current_user.id},
        order_by=[desc(QueryModel.created_at)],
        limit=limit,
        offset=offset
    )
    
    return APIResponse(
        success=True,
        message="Queries retrieved",
        data=[{
            "id": str(q.id),
            "natural_query": q.natural_query,
            "status": q.status,
            "created_at": q.created_at
        } for q in queries]
    )

@router.get("/{query_id}/results")
async def get_query_results(
    request: Request,
    query_id: str,
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Get query results."""
    # Get query
    query_repo = Repository[QueryModel](request.state.db)
    query = query_repo.get_by_id(query_id)
    
    if not query or query.user_id != current_user.id:
        return APIResponse(
            success=False,
            message="Query not found",
            error="Query not found or access denied"
        )
    
    # Get results
    result_repo = Repository[QueryResult](request.state.db)
    results = result_repo.filter({"query_id": query_id})
    
    return APIResponse(
        success=True,
        message="Query results retrieved",
        data=[{
            "id": str(r.id),
            "result_data": r.result_data,
            "format": r.format,
            "size": r.size,
            "created_at": r.created_at
        } for r in results]
    )
