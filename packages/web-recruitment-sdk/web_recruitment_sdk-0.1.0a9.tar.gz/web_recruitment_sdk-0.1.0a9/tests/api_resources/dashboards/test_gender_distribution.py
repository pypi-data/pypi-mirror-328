# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from web_recruitment_sdk import WebRecruitmentSDK, AsyncWebRecruitmentSDK
from web_recruitment_sdk.types.shared import ChartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenderDistribution:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: WebRecruitmentSDK) -> None:
        gender_distribution = client.dashboards.gender_distribution.list()
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: WebRecruitmentSDK) -> None:
        gender_distribution = client.dashboards.gender_distribution.list(
            limit=1,
            protocol_id=0,
        )
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: WebRecruitmentSDK) -> None:
        response = client.dashboards.gender_distribution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gender_distribution = response.parse()
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: WebRecruitmentSDK) -> None:
        with client.dashboards.gender_distribution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gender_distribution = response.parse()
            assert_matches_type(ChartResponse, gender_distribution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenderDistribution:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        gender_distribution = await async_client.dashboards.gender_distribution.list()
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWebRecruitmentSDK) -> None:
        gender_distribution = await async_client.dashboards.gender_distribution.list(
            limit=1,
            protocol_id=0,
        )
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        response = await async_client.dashboards.gender_distribution.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gender_distribution = await response.parse()
        assert_matches_type(ChartResponse, gender_distribution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWebRecruitmentSDK) -> None:
        async with async_client.dashboards.gender_distribution.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gender_distribution = await response.parse()
            assert_matches_type(ChartResponse, gender_distribution, path=["response"])

        assert cast(Any, response.is_closed) is True
