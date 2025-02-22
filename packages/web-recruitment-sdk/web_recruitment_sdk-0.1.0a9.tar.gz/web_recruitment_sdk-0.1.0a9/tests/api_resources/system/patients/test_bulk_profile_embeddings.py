# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from web_recruitment_sdk import WebRecruitmentSDK, AsyncWebRecruitmentSDK
from web_recruitment_sdk.types import BulkInsertResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkProfileEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: WebRecruitmentSDK) -> None:
        bulk_profile_embedding = client.system.patients.bulk_profile_embeddings.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        )
        assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WebRecruitmentSDK) -> None:
        response = client.system.patients.bulk_profile_embeddings.with_raw_response.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_profile_embedding = response.parse()
        assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WebRecruitmentSDK) -> None:
        with client.system.patients.bulk_profile_embeddings.with_streaming_response.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_profile_embedding = response.parse()
            assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: WebRecruitmentSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.system.patients.bulk_profile_embeddings.with_raw_response.update(
                tenant_id="",
                body=[
                    {
                        "category": "category",
                        "embedding": [0],
                        "text": "text",
                        "trially_patient_id": "triallyPatientId",
                    }
                ],
            )


class TestAsyncBulkProfileEmbeddings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncWebRecruitmentSDK) -> None:
        bulk_profile_embedding = await async_client.system.patients.bulk_profile_embeddings.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        )
        assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWebRecruitmentSDK) -> None:
        response = await async_client.system.patients.bulk_profile_embeddings.with_raw_response.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_profile_embedding = await response.parse()
        assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWebRecruitmentSDK) -> None:
        async with async_client.system.patients.bulk_profile_embeddings.with_streaming_response.update(
            tenant_id="tenant_id",
            body=[
                {
                    "category": "category",
                    "embedding": [0],
                    "text": "text",
                    "trially_patient_id": "triallyPatientId",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_profile_embedding = await response.parse()
            assert_matches_type(BulkInsertResult, bulk_profile_embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWebRecruitmentSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.system.patients.bulk_profile_embeddings.with_raw_response.update(
                tenant_id="",
                body=[
                    {
                        "category": "category",
                        "embedding": [0],
                        "text": "text",
                        "trially_patient_id": "triallyPatientId",
                    }
                ],
            )
