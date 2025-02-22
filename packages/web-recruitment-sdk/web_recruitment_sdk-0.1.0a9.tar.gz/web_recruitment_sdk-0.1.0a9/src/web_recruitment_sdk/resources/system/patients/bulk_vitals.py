# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.system.patients import bulk_vital_update_params
from ....types.bulk_insert_result import BulkInsertResult

__all__ = ["BulkVitalsResource", "AsyncBulkVitalsResource"]


class BulkVitalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkVitalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return BulkVitalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkVitalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return BulkVitalsResourceWithStreamingResponse(self)

    def update(
        self,
        tenant_id: str,
        *,
        body: Iterable[bulk_vital_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkInsertResult:
        """
        Bulk update patient vitals

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._put(
            f"/system/{tenant_id}/patients/bulk/patient_vitals",
            body=maybe_transform(body, Iterable[bulk_vital_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkInsertResult,
        )


class AsyncBulkVitalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkVitalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkVitalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkVitalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncBulkVitalsResourceWithStreamingResponse(self)

    async def update(
        self,
        tenant_id: str,
        *,
        body: Iterable[bulk_vital_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkInsertResult:
        """
        Bulk update patient vitals

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._put(
            f"/system/{tenant_id}/patients/bulk/patient_vitals",
            body=await async_maybe_transform(body, Iterable[bulk_vital_update_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkInsertResult,
        )


class BulkVitalsResourceWithRawResponse:
    def __init__(self, bulk_vitals: BulkVitalsResource) -> None:
        self._bulk_vitals = bulk_vitals

        self.update = to_raw_response_wrapper(
            bulk_vitals.update,
        )


class AsyncBulkVitalsResourceWithRawResponse:
    def __init__(self, bulk_vitals: AsyncBulkVitalsResource) -> None:
        self._bulk_vitals = bulk_vitals

        self.update = async_to_raw_response_wrapper(
            bulk_vitals.update,
        )


class BulkVitalsResourceWithStreamingResponse:
    def __init__(self, bulk_vitals: BulkVitalsResource) -> None:
        self._bulk_vitals = bulk_vitals

        self.update = to_streamed_response_wrapper(
            bulk_vitals.update,
        )


class AsyncBulkVitalsResourceWithStreamingResponse:
    def __init__(self, bulk_vitals: AsyncBulkVitalsResource) -> None:
        self._bulk_vitals = bulk_vitals

        self.update = async_to_streamed_response_wrapper(
            bulk_vitals.update,
        )
