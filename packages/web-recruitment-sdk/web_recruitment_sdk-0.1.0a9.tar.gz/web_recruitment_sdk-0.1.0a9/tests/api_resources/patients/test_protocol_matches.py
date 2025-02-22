# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from web_recruitment_sdk import WebRecruitmentSDK, AsyncWebRecruitmentSDK
from web_recruitment_sdk.types.patients import ProtocolMatchListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProtocolMatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: WebRecruitmentSDK) -> None:
        protocol_match = client.patients.protocol_matches.list(
            0,
        )
        assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WebRecruitmentSDK) -> None:
        response = client.patients.protocol_matches.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        protocol_match = response.parse()
        assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WebRecruitmentSDK) -> None:
        with client.patients.protocol_matches.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            protocol_match = response.parse()
            assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProtocolMatches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        protocol_match = await async_client.patients.protocol_matches.list(
            0,
        )
        assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        response = await async_client.patients.protocol_matches.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        protocol_match = await response.parse()
        assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        async with async_client.patients.protocol_matches.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            protocol_match = await response.parse()
            assert_matches_type(ProtocolMatchListResponse, protocol_match, path=["response"])

        assert cast(Any, response.is_closed) is True
