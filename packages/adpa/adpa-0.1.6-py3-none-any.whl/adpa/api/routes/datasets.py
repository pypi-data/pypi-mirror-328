"""
Dataset routes.
"""
from typing import Optional
from fastapi import APIRouter, Depends, Request, Query, HTTPException
from sqlalchemy import desc

from adpa.api.types import APIResponse
from adpa.api.routes.auth import get_current_user
from adpa.database.models import User, Dataset, DataTable
from adpa.database.repository import Repository

router = APIRouter()

@router.post("/")
async def create_dataset(
    request: Request,
    name: str = Query(..., description="Dataset name"),
    description: Optional[str] = Query(None, description="Dataset description"),
    schema: dict = Query(..., description="Dataset schema"),
    format: str = Query(..., description="Dataset format"),
    is_public: bool = Query(False, description="Whether dataset is public"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Create new dataset."""
    # Create dataset
    dataset = Dataset(
        owner_id=current_user.id,
        name=name,
        description=description,
        schema=schema,
        format=format,
        is_public=is_public
    )
    
    # Save to database
    repo = Repository[Dataset](request.state.db)
    dataset = repo.create(dataset)
    
    return APIResponse(
        success=True,
        message="Dataset created",
        data={
            "id": str(dataset.id),
            "name": dataset.name,
            "description": dataset.description,
            "format": dataset.format,
            "is_public": dataset.is_public
        }
    )

@router.get("/{dataset_id}")
async def get_dataset(
    request: Request,
    dataset_id: str,
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Get dataset by ID."""
    repo = Repository[Dataset](request.state.db)
    dataset = repo.get_by_id(dataset_id)
    
    if not dataset or (not dataset.is_public and dataset.owner_id != current_user.id):
        return APIResponse(
            success=False,
            message="Dataset not found",
            error="Dataset not found or access denied"
        )
    
    return APIResponse(
        success=True,
        message="Dataset retrieved",
        data={
            "id": str(dataset.id),
            "name": dataset.name,
            "description": dataset.description,
            "schema": dataset.schema,
            "format": dataset.format,
            "row_count": dataset.row_count,
            "file_size": dataset.file_size,
            "is_public": dataset.is_public,
            "created_at": dataset.created_at,
            "updated_at": dataset.updated_at
        }
    )

@router.get("/")
async def list_datasets(
    request: Request,
    current_user: User = Depends(get_current_user),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    include_public: bool = Query(True, description="Include public datasets")
) -> APIResponse:
    """List datasets."""
    repo = Repository[Dataset](request.state.db)
    
    if include_public:
        datasets = repo.filter(
            {"$or": [
                {"owner_id": current_user.id},
                {"is_public": True}
            ]},
            order_by=[desc(Dataset.created_at)],
            limit=limit,
            offset=offset
        )
    else:
        datasets = repo.filter(
            {"owner_id": current_user.id},
            order_by=[desc(Dataset.created_at)],
            limit=limit,
            offset=offset
        )
    
    return APIResponse(
        success=True,
        message="Datasets retrieved",
        data=[{
            "id": str(d.id),
            "name": d.name,
            "description": d.description,
            "format": d.format,
            "is_public": d.is_public,
            "created_at": d.created_at
        } for d in datasets]
    )

@router.post("/{dataset_id}/tables")
async def create_table(
    request: Request,
    dataset_id: str,
    name: str = Query(..., description="Table name"),
    description: Optional[str] = Query(None, description="Table description"),
    schema: dict = Query(..., description="Table schema"),
    primary_key: Optional[str] = Query(None, description="Primary key column"),
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """Create new table in dataset."""
    # Check dataset access
    dataset_repo = Repository[Dataset](request.state.db)
    dataset = dataset_repo.get_by_id(dataset_id)
    
    if not dataset or dataset.owner_id != current_user.id:
        return APIResponse(
            success=False,
            message="Dataset not found",
            error="Dataset not found or access denied"
        )
    
    # Create table
    table = DataTable(
        dataset_id=dataset_id,
        name=name,
        description=description,
        schema=schema,
        primary_key=primary_key
    )
    
    # Save to database
    table_repo = Repository[DataTable](request.state.db)
    table = table_repo.create(table)
    
    return APIResponse(
        success=True,
        message="Table created",
        data={
            "id": str(table.id),
            "name": table.name,
            "description": table.description,
            "schema": table.schema,
            "primary_key": table.primary_key
        }
    )

@router.get("/{dataset_id}/tables")
async def list_tables(
    request: Request,
    dataset_id: str,
    current_user: User = Depends(get_current_user)
) -> APIResponse:
    """List tables in dataset."""
    # Check dataset access
    dataset_repo = Repository[Dataset](request.state.db)
    dataset = dataset_repo.get_by_id(dataset_id)
    
    if not dataset or (not dataset.is_public and dataset.owner_id != current_user.id):
        return APIResponse(
            success=False,
            message="Dataset not found",
            error="Dataset not found or access denied"
        )
    
    # Get tables
    table_repo = Repository[DataTable](request.state.db)
    tables = table_repo.filter({"dataset_id": dataset_id})
    
    return APIResponse(
        success=True,
        message="Tables retrieved",
        data=[{
            "id": str(t.id),
            "name": t.name,
            "description": t.description,
            "schema": t.schema,
            "row_count": t.row_count,
            "primary_key": t.primary_key,
            "created_at": t.created_at
        } for t in tables]
    )
