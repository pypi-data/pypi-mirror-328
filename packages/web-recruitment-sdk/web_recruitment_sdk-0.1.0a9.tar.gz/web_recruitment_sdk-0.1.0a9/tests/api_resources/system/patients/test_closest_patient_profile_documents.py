# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from web_recruitment_sdk import WebRecruitmentSDK, AsyncWebRecruitmentSDK
from web_recruitment_sdk.types.system.patients import (
    ClosestPatientProfileDocumentCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClosestPatientProfileDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WebRecruitmentSDK) -> None:
        closest_patient_profile_document = client.system.patients.closest_patient_profile_documents.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        )
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    def test_method_create_with_all_params(self, client: WebRecruitmentSDK) -> None:
        closest_patient_profile_document = client.system.patients.closest_patient_profile_documents.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
            n_results=0,
        )
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: WebRecruitmentSDK) -> None:
        response = client.system.patients.closest_patient_profile_documents.with_raw_response.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closest_patient_profile_document = response.parse()
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: WebRecruitmentSDK) -> None:
        with client.system.patients.closest_patient_profile_documents.with_streaming_response.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closest_patient_profile_document = response.parse()
            assert_matches_type(
                ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: WebRecruitmentSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.system.patients.closest_patient_profile_documents.with_raw_response.create(
                tenant_id="",
                category="category",
                query=[0],
                trially_patient_id="triallyPatientId",
            )


class TestAsyncClosestPatientProfileDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWebRecruitmentSDK) -> None:
        closest_patient_profile_document = await async_client.system.patients.closest_patient_profile_documents.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        )
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWebRecruitmentSDK) -> None:
        closest_patient_profile_document = await async_client.system.patients.closest_patient_profile_documents.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
            n_results=0,
        )
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWebRecruitmentSDK) -> None:
        response = await async_client.system.patients.closest_patient_profile_documents.with_raw_response.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        closest_patient_profile_document = await response.parse()
        assert_matches_type(
            ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWebRecruitmentSDK) -> None:
        async with async_client.system.patients.closest_patient_profile_documents.with_streaming_response.create(
            tenant_id="tenant_id",
            category="category",
            query=[0],
            trially_patient_id="triallyPatientId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            closest_patient_profile_document = await response.parse()
            assert_matches_type(
                ClosestPatientProfileDocumentCreateResponse, closest_patient_profile_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWebRecruitmentSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.system.patients.closest_patient_profile_documents.with_raw_response.create(
                tenant_id="",
                category="category",
                query=[0],
                trially_patient_id="triallyPatientId",
            )
