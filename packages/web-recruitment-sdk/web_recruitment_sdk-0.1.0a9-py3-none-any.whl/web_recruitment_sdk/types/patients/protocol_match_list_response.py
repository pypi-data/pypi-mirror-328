# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .patient_protocol_match import PatientProtocolMatch

__all__ = ["ProtocolMatchListResponse"]

ProtocolMatchListResponse: TypeAlias = List[PatientProtocolMatch]
