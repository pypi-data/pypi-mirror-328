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
from ...types.dashboards import ethnic_distribution_list_params
from ...types.shared.chart_response import ChartResponse

__all__ = ["EthnicDistributionResource", "AsyncEthnicDistributionResource"]


class EthnicDistributionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EthnicDistributionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return EthnicDistributionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EthnicDistributionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return EthnicDistributionResourceWithStreamingResponse(self)

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
        Get ethnic distribution across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dashboards/ethnic-distribution",
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
                    ethnic_distribution_list_params.EthnicDistributionListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class AsyncEthnicDistributionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEthnicDistributionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEthnicDistributionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEthnicDistributionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncEthnicDistributionResourceWithStreamingResponse(self)

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
        Get ethnic distribution across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dashboards/ethnic-distribution",
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
                    ethnic_distribution_list_params.EthnicDistributionListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class EthnicDistributionResourceWithRawResponse:
    def __init__(self, ethnic_distribution: EthnicDistributionResource) -> None:
        self._ethnic_distribution = ethnic_distribution

        self.list = to_raw_response_wrapper(
            ethnic_distribution.list,
        )


class AsyncEthnicDistributionResourceWithRawResponse:
    def __init__(self, ethnic_distribution: AsyncEthnicDistributionResource) -> None:
        self._ethnic_distribution = ethnic_distribution

        self.list = async_to_raw_response_wrapper(
            ethnic_distribution.list,
        )


class EthnicDistributionResourceWithStreamingResponse:
    def __init__(self, ethnic_distribution: EthnicDistributionResource) -> None:
        self._ethnic_distribution = ethnic_distribution

        self.list = to_streamed_response_wrapper(
            ethnic_distribution.list,
        )


class AsyncEthnicDistributionResourceWithStreamingResponse:
    def __init__(self, ethnic_distribution: AsyncEthnicDistributionResource) -> None:
        self._ethnic_distribution = ethnic_distribution

        self.list = async_to_streamed_response_wrapper(
            ethnic_distribution.list,
        )
