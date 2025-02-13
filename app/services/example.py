from app.db.repositories.example import ExampleRepository


class ExampleService:
    def __init__(self, repository: ExampleRepository):
        self.repository = repository

    async def get_example(self):
        return await self.repository.get_example()
