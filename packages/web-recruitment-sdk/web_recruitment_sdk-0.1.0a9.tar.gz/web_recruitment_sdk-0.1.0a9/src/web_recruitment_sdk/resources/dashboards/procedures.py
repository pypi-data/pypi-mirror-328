# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.dashboards import procedure_list_params
from ...types.shared.chart_response import ChartResponse

__all__ = ["ProceduresResource", "AsyncProceduresResource"]


class ProceduresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProceduresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return ProceduresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProceduresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return ProceduresResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        protocol_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChartResponse:
        """
        Get top procedures across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dashboards/procedures",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "protocol_id": protocol_id,
                    },
                    procedure_list_params.ProcedureListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class AsyncProceduresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProceduresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProceduresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProceduresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncProceduresResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        protocol_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChartResponse:
        """
        Get top procedures across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dashboards/procedures",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "protocol_id": protocol_id,
                    },
                    procedure_list_params.ProcedureListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class ProceduresResourceWithRawResponse:
    def __init__(self, procedures: ProceduresResource) -> None:
        self._procedures = procedures

        self.list = to_raw_response_wrapper(
            procedures.list,
        )


class AsyncProceduresResourceWithRawResponse:
    def __init__(self, procedures: AsyncProceduresResource) -> None:
        self._procedures = procedures

        self.list = async_to_raw_response_wrapper(
            procedures.list,
        )


class ProceduresResourceWithStreamingResponse:
    def __init__(self, procedures: ProceduresResource) -> None:
        self._procedures = procedures

        self.list = to_streamed_response_wrapper(
            procedures.list,
        )


class AsyncProceduresResourceWithStreamingResponse:
    def __init__(self, procedures: AsyncProceduresResource) -> None:
        self._procedures = procedures

        self.list = async_to_streamed_response_wrapper(
            procedures.list,
        )
