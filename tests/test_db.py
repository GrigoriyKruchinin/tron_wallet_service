import pytest
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db


@pytest.mark.asyncio
async def test_db_connection(session: AsyncSession = Depends(get_db)):
    result = await session.execute("SELECT 1")
    assert result.scalar() == 1
