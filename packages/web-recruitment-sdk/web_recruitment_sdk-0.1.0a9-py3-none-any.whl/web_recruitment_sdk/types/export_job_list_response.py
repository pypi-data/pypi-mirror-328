# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .export_job_status_read import ExportJobStatusRead

__all__ = ["ExportJobListResponse"]

ExportJobListResponse: TypeAlias = List[ExportJobStatusRead]
