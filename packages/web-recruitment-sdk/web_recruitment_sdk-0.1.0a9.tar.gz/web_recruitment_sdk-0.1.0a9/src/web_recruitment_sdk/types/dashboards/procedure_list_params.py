# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProcedureListParams"]


class ProcedureListParams(TypedDict, total=False):
    limit: int

    protocol_id: Optional[int]
