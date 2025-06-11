from fastapi import APIRouter, UploadFile, File
from ..usecases.generate_tags import GenerateTags
from ..infrastructure.gemini_service import GeminiService
from ..domain.models import TagResult

router = APIRouter()
service = GeminiService()
usecase = GenerateTags(service)

@router.post("/generate_tags", response_model=TagResult)
async def generate_tags_endpoint(image: UploadFile = File(...)):
    tags = await usecase.execute(image)
    return TagResult(tags=tags)
