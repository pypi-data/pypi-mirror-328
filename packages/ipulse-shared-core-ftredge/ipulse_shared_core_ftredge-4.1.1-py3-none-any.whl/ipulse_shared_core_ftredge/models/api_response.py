from typing import Generic, TypeVar, Optional, Any, Dict, List
from pydantic import BaseModel, ConfigDict
import datetime as dt

T = TypeVar('T')

class StandardResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    success: bool
    data: Optional[T] = None
    message: Optional[str] = None
    error: Optional[str] = None

    metadata: Dict[str, Any] = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat()
    }

class PaginatedResponse(StandardResponse, Generic[T]):
    total_count: int
    page: int
    page_size: int
    items: List[T]
