# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .role_read import RoleRead
from ..shared.site_read import SiteRead

__all__ = ["Authorization"]


class Authorization(BaseModel):
    permissions: Optional[List[str]] = None

    role: Optional[RoleRead] = None

    secondary_roles: Optional[List[RoleRead]] = FieldInfo(alias="secondaryRoles", default=None)

    sites: Optional[List[SiteRead]] = None
