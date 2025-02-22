# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .sites import (
    SitesResource,
    AsyncSitesResource,
    SitesResourceWithRawResponse,
    AsyncSitesResourceWithRawResponse,
    SitesResourceWithStreamingResponse,
    AsyncSitesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.export_job_list_response import ExportJobListResponse

__all__ = ["ExportJobsResource", "AsyncExportJobsResource"]


class ExportJobsResource(SyncAPIResource):
    @cached_property
    def sites(self) -> SitesResource:
        return SitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExportJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return ExportJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return ExportJobsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportJobListResponse:
        """Get all export jobs with their status for the current user."""
        return self._get(
            "/export-jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportJobListResponse,
        )


class AsyncExportJobsResource(AsyncAPIResource):
    @cached_property
    def sites(self) -> AsyncSitesResource:
        return AsyncSitesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExportJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExportJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncExportJobsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportJobListResponse:
        """Get all export jobs with their status for the current user."""
        return await self._get(
            "/export-jobs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportJobListResponse,
        )


class ExportJobsResourceWithRawResponse:
    def __init__(self, export_jobs: ExportJobsResource) -> None:
        self._export_jobs = export_jobs

        self.list = to_raw_response_wrapper(
            export_jobs.list,
        )

    @cached_property
    def sites(self) -> SitesResourceWithRawResponse:
        return SitesResourceWithRawResponse(self._export_jobs.sites)


class AsyncExportJobsResourceWithRawResponse:
    def __init__(self, export_jobs: AsyncExportJobsResource) -> None:
        self._export_jobs = export_jobs

        self.list = async_to_raw_response_wrapper(
            export_jobs.list,
        )

    @cached_property
    def sites(self) -> AsyncSitesResourceWithRawResponse:
        return AsyncSitesResourceWithRawResponse(self._export_jobs.sites)


class ExportJobsResourceWithStreamingResponse:
    def __init__(self, export_jobs: ExportJobsResource) -> None:
        self._export_jobs = export_jobs

        self.list = to_streamed_response_wrapper(
            export_jobs.list,
        )

    @cached_property
    def sites(self) -> SitesResourceWithStreamingResponse:
        return SitesResourceWithStreamingResponse(self._export_jobs.sites)


class AsyncExportJobsResourceWithStreamingResponse:
    def __init__(self, export_jobs: AsyncExportJobsResource) -> None:
        self._export_jobs = export_jobs

        self.list = async_to_streamed_response_wrapper(
            export_jobs.list,
        )

    @cached_property
    def sites(self) -> AsyncSitesResourceWithStreamingResponse:
        return AsyncSitesResourceWithStreamingResponse(self._export_jobs.sites)
