# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...shared.patient_profile_embedding_read import PatientProfileEmbeddingRead

__all__ = ["ClosestPatientProfileDocumentCreateResponse"]

ClosestPatientProfileDocumentCreateResponse: TypeAlias = List[PatientProfileEmbeddingRead]
