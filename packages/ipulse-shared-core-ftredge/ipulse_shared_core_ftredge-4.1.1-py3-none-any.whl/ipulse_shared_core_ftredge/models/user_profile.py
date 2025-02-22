from datetime import datetime, date
from typing import Set, Optional, ClassVar
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserProfile(BaseModel):
    """
    User Profile model representing user information and metadata.
    Contains both system-managed and user-editable fields.
    """
    model_config = ConfigDict(frozen=True, extra="forbid")

    # Metadata as class variables
    VERSION: ClassVar[float] = 3.01
    DOMAIN: ClassVar[str] = "user"
    OBJ_REF: ClassVar[str] = "usprfl"
    
    # System-managed fields (read-only)
    schema_version: float = Field(
        default=3.01,
        description="Version of this Class == version of DB Schema",
        frozen=True
    )
    email: EmailStr = Field(
        ...,
        description="Propagated from Firebase Auth",
        frozen=True
    )
    organizations_uids: Set[str] = Field(
        default_factory=set,
        description="Depends on Subscription Plan, Regularly Updated",
        frozen=True
    )
    
    # Timestamps and audit fields (read-only)
    creat_date: datetime = Field(frozen=True)
    creat_by_user: str = Field(frozen=True)
    updt_date: datetime = Field(frozen=True)
    updt_by_user: str = Field(frozen=True)
    
    # System identification (read-only)
    provider_id: str = Field(frozen=True)
    aliases: Optional[Set[str]] = Field(
        default=None,
        frozen=True
    )
    
    # User-editable fields
    username: Optional[str] = Field(
        default=None,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$"
    )
    dob: Optional[date] = Field(
        default=None,
        description="Date of Birth"
    )
    first_name: Optional[str] = Field(
        default=None,
        max_length=100
    )
    last_name: Optional[str] = Field(
        default=None,
        max_length=100
    )
    mobile: Optional[str] = Field(
        default=None,
        pattern=r"^\+?[1-9]\d{1,14}$",  # Added 'r' prefix for raw string
        description="E.164 format phone number"
    )

    # Revision history (as model metadata)
    CLASS_ORIGIN_AUTHOR: ClassVar[str] = "Russlan Ramdowar;russlan@ftredge.com"
    CLASS_ORGIN_DATE: ClassVar[datetime] = datetime(2024, 1, 16, 20, 5)
    CLASS_REVISION_AUTHOR: ClassVar[str] = "Russlan Ramdowar;russlan@ftredge.com"
    CLASS_REVISION_DATE: ClassVar[datetime] = datetime(2024, 2, 13, 20, 15)
    LAST_MODIFICATION: ClassVar[str] = "Updated to Pydantic v2 with improved validation"