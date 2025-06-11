from typing import List
from fastapi import UploadFile

class GeminiService:
    """Gemini API と通信する役割を持つサービス。"""

    async def generate_tags(self, file: UploadFile) -> List[str]:
        # 仮実装です。実運用では `file` を Gemini API に送信してください。
        filename = file.filename
        return ["sample", "tags", filename]
