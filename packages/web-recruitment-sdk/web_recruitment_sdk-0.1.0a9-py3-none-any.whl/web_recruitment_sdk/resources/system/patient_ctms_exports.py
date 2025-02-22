# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.system import patient_ctms_export_update_params
from ...types.system.patient_ctms_export_update_response import PatientCtmsExportUpdateResponse

__all__ = ["PatientCtmsExportsResource", "AsyncPatientCtmsExportsResource"]


class PatientCtmsExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PatientCtmsExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return PatientCtmsExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PatientCtmsExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return PatientCtmsExportsResourceWithStreamingResponse(self)

    def update(
        self,
        patient_ctms_export_id: int,
        *,
        tenant_id: str,
        status: Literal["IN_PROGRESS", "SUCCESS", "ERROR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatientCtmsExportUpdateResponse:
        """
        Update a patient CTMS export's status

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._patch(
            f"/system/{tenant_id}/patient-ctms-exports/{patient_ctms_export_id}",
            body=maybe_transform({"status": status}, patient_ctms_export_update_params.PatientCtmsExportUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatientCtmsExportUpdateResponse,
        )


class AsyncPatientCtmsExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPatientCtmsExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPatientCtmsExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPatientCtmsExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncPatientCtmsExportsResourceWithStreamingResponse(self)

    async def update(
        self,
        patient_ctms_export_id: int,
        *,
        tenant_id: str,
        status: Literal["IN_PROGRESS", "SUCCESS", "ERROR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatientCtmsExportUpdateResponse:
        """
        Update a patient CTMS export's status

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._patch(
            f"/system/{tenant_id}/patient-ctms-exports/{patient_ctms_export_id}",
            body=await async_maybe_transform(
                {"status": status}, patient_ctms_export_update_params.PatientCtmsExportUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatientCtmsExportUpdateResponse,
        )


class PatientCtmsExportsResourceWithRawResponse:
    def __init__(self, patient_ctms_exports: PatientCtmsExportsResource) -> None:
        self._patient_ctms_exports = patient_ctms_exports

        self.update = to_raw_response_wrapper(
            patient_ctms_exports.update,
        )


class AsyncPatientCtmsExportsResourceWithRawResponse:
    def __init__(self, patient_ctms_exports: AsyncPatientCtmsExportsResource) -> None:
        self._patient_ctms_exports = patient_ctms_exports

        self.update = async_to_raw_response_wrapper(
            patient_ctms_exports.update,
        )


class PatientCtmsExportsResourceWithStreamingResponse:
    def __init__(self, patient_ctms_exports: PatientCtmsExportsResource) -> None:
        self._patient_ctms_exports = patient_ctms_exports

        self.update = to_streamed_response_wrapper(
            patient_ctms_exports.update,
        )


class AsyncPatientCtmsExportsResourceWithStreamingResponse:
    def __init__(self, patient_ctms_exports: AsyncPatientCtmsExportsResource) -> None:
        self._patient_ctms_exports = patient_ctms_exports

        self.update = async_to_streamed_response_wrapper(
            patient_ctms_exports.update,
        )
