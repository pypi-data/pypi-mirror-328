# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.patients.protocol_match_list_response import ProtocolMatchListResponse

__all__ = ["ProtocolMatchesResource", "AsyncProtocolMatchesResource"]


class ProtocolMatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProtocolMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return ProtocolMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtocolMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return ProtocolMatchesResourceWithStreamingResponse(self)

    def list(
        self,
        patient_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtocolMatchListResponse:
        """
        Get all protocols a patient has a match with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/patients/{patient_id}/protocol-matches",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProtocolMatchListResponse,
        )


class AsyncProtocolMatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProtocolMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProtocolMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtocolMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncProtocolMatchesResourceWithStreamingResponse(self)

    async def list(
        self,
        patient_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtocolMatchListResponse:
        """
        Get all protocols a patient has a match with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/patients/{patient_id}/protocol-matches",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProtocolMatchListResponse,
        )


class ProtocolMatchesResourceWithRawResponse:
    def __init__(self, protocol_matches: ProtocolMatchesResource) -> None:
        self._protocol_matches = protocol_matches

        self.list = to_raw_response_wrapper(
            protocol_matches.list,
        )


class AsyncProtocolMatchesResourceWithRawResponse:
    def __init__(self, protocol_matches: AsyncProtocolMatchesResource) -> None:
        self._protocol_matches = protocol_matches

        self.list = async_to_raw_response_wrapper(
            protocol_matches.list,
        )


class ProtocolMatchesResourceWithStreamingResponse:
    def __init__(self, protocol_matches: ProtocolMatchesResource) -> None:
        self._protocol_matches = protocol_matches

        self.list = to_streamed_response_wrapper(
            protocol_matches.list,
        )


class AsyncProtocolMatchesResourceWithStreamingResponse:
    def __init__(self, protocol_matches: AsyncProtocolMatchesResource) -> None:
        self._protocol_matches = protocol_matches

        self.list = async_to_streamed_response_wrapper(
            protocol_matches.list,
        )
