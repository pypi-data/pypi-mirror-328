from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Set, Optional, Dict, List, ClassVar
from pydantic import BaseModel, Field, ConfigDict

# ORIGINAL AUTHOR ="Russlan Ramdowar;russlan@ftredge.com"
CLASS_ORGIN_DATE=datetime(2024, 2, 12, 20, 5)

SCHEMA_VERSION = 2.3
CLASS_REVISION_AUTHOR="Russlan Ramdowar;russlan@ftredge.com"
CLASS_REVISION_DATE=datetime(2024, 2, 13, 20, 15)
LAST_MODIFICATION="Changed default IAM_GROUPS"

DOMAIN="user"
OBJ_REF = "usrsttus"

DEFAULT_IAM_GROUPS={"pulseroot":["full_open_read"]}
DEFAULT_SUBSCRIPTION_PLAN="subscription_free"
DEFAULT_SUBSCRIPTION_STATUS="active"
DEFAULT_SUBSCRIPTION_INSIGHT_CREDITS=10
DEFAULT_EXTRA_INSIGHT_CREDITS=0

############################################ !!!!! ALWAYS UPDATE SCHEMA VERSION , IF SCHEMA IS BEING MODIFIED !!! ############################################
class UserStatus(BaseModel):
    """
    User Status model for tracking user subscription and access rights.
    """
    model_config = ConfigDict(frozen=True, extra="forbid")

    # Class constants
    VERSION: ClassVar[float] = 2.3
    DOMAIN: ClassVar[str] = "user"
    OBJ_REF: ClassVar[str] = "usrsttus"
    
    # Default values as class variables
    DEFAULT_IAM_GROUPS: ClassVar[Dict[str, List[str]]] = {"pulseroot": ["full_open_read"]}
    DEFAULT_SUBSCRIPTION_PLAN: ClassVar[str] = "subscription_free"
    DEFAULT_SUBSCRIPTION_STATUS: ClassVar[str] = "active"
    DEFAULT_SUBSCRIPTION_INSIGHT_CREDITS: ClassVar[int] = 10
    DEFAULT_EXTRA_INSIGHT_CREDITS: ClassVar[int] = 0

    # System-managed fields
    schema_version: float = Field(
        default=2.3,
        description="Version of this Class == version of DB Schema"
    )
    
    # IAM and subscription fields
    iam_groups: Dict[str, List[str]] = Field(
        default_factory=lambda: UserStatus.DEFAULT_IAM_GROUPS,
        description="User's Groups, with a default one for all authenticated Pulse users"
    )
    sbscrptn_plan: str = Field(
        default_factory=lambda: UserStatus.DEFAULT_SUBSCRIPTION_PLAN,
        description="Subscription Plan"
    )
    sbscrptn_status: str = Field(
        default_factory=lambda: UserStatus.DEFAULT_SUBSCRIPTION_STATUS,
        description="Subscription Status"
    )
    
    # Subscription dates
    sbscrptn_start_date: datetime = Field(
        default_factory=datetime.utcnow,
        description="Subscription Start Date"
    )
    sbscrptn_end_date: datetime = Field(
        default_factory=lambda: datetime.utcnow() + relativedelta(years=1),
        description="Subscription End Date"
    )
    
    # Credits management
    sbscrptn_insight_credits: int = Field(
        default_factory=lambda: UserStatus.DEFAULT_SUBSCRIPTION_INSIGHT_CREDITS,
        description="Subscription-based insight credits"
    )
    sbscrptn_ins_crdts_updtd_since_datetime: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp for subscription credits"
    )
    extra_insight_credits: int = Field(
        default_factory=lambda: UserStatus.DEFAULT_EXTRA_INSIGHT_CREDITS,
        description="Additional purchased insight credits (non-expiring)"
    )
    
    # Optional fields
    payment_refs_uids: Optional[Set[str]] = None
    
    # Audit fields
    creat_date: datetime
    creat_by_user: str
    updt_date: datetime
    updt_by_user: str