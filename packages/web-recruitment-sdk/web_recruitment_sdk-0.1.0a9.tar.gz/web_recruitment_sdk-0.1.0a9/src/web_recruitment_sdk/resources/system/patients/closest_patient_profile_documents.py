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
from ....types.system.patients import closest_patient_profile_document_create_params
from ....types.system.patients.closest_patient_profile_document_create_response import (
    ClosestPatientProfileDocumentCreateResponse,
)

__all__ = ["ClosestPatientProfileDocumentsResource", "AsyncClosestPatientProfileDocumentsResource"]


class ClosestPatientProfileDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClosestPatientProfileDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return ClosestPatientProfileDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClosestPatientProfileDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return ClosestPatientProfileDocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        tenant_id: str,
        *,
        category: str,
        query: Iterable[float],
        trially_patient_id: str,
        n_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClosestPatientProfileDocumentCreateResponse:
        """
        Get Patient Profile Embeddings

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._post(
            f"/system/{tenant_id}/patients/closest_patient_profile_documents",
            body=maybe_transform(
                {
                    "category": category,
                    "query": query,
                    "trially_patient_id": trially_patient_id,
                    "n_results": n_results,
                },
                closest_patient_profile_document_create_params.ClosestPatientProfileDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClosestPatientProfileDocumentCreateResponse,
        )


class AsyncClosestPatientProfileDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClosestPatientProfileDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClosestPatientProfileDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClosestPatientProfileDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncClosestPatientProfileDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        tenant_id: str,
        *,
        category: str,
        query: Iterable[float],
        trially_patient_id: str,
        n_results: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClosestPatientProfileDocumentCreateResponse:
        """
        Get Patient Profile Embeddings

        Args:
          tenant_id: The tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._post(
            f"/system/{tenant_id}/patients/closest_patient_profile_documents",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "query": query,
                    "trially_patient_id": trially_patient_id,
                    "n_results": n_results,
                },
                closest_patient_profile_document_create_params.ClosestPatientProfileDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClosestPatientProfileDocumentCreateResponse,
        )


class ClosestPatientProfileDocumentsResourceWithRawResponse:
    def __init__(self, closest_patient_profile_documents: ClosestPatientProfileDocumentsResource) -> None:
        self._closest_patient_profile_documents = closest_patient_profile_documents

        self.create = to_raw_response_wrapper(
            closest_patient_profile_documents.create,
        )


class AsyncClosestPatientProfileDocumentsResourceWithRawResponse:
    def __init__(self, closest_patient_profile_documents: AsyncClosestPatientProfileDocumentsResource) -> None:
        self._closest_patient_profile_documents = closest_patient_profile_documents

        self.create = async_to_raw_response_wrapper(
            closest_patient_profile_documents.create,
        )


class ClosestPatientProfileDocumentsResourceWithStreamingResponse:
    def __init__(self, closest_patient_profile_documents: ClosestPatientProfileDocumentsResource) -> None:
        self._closest_patient_profile_documents = closest_patient_profile_documents

        self.create = to_streamed_response_wrapper(
            closest_patient_profile_documents.create,
        )


class AsyncClosestPatientProfileDocumentsResourceWithStreamingResponse:
    def __init__(self, closest_patient_profile_documents: AsyncClosestPatientProfileDocumentsResource) -> None:
        self._closest_patient_profile_documents = closest_patient_profile_documents

        self.create = async_to_streamed_response_wrapper(
            closest_patient_profile_documents.create,
        )
