from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.example import ExampleService
from app.db.repositories.example import ExampleRepository
from app.db.session import get_db

router = APIRouter()


@router.get("/example")
async def get_example(session: AsyncSession = Depends(get_db)):
    repository = ExampleRepository(session)
    service = ExampleService(repository)
    return await service.get_example()
