from typing import List
from fastapi import UploadFile
import os
import asyncio
import google.generativeai as genai

if not hasattr(genai, "GenerativeModel"):
    raise ImportError(
        "google-generativeai package is outdated."
        " Please install version 0.3.0 or newer."
    )


class GeminiService:
    """Gemini API と通信する役割を持つサービス。"""

    def __init__(self) -> None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")
        genai.configure(api_key=api_key)

    async def generate_tags(self, file: UploadFile) -> List[str]:
        data = await file.read()
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            "あなたは画像の内容を10個の短いタグで説明するアシスタントです。"
            "タグは日本語で、カンマ区切りのリストで10個のみ返してください。"
        )
        response = await asyncio.to_thread(
            model.generate_content,
            [prompt, {"mime_type": file.content_type, "data": data}],
            stream=False,
        )
        text = response.text or ""
        tags = [t.strip() for t in text.split(",") if t.strip()]
        return tags[:10]
