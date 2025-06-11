from typing import List
from fastapi import UploadFile

class GeminiService:
    """Service responsible for communicating with the Gemini API."""

    async def generate_tags(self, file: UploadFile) -> List[str]:
        # Placeholder implementation. In production, send `file` to Gemini API.
        filename = file.filename
        return ["sample", "tags", filename]
