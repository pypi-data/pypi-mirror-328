from fastapi import HTTPException
from typing import Optional, Any, Dict

class BaseServiceException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        resource_type: str,
        resource_id: Optional[str] = None,
        additional_info: Optional[Dict[str, Any]] = None
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.additional_info = additional_info or {}
        
        # Build detailed message
        detail_msg = f"{detail}"
        if resource_type:
            detail_msg += f" [Resource Type: {resource_type}]"
        if resource_id:
            detail_msg += f" [ID: {resource_id}]"
        
        super().__init__(status_code=status_code, detail=detail_msg)

class ResourceNotFoundError(BaseServiceException):
    def __init__(
        self,
        resource_type: str,
        resource_id: str,
        additional_info: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            status_code=404,
            detail="Resource not found",
            resource_type=resource_type,
            resource_id=resource_id,
            additional_info=additional_info
        )

class AuthorizationError(BaseServiceException):
    def __init__(
        self,
        resource_type: str,
        action: str,
        resource_id: Optional[str] = None,
        additional_info: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            status_code=403,
            detail=f"Not authorized to {action}",
            resource_type=resource_type,
            resource_id=resource_id,
            additional_info=additional_info
        )

class ValidationError(BaseServiceException):
    def __init__(
        self,
        resource_type: str,
        detail: str,
        resource_id: Optional[str] = None,
        additional_info: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            status_code=422,
            detail=detail,
            resource_type=resource_type,
            resource_id=resource_id,
            additional_info=additional_info
        )
