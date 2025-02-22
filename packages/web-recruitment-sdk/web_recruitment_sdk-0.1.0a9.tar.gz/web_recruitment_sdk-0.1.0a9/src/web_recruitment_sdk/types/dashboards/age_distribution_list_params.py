# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgeDistributionListParams"]


class AgeDistributionListParams(TypedDict, total=False):
    limit: int

    protocol_id: Optional[int]

    step: int
