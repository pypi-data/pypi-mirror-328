from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from typing import Set, Optional, Dict, List, ClassVar
from pydantic import BaseModel, Field, ConfigDict
from ipulse_shared_base_ftredge import Layer, Module, list_as_lower_strings
# ORIGINAL AUTHOR ="Russlan Ramdowar;russlan@ftredge.com"
# CLASS_ORGIN_DATE=datetime(2024, 2, 12, 20, 5)


DEFAULT_SUBSCRIPTION_PLAN="subscription_free"
DEFAULT_SUBSCRIPTION_STATUS="active"

############################################ !!!!! ALWAYS UPDATE SCHEMA VERSION , IF SCHEMA IS BEING MODIFIED !!! ############################################
class Subscription(BaseModel):
    """
    Represents a single subscription cycle.
    """
    plan_name: str = Field(
        default=DEFAULT_SUBSCRIPTION_PLAN,
        description="Subscription Plan Name"
    )

    cycle_start_date: datetime = Field(
        default=datetime.now(timezone.utc),
        description="Subscription Cycle Start Date"
    )
    cycle_end_date: datetime = Field(
        default=lambda: datetime.now(timezone.utc) + relativedelta(years=1),
        description="Subscription Cycle End Date"
    )
    status: str = Field(
        default=DEFAULT_SUBSCRIPTION_STATUS,
        description="Subscription Status (active, inactive, etc.)"
    )