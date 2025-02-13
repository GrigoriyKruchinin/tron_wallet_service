from sqlalchemy.ext.asyncio import AsyncSession


class ExampleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_example(self):
        pass
