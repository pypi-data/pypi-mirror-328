from typing import Optional

from pydantic import BaseModel

from savant_models.utils.base import PyObjectId


class QACheckResult(BaseModel):
    qa_check: str
    passed: bool
    object_id: Optional[PyObjectId]
    message: str
