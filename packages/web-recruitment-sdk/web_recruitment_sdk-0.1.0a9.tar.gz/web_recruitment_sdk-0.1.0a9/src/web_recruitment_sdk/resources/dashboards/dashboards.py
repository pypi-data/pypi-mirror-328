# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .conditions import (
    ConditionsResource,
    AsyncConditionsResource,
    ConditionsResourceWithRawResponse,
    AsyncConditionsResourceWithRawResponse,
    ConditionsResourceWithStreamingResponse,
    AsyncConditionsResourceWithStreamingResponse,
)
from .procedures import (
    ProceduresResource,
    AsyncProceduresResource,
    ProceduresResourceWithRawResponse,
    AsyncProceduresResourceWithRawResponse,
    ProceduresResourceWithStreamingResponse,
    AsyncProceduresResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .medications import (
    MedicationsResource,
    AsyncMedicationsResource,
    MedicationsResourceWithRawResponse,
    AsyncMedicationsResourceWithRawResponse,
    MedicationsResourceWithStreamingResponse,
    AsyncMedicationsResourceWithStreamingResponse,
)
from .age_distribution import (
    AgeDistributionResource,
    AsyncAgeDistributionResource,
    AgeDistributionResourceWithRawResponse,
    AsyncAgeDistributionResourceWithRawResponse,
    AgeDistributionResourceWithStreamingResponse,
    AsyncAgeDistributionResourceWithStreamingResponse,
)
from .ethnic_distribution import (
    EthnicDistributionResource,
    AsyncEthnicDistributionResource,
    EthnicDistributionResourceWithRawResponse,
    AsyncEthnicDistributionResourceWithRawResponse,
    EthnicDistributionResourceWithStreamingResponse,
    AsyncEthnicDistributionResourceWithStreamingResponse,
)
from .gender_distribution import (
    GenderDistributionResource,
    AsyncGenderDistributionResource,
    GenderDistributionResourceWithRawResponse,
    AsyncGenderDistributionResourceWithRawResponse,
    GenderDistributionResourceWithStreamingResponse,
    AsyncGenderDistributionResourceWithStreamingResponse,
)

__all__ = ["DashboardsResource", "AsyncDashboardsResource"]


class DashboardsResource(SyncAPIResource):
    @cached_property
    def medications(self) -> MedicationsResource:
        return MedicationsResource(self._client)

    @cached_property
    def conditions(self) -> ConditionsResource:
        return ConditionsResource(self._client)

    @cached_property
    def procedures(self) -> ProceduresResource:
        return ProceduresResource(self._client)

    @cached_property
    def age_distribution(self) -> AgeDistributionResource:
        return AgeDistributionResource(self._client)

    @cached_property
    def gender_distribution(self) -> GenderDistributionResource:
        return GenderDistributionResource(self._client)

    @cached_property
    def ethnic_distribution(self) -> EthnicDistributionResource:
        return EthnicDistributionResource(self._client)

    @cached_property
    def with_raw_response(self) -> DashboardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return DashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DashboardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return DashboardsResourceWithStreamingResponse(self)


class AsyncDashboardsResource(AsyncAPIResource):
    @cached_property
    def medications(self) -> AsyncMedicationsResource:
        return AsyncMedicationsResource(self._client)

    @cached_property
    def conditions(self) -> AsyncConditionsResource:
        return AsyncConditionsResource(self._client)

    @cached_property
    def procedures(self) -> AsyncProceduresResource:
        return AsyncProceduresResource(self._client)

    @cached_property
    def age_distribution(self) -> AsyncAgeDistributionResource:
        return AsyncAgeDistributionResource(self._client)

    @cached_property
    def gender_distribution(self) -> AsyncGenderDistributionResource:
        return AsyncGenderDistributionResource(self._client)

    @cached_property
    def ethnic_distribution(self) -> AsyncEthnicDistributionResource:
        return AsyncEthnicDistributionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDashboardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDashboardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TriallyAI/web-recruitment-sdk#with_streaming_response
        """
        return AsyncDashboardsResourceWithStreamingResponse(self)


class DashboardsResourceWithRawResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def medications(self) -> MedicationsResourceWithRawResponse:
        return MedicationsResourceWithRawResponse(self._dashboards.medications)

    @cached_property
    def conditions(self) -> ConditionsResourceWithRawResponse:
        return ConditionsResourceWithRawResponse(self._dashboards.conditions)

    @cached_property
    def procedures(self) -> ProceduresResourceWithRawResponse:
        return ProceduresResourceWithRawResponse(self._dashboards.procedures)

    @cached_property
    def age_distribution(self) -> AgeDistributionResourceWithRawResponse:
        return AgeDistributionResourceWithRawResponse(self._dashboards.age_distribution)

    @cached_property
    def gender_distribution(self) -> GenderDistributionResourceWithRawResponse:
        return GenderDistributionResourceWithRawResponse(self._dashboards.gender_distribution)

    @cached_property
    def ethnic_distribution(self) -> EthnicDistributionResourceWithRawResponse:
        return EthnicDistributionResourceWithRawResponse(self._dashboards.ethnic_distribution)


class AsyncDashboardsResourceWithRawResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def medications(self) -> AsyncMedicationsResourceWithRawResponse:
        return AsyncMedicationsResourceWithRawResponse(self._dashboards.medications)

    @cached_property
    def conditions(self) -> AsyncConditionsResourceWithRawResponse:
        return AsyncConditionsResourceWithRawResponse(self._dashboards.conditions)

    @cached_property
    def procedures(self) -> AsyncProceduresResourceWithRawResponse:
        return AsyncProceduresResourceWithRawResponse(self._dashboards.procedures)

    @cached_property
    def age_distribution(self) -> AsyncAgeDistributionResourceWithRawResponse:
        return AsyncAgeDistributionResourceWithRawResponse(self._dashboards.age_distribution)

    @cached_property
    def gender_distribution(self) -> AsyncGenderDistributionResourceWithRawResponse:
        return AsyncGenderDistributionResourceWithRawResponse(self._dashboards.gender_distribution)

    @cached_property
    def ethnic_distribution(self) -> AsyncEthnicDistributionResourceWithRawResponse:
        return AsyncEthnicDistributionResourceWithRawResponse(self._dashboards.ethnic_distribution)


class DashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def medications(self) -> MedicationsResourceWithStreamingResponse:
        return MedicationsResourceWithStreamingResponse(self._dashboards.medications)

    @cached_property
    def conditions(self) -> ConditionsResourceWithStreamingResponse:
        return ConditionsResourceWithStreamingResponse(self._dashboards.conditions)

    @cached_property
    def procedures(self) -> ProceduresResourceWithStreamingResponse:
        return ProceduresResourceWithStreamingResponse(self._dashboards.procedures)

    @cached_property
    def age_distribution(self) -> AgeDistributionResourceWithStreamingResponse:
        return AgeDistributionResourceWithStreamingResponse(self._dashboards.age_distribution)

    @cached_property
    def gender_distribution(self) -> GenderDistributionResourceWithStreamingResponse:
        return GenderDistributionResourceWithStreamingResponse(self._dashboards.gender_distribution)

    @cached_property
    def ethnic_distribution(self) -> EthnicDistributionResourceWithStreamingResponse:
        return EthnicDistributionResourceWithStreamingResponse(self._dashboards.ethnic_distribution)


class AsyncDashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

    @cached_property
    def medications(self) -> AsyncMedicationsResourceWithStreamingResponse:
        return AsyncMedicationsResourceWithStreamingResponse(self._dashboards.medications)

    @cached_property
    def conditions(self) -> AsyncConditionsResourceWithStreamingResponse:
        return AsyncConditionsResourceWithStreamingResponse(self._dashboards.conditions)

    @cached_property
    def procedures(self) -> AsyncProceduresResourceWithStreamingResponse:
        return AsyncProceduresResourceWithStreamingResponse(self._dashboards.procedures)

    @cached_property
    def age_distribution(self) -> AsyncAgeDistributionResourceWithStreamingResponse:
        return AsyncAgeDistributionResourceWithStreamingResponse(self._dashboards.age_distribution)

    @cached_property
    def gender_distribution(self) -> AsyncGenderDistributionResourceWithStreamingResponse:
        return AsyncGenderDistributionResourceWithStreamingResponse(self._dashboards.gender_distribution)

    @cached_property
    def ethnic_distribution(self) -> AsyncEthnicDistributionResourceWithStreamingResponse:
        return AsyncEthnicDistributionResourceWithStreamingResponse(self._dashboards.ethnic_distribution)
