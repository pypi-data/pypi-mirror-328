# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import protocol_parsing_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.protocol_parsing_list_response import ProtocolParsingListResponse

__all__ = ["ProtocolParsingsResource", "AsyncProtocolParsingsResource"]


class ProtocolParsingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProtocolParsingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return ProtocolParsingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtocolParsingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return ProtocolParsingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtocolParsingListResponse:
        """
        Get Protocol Parsing Statuses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/protocol-parsing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    protocol_parsing_list_params.ProtocolParsingListParams,
                ),
            ),
            cast_to=ProtocolParsingListResponse,
        )


class AsyncProtocolParsingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProtocolParsingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProtocolParsingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtocolParsingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncProtocolParsingsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtocolParsingListResponse:
        """
        Get Protocol Parsing Statuses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/protocol-parsing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    protocol_parsing_list_params.ProtocolParsingListParams,
                ),
            ),
            cast_to=ProtocolParsingListResponse,
        )


class ProtocolParsingsResourceWithRawResponse:
    def __init__(self, protocol_parsings: ProtocolParsingsResource) -> None:
        self._protocol_parsings = protocol_parsings

        self.list = to_raw_response_wrapper(
            protocol_parsings.list,
        )


class AsyncProtocolParsingsResourceWithRawResponse:
    def __init__(self, protocol_parsings: AsyncProtocolParsingsResource) -> None:
        self._protocol_parsings = protocol_parsings

        self.list = async_to_raw_response_wrapper(
            protocol_parsings.list,
        )


class ProtocolParsingsResourceWithStreamingResponse:
    def __init__(self, protocol_parsings: ProtocolParsingsResource) -> None:
        self._protocol_parsings = protocol_parsings

        self.list = to_streamed_response_wrapper(
            protocol_parsings.list,
        )


class AsyncProtocolParsingsResourceWithStreamingResponse:
    def __init__(self, protocol_parsings: AsyncProtocolParsingsResource) -> None:
        self._protocol_parsings = protocol_parsings

        self.list = async_to_streamed_response_wrapper(
            protocol_parsings.list,
        )
