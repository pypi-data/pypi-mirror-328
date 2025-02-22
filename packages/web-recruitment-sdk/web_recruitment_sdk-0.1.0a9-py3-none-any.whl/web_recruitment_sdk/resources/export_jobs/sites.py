# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.export_jobs import site_create_params
from ...types.export_job_read import ExportJobRead

__all__ = ["SitesResource", "AsyncSitesResource"]


class SitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return SitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return SitesResourceWithStreamingResponse(self)

    def create(
        self,
        site_id: int,
        *,
        client_id: str,
        ctms: str,
        ctms_site_id: str,
        patients: Iterable[site_create_params.Patient],
        referral_source_category_key: int,
        referral_source_key: int,
        study_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportJobRead:
        """
        Start an export job to export given patients to a CTMS

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/export-job/sites/{site_id}",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "ctms": ctms,
                    "ctms_site_id": ctms_site_id,
                    "patients": patients,
                    "referral_source_category_key": referral_source_category_key,
                    "referral_source_key": referral_source_key,
                    "study_id": study_id,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportJobRead,
        )


class AsyncSitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncSitesResourceWithStreamingResponse(self)

    async def create(
        self,
        site_id: int,
        *,
        client_id: str,
        ctms: str,
        ctms_site_id: str,
        patients: Iterable[site_create_params.Patient],
        referral_source_category_key: int,
        referral_source_key: int,
        study_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportJobRead:
        """
        Start an export job to export given patients to a CTMS

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/export-job/sites/{site_id}",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "ctms": ctms,
                    "ctms_site_id": ctms_site_id,
                    "patients": patients,
                    "referral_source_category_key": referral_source_category_key,
                    "referral_source_key": referral_source_key,
                    "study_id": study_id,
                },
                site_create_params.SiteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportJobRead,
        )


class SitesResourceWithRawResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

        self.create = to_raw_response_wrapper(
            sites.create,
        )


class AsyncSitesResourceWithRawResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

        self.create = async_to_raw_response_wrapper(
            sites.create,
        )


class SitesResourceWithStreamingResponse:
    def __init__(self, sites: SitesResource) -> None:
        self._sites = sites

        self.create = to_streamed_response_wrapper(
            sites.create,
        )


class AsyncSitesResourceWithStreamingResponse:
    def __init__(self, sites: AsyncSitesResource) -> None:
        self._sites = sites

        self.create = async_to_streamed_response_wrapper(
            sites.create,
        )
