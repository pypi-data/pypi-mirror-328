# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PatientProtocolMatch"]


class PatientProtocolMatch(BaseModel):
    id: int

    match_percentage: float = FieldInfo(alias="matchPercentage")

    title: str
