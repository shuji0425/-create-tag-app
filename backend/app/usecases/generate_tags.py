from typing import List, Protocol
from fastapi import UploadFile

class TagGenerator(Protocol):
    async def generate_tags(self, file: UploadFile) -> List[str]:
        ...

class GenerateTags:
    def __init__(self, generator: TagGenerator):
        self.generator = generator

    async def execute(self, file: UploadFile) -> List[str]:
        return await self.generator.generate_tags(file)
