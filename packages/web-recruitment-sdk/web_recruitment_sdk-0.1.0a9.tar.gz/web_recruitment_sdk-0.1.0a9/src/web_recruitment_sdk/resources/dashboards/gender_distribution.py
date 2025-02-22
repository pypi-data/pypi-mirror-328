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
from ...types.dashboards import gender_distribution_list_params
from ...types.shared.chart_response import ChartResponse

__all__ = ["GenderDistributionResource", "AsyncGenderDistributionResource"]


class GenderDistributionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenderDistributionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return GenderDistributionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenderDistributionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return GenderDistributionResourceWithStreamingResponse(self)

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
        Get gender distribution across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dashboards/gender-distribution",
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
                    gender_distribution_list_params.GenderDistributionListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class AsyncGenderDistributionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenderDistributionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGenderDistributionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenderDistributionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncGenderDistributionResourceWithStreamingResponse(self)

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
        Get gender distribution across sites

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dashboards/gender-distribution",
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
                    gender_distribution_list_params.GenderDistributionListParams,
                ),
            ),
            cast_to=ChartResponse,
        )


class GenderDistributionResourceWithRawResponse:
    def __init__(self, gender_distribution: GenderDistributionResource) -> None:
        self._gender_distribution = gender_distribution

        self.list = to_raw_response_wrapper(
            gender_distribution.list,
        )


class AsyncGenderDistributionResourceWithRawResponse:
    def __init__(self, gender_distribution: AsyncGenderDistributionResource) -> None:
        self._gender_distribution = gender_distribution

        self.list = async_to_raw_response_wrapper(
            gender_distribution.list,
        )


class GenderDistributionResourceWithStreamingResponse:
    def __init__(self, gender_distribution: GenderDistributionResource) -> None:
        self._gender_distribution = gender_distribution

        self.list = to_streamed_response_wrapper(
            gender_distribution.list,
        )


class AsyncGenderDistributionResourceWithStreamingResponse:
    def __init__(self, gender_distribution: AsyncGenderDistributionResource) -> None:
        self._gender_distribution = gender_distribution

        self.list = async_to_streamed_response_wrapper(
            gender_distribution.list,
        )
