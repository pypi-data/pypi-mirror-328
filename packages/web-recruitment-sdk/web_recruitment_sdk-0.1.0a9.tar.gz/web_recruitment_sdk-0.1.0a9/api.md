# Shared Types

```python
from web_recruitment_sdk.types import (
    AppointmentRead,
    ChartResponse,
    CriteriaRead,
    Note,
    PatientProfileEmbeddingRead,
    PatientRead,
    ProtocolParsingRead,
    ProtocolRead,
    SiteRead,
)
```

# WebRecruitmentSDK

Methods:

- <code title="post /protocol-parsing">client.<a href="./src/web_recruitment_sdk/_client.py">protocol_parsing</a>(\*\*<a href="src/web_recruitment_sdk/types/client_protocol_parsing_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_read.py">ProtocolRead</a></code>

# Auth

## Roles

Types:

```python
from web_recruitment_sdk.types.auth import RoleRead, RoleListResponse
```

Methods:

- <code title="get /auth/roles">client.auth.roles.<a href="./src/web_recruitment_sdk/resources/auth/roles.py">list</a>() -> <a href="./src/web_recruitment_sdk/types/auth/role_list_response.py">RoleListResponse</a></code>

## Users

Types:

```python
from web_recruitment_sdk.types.auth import Authorization
```

Methods:

- <code title="patch /auth/users/{user_id}">client.auth.users.<a href="./src/web_recruitment_sdk/resources/auth/users.py">update</a>(user_id, \*\*<a href="src/web_recruitment_sdk/types/auth/user_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/auth/authorization.py">Authorization</a></code>

# Admin

## Users

Types:

```python
from web_recruitment_sdk.types.admin import UserWithAccount, UserListResponse
```

Methods:

- <code title="post /admin/users">client.admin.users.<a href="./src/web_recruitment_sdk/resources/admin/users.py">create</a>(\*\*<a href="src/web_recruitment_sdk/types/admin/user_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/admin/user_with_account.py">UserWithAccount</a></code>
- <code title="get /admin/users/{user_id}">client.admin.users.<a href="./src/web_recruitment_sdk/resources/admin/users.py">retrieve</a>(user_id) -> <a href="./src/web_recruitment_sdk/types/admin/user_with_account.py">UserWithAccount</a></code>
- <code title="get /admin/users">client.admin.users.<a href="./src/web_recruitment_sdk/resources/admin/users.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/admin/user_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/admin/user_list_response.py">UserListResponse</a></code>
- <code title="delete /admin/users/{user_id}">client.admin.users.<a href="./src/web_recruitment_sdk/resources/admin/users.py">delete</a>(user_id) -> None</code>
- <code title="get /admin/users/me">client.admin.users.<a href="./src/web_recruitment_sdk/resources/admin/users.py">retrieve_self</a>() -> <a href="./src/web_recruitment_sdk/types/admin/user_with_account.py">UserWithAccount</a></code>

# Patients

Types:

```python
from web_recruitment_sdk.types import PatientListResponse
```

Methods:

- <code title="get /patients/{patient_id}">client.patients.<a href="./src/web_recruitment_sdk/resources/patients/patients.py">retrieve</a>(patient_id) -> <a href="./src/web_recruitment_sdk/types/shared/patient_read.py">PatientRead</a></code>
- <code title="patch /patients/{patient_id}">client.patients.<a href="./src/web_recruitment_sdk/resources/patients/patients.py">update</a>(patient_id, \*\*<a href="src/web_recruitment_sdk/types/patient_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/patient_read.py">PatientRead</a></code>
- <code title="get /patients">client.patients.<a href="./src/web_recruitment_sdk/resources/patients/patients.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/patient_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/patient_list_response.py">PatientListResponse</a></code>

## Protocol

Types:

```python
from web_recruitment_sdk.types.patients import ProtocolRetrieveResponse
```

Methods:

- <code title="get /patients/protocol/{protocol_id}">client.patients.protocol.<a href="./src/web_recruitment_sdk/resources/patients/protocol.py">retrieve</a>(protocol_id, \*\*<a href="src/web_recruitment_sdk/types/patients/protocol_retrieve_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/patients/protocol_retrieve_response.py">ProtocolRetrieveResponse</a></code>

## Notes

Methods:

- <code title="post /patients/{patient_id}/notes">client.patients.notes.<a href="./src/web_recruitment_sdk/resources/patients/notes.py">create</a>(path_patient_id, \*\*<a href="src/web_recruitment_sdk/types/patients/note_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/note.py">Note</a></code>
- <code title="delete /patients/{patient_id}/notes/{note_id}">client.patients.notes.<a href="./src/web_recruitment_sdk/resources/patients/notes.py">delete</a>(note_id, \*, patient_id) -> None</code>

## ProtocolMatches

Types:

```python
from web_recruitment_sdk.types.patients import PatientProtocolMatch, ProtocolMatchListResponse
```

Methods:

- <code title="get /patients/{patient_id}/protocol-matches">client.patients.protocol_matches.<a href="./src/web_recruitment_sdk/resources/patients/protocol_matches.py">list</a>(patient_id) -> <a href="./src/web_recruitment_sdk/types/patients/protocol_match_list_response.py">ProtocolMatchListResponse</a></code>

# PatientsByExternalID

Methods:

- <code title="get /patients_by_external_id/{external_id}">client.patients_by_external_id.<a href="./src/web_recruitment_sdk/resources/patients_by_external_id.py">retrieve</a>(external_id) -> <a href="./src/web_recruitment_sdk/types/shared/patient_read.py">PatientRead</a></code>

# Protocols

Types:

```python
from web_recruitment_sdk.types import ProtocolListResponse
```

Methods:

- <code title="post /protocols">client.protocols.<a href="./src/web_recruitment_sdk/resources/protocols/protocols.py">create</a>(\*\*<a href="src/web_recruitment_sdk/types/protocol_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_read.py">ProtocolRead</a></code>
- <code title="get /protocols/{protocol_id}">client.protocols.<a href="./src/web_recruitment_sdk/resources/protocols/protocols.py">retrieve</a>(protocol_id) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_read.py">ProtocolRead</a></code>
- <code title="patch /protocols/{protocol_id}">client.protocols.<a href="./src/web_recruitment_sdk/resources/protocols/protocols.py">update</a>(protocol_id, \*\*<a href="src/web_recruitment_sdk/types/protocol_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_read.py">ProtocolRead</a></code>
- <code title="get /protocols">client.protocols.<a href="./src/web_recruitment_sdk/resources/protocols/protocols.py">list</a>() -> <a href="./src/web_recruitment_sdk/types/protocol_list_response.py">ProtocolListResponse</a></code>
- <code title="delete /protocols/{protocol_id}">client.protocols.<a href="./src/web_recruitment_sdk/resources/protocols/protocols.py">delete</a>(protocol_id) -> None</code>

## ProtocolParsing

Methods:

- <code title="get /protocols/{protocol_id}/protocol-parsing">client.protocols.protocol_parsing.<a href="./src/web_recruitment_sdk/resources/protocols/protocol_parsing.py">list</a>(protocol_id) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_parsing_read.py">ProtocolParsingRead</a></code>

## Matches

Types:

```python
from web_recruitment_sdk.types.protocols import PatientMatch, MatchListResponse
```

Methods:

- <code title="get /protocols/{protocol_id}/matches">client.protocols.matches.<a href="./src/web_recruitment_sdk/resources/protocols/matches.py">list</a>(protocol_id) -> <a href="./src/web_recruitment_sdk/types/protocols/match_list_response.py">MatchListResponse</a></code>

## Criteria

Types:

```python
from web_recruitment_sdk.types.protocols import CriterionListResponse
```

Methods:

- <code title="get /protocols/{protocol_id}/criteria">client.protocols.criteria.<a href="./src/web_recruitment_sdk/resources/protocols/criteria.py">list</a>(protocol_id) -> <a href="./src/web_recruitment_sdk/types/protocols/criterion_list_response.py">CriterionListResponse</a></code>

## Sites

Types:

```python
from web_recruitment_sdk.types.protocols import ProtocolSite, SiteListResponse
```

Methods:

- <code title="post /protocols/{protocol_id}/sites/{site_id}">client.protocols.sites.<a href="./src/web_recruitment_sdk/resources/protocols/sites.py">create</a>(site_id, \*, protocol_id) -> <a href="./src/web_recruitment_sdk/types/protocols/protocol_site.py">ProtocolSite</a></code>
- <code title="get /protocols/{protocol_id}/sites">client.protocols.sites.<a href="./src/web_recruitment_sdk/resources/protocols/sites.py">list</a>(protocol_id) -> <a href="./src/web_recruitment_sdk/types/protocols/site_list_response.py">SiteListResponse</a></code>
- <code title="delete /protocols/{protocol_id}/sites/{site_id}">client.protocols.sites.<a href="./src/web_recruitment_sdk/resources/protocols/sites.py">delete</a>(site_id, \*, protocol_id) -> None</code>

## CriteriaInstances

Types:

```python
from web_recruitment_sdk.types.protocols import (
    CriteriaInstanceWithCriteria,
    CriteriaInstanceListResponse,
)
```

Methods:

- <code title="get /protocols/{protocol_id}/criteria_instances">client.protocols.criteria_instances.<a href="./src/web_recruitment_sdk/resources/protocols/criteria_instances.py">list</a>(protocol_id, \*\*<a href="src/web_recruitment_sdk/types/protocols/criteria_instance_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/protocols/criteria_instance_list_response.py">CriteriaInstanceListResponse</a></code>

## Funnel

Types:

```python
from web_recruitment_sdk.types.protocols import ProtocolFunnelStats
```

Methods:

- <code title="get /protocols/{protocol_id}/funnel">client.protocols.funnel.<a href="./src/web_recruitment_sdk/resources/protocols/funnel.py">retrieve</a>(protocol_id, \*\*<a href="src/web_recruitment_sdk/types/protocols/funnel_retrieve_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/protocols/protocol_funnel_stats.py">ProtocolFunnelStats</a></code>

# ProtocolParsings

Types:

```python
from web_recruitment_sdk.types import ProtocolParsingListResponse
```

Methods:

- <code title="get /protocol-parsing">client.protocol_parsings.<a href="./src/web_recruitment_sdk/resources/protocol_parsings.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/protocol_parsing_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/protocol_parsing_list_response.py">ProtocolParsingListResponse</a></code>

# Criteria

Methods:

- <code title="post /criteria">client.criteria.<a href="./src/web_recruitment_sdk/resources/criteria.py">create</a>(\*\*<a href="src/web_recruitment_sdk/types/criterion_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/criteria_read.py">CriteriaRead</a></code>
- <code title="get /criteria/{criteria_id}">client.criteria.<a href="./src/web_recruitment_sdk/resources/criteria.py">retrieve</a>(criteria_id) -> <a href="./src/web_recruitment_sdk/types/shared/criteria_read.py">CriteriaRead</a></code>
- <code title="put /criteria/{criterion_id}">client.criteria.<a href="./src/web_recruitment_sdk/resources/criteria.py">update</a>(criterion_id, \*\*<a href="src/web_recruitment_sdk/types/criterion_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/criteria_read.py">CriteriaRead</a></code>

# Appointments

Types:

```python
from web_recruitment_sdk.types import AppointmentListResponse
```

Methods:

- <code title="get /appointments/{appointment_id}">client.appointments.<a href="./src/web_recruitment_sdk/resources/appointments.py">retrieve</a>(appointment_id) -> <a href="./src/web_recruitment_sdk/types/shared/appointment_read.py">AppointmentRead</a></code>
- <code title="get /appointments">client.appointments.<a href="./src/web_recruitment_sdk/resources/appointments.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/appointment_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/appointment_list_response.py">AppointmentListResponse</a></code>

# Sites

Types:

```python
from web_recruitment_sdk.types import SiteListResponse
```

Methods:

- <code title="get /sites/{site_id}">client.sites.<a href="./src/web_recruitment_sdk/resources/sites.py">retrieve</a>(site_id) -> <a href="./src/web_recruitment_sdk/types/shared/site_read.py">SiteRead</a></code>
- <code title="get /sites">client.sites.<a href="./src/web_recruitment_sdk/resources/sites.py">list</a>() -> <a href="./src/web_recruitment_sdk/types/site_list_response.py">SiteListResponse</a></code>

# Health

Types:

```python
from web_recruitment_sdk.types import HealthRetrieveResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/web_recruitment_sdk/resources/health.py">retrieve</a>() -> <a href="./src/web_recruitment_sdk/types/health_retrieve_response.py">object</a></code>

# System

Types:

```python
from web_recruitment_sdk.types import BulkInsertResult, SystemPingResponse
```

Methods:

- <code title="get /system/ping">client.system.<a href="./src/web_recruitment_sdk/resources/system/system.py">ping</a>() -> <a href="./src/web_recruitment_sdk/types/system_ping_response.py">object</a></code>

## Protocols

Types:

```python
from web_recruitment_sdk.types.system import ProtocolListResponse
```

Methods:

- <code title="get /system/{tenant_id}/protocols/{protocol_id}">client.system.protocols.<a href="./src/web_recruitment_sdk/resources/system/protocols/protocols.py">retrieve</a>(protocol_id, \*, tenant_id) -> <a href="./src/web_recruitment_sdk/types/shared/protocol_read.py">ProtocolRead</a></code>
- <code title="get /system/{tenant_id}/protocols">client.system.protocols.<a href="./src/web_recruitment_sdk/resources/system/protocols/protocols.py">list</a>(tenant_id) -> <a href="./src/web_recruitment_sdk/types/system/protocol_list_response.py">ProtocolListResponse</a></code>

### Criteria

Types:

```python
from web_recruitment_sdk.types.system.protocols import CriterionListResponse
```

Methods:

- <code title="get /system/{tenant_id}/protocols/{protocol_id}/criteria">client.system.protocols.criteria.<a href="./src/web_recruitment_sdk/resources/system/protocols/criteria.py">list</a>(protocol_id, \*, tenant_id) -> <a href="./src/web_recruitment_sdk/types/system/protocols/criterion_list_response.py">CriterionListResponse</a></code>

## ProtocolParsing

Types:

```python
from web_recruitment_sdk.types.system import (
    ProtocolParsingErrorResponse,
    ProtocolParsingSuccessResponse,
)
```

Methods:

- <code title="post /system/{tenant_id}/protocol-parsing/{job_id}/error">client.system.protocol_parsing.<a href="./src/web_recruitment_sdk/resources/system/protocol_parsing.py">error</a>(job_id, \*, tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/protocol_parsing_error_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/protocol_parsing_error_response.py">object</a></code>
- <code title="post /system/{tenant_id}/protocol-parsing/{job_id}/success">client.system.protocol_parsing.<a href="./src/web_recruitment_sdk/resources/system/protocol_parsing.py">success</a>(job_id, \*, tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/protocol_parsing_success_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/protocol_parsing_success_response.py">object</a></code>

## Sites

Types:

```python
from web_recruitment_sdk.types.system import SiteListResponse, SiteDeleteResponse
```

Methods:

- <code title="post /system/{tenant_id}/sites">client.system.sites.<a href="./src/web_recruitment_sdk/resources/system/sites/sites.py">create</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/site_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/site_read.py">SiteRead</a></code>
- <code title="get /system/{tenant_id}/sites/{site_id}">client.system.sites.<a href="./src/web_recruitment_sdk/resources/system/sites/sites.py">retrieve</a>(site_id, \*, tenant_id) -> <a href="./src/web_recruitment_sdk/types/shared/site_read.py">SiteRead</a></code>
- <code title="patch /system/{tenant_id}/sites/{site_id}">client.system.sites.<a href="./src/web_recruitment_sdk/resources/system/sites/sites.py">update</a>(site_id, \*, tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/site_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/site_read.py">SiteRead</a></code>
- <code title="get /system/{tenant_id}/sites">client.system.sites.<a href="./src/web_recruitment_sdk/resources/system/sites/sites.py">list</a>(tenant_id) -> <a href="./src/web_recruitment_sdk/types/system/site_list_response.py">SiteListResponse</a></code>
- <code title="delete /system/{tenant_id}/sites/{site_id}">client.system.sites.<a href="./src/web_recruitment_sdk/resources/system/sites/sites.py">delete</a>(site_id, \*, tenant_id) -> <a href="./src/web_recruitment_sdk/types/system/site_delete_response.py">object</a></code>

### Trially

#### Protocols

Types:

```python
from web_recruitment_sdk.types.system.sites.trially import ProtocolListResponse
```

Methods:

- <code title="get /system/{tenant_id}/sites/trially/{trially_site_id}/protocols">client.system.sites.trially.protocols.<a href="./src/web_recruitment_sdk/resources/system/sites/trially/protocols.py">list</a>(trially_site_id, \*, tenant_id) -> <a href="./src/web_recruitment_sdk/types/system/sites/trially/protocol_list_response.py">ProtocolListResponse</a></code>

## Appointments

Types:

```python
from web_recruitment_sdk.types.system import AppointmentListResponse, AppointmentBulkResponse
```

Methods:

- <code title="get /system/{tenant_id}/appointments">client.system.appointments.<a href="./src/web_recruitment_sdk/resources/system/appointments.py">list</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/appointment_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/appointment_list_response.py">AppointmentListResponse</a></code>
- <code title="delete /system/{tenant_id}/appointments/{appointment_id}">client.system.appointments.<a href="./src/web_recruitment_sdk/resources/system/appointments.py">delete</a>(appointment_id, \*, tenant_id) -> None</code>
- <code title="post /system/{tenant_id}/appointments/bulk">client.system.appointments.<a href="./src/web_recruitment_sdk/resources/system/appointments.py">bulk</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/appointment_bulk_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/appointment_bulk_response.py">AppointmentBulkResponse</a></code>

## Patients

Methods:

- <code title="post /system/{tenant_id}/patients">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">create</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/patient_read.py">PatientRead</a></code>
- <code title="patch /system/{tenant_id}/patients/{patient_id}">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">update</a>(patient_id, \*, tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/patient_read.py">PatientRead</a></code>
- <code title="put /system/{tenant_id}/patients/bulk/allergies">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">bulk_allergies</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_bulk_allergies_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>
- <code title="put /system/{tenant_id}/patients/bulk/conditions">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">bulk_conditions</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_bulk_conditions_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>
- <code title="put /system/{tenant_id}/patients/bulk/medications">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">bulk_medications</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_bulk_medications_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>
- <code title="put /system/{tenant_id}/patients/bulk/procedures">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">bulk_procedures</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_bulk_procedures_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>
- <code title="put /system/{tenant_id}/patients/bulk">client.system.patients.<a href="./src/web_recruitment_sdk/resources/system/patients/patients.py">bulk_update</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_bulk_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>

### BulkVitals

Methods:

- <code title="put /system/{tenant_id}/patients/bulk/patient_vitals">client.system.patients.bulk_vitals.<a href="./src/web_recruitment_sdk/resources/system/patients/bulk_vitals.py">update</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patients/bulk_vital_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>

### BulkDemographics

Methods:

- <code title="put /system/{tenant_id}/patients/bulk/patient_demographics">client.system.patients.bulk_demographics.<a href="./src/web_recruitment_sdk/resources/system/patients/bulk_demographics.py">update</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patients/bulk_demographic_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>

### ClosestPatientProfileDocuments

Types:

```python
from web_recruitment_sdk.types.system.patients import ClosestPatientProfileDocumentCreateResponse
```

Methods:

- <code title="post /system/{tenant_id}/patients/closest_patient_profile_documents">client.system.patients.closest_patient_profile_documents.<a href="./src/web_recruitment_sdk/resources/system/patients/closest_patient_profile_documents.py">create</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patients/closest_patient_profile_document_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/patients/closest_patient_profile_document_create_response.py">ClosestPatientProfileDocumentCreateResponse</a></code>

### BulkProfileEmbeddings

Methods:

- <code title="put /system/{tenant_id}/patients/bulk/patient_profile_embeddings">client.system.patients.bulk_profile_embeddings.<a href="./src/web_recruitment_sdk/resources/system/patients/bulk_profile_embeddings.py">update</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patients/bulk_profile_embedding_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>

## CriteriaInstances

Types:

```python
from web_recruitment_sdk.types.system import CriteriaInstance, CriteriaInstanceCreateResponse
```

Methods:

- <code title="post /system/{tenant_id}/criteria_instances">client.system.criteria_instances.<a href="./src/web_recruitment_sdk/resources/system/criteria_instances.py">create</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/criteria_instance_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/criteria_instance_create_response.py">CriteriaInstanceCreateResponse</a></code>

## BulkCriteriaInstances

Methods:

- <code title="put /system/{tenant_id}/bulk/criteria_instances">client.system.bulk_criteria_instances.<a href="./src/web_recruitment_sdk/resources/system/bulk_criteria_instances.py">update</a>(tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/bulk_criteria_instance_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/bulk_insert_result.py">BulkInsertResult</a></code>

## PatientCtmsExports

Types:

```python
from web_recruitment_sdk.types.system import PatientCtmsExportUpdateResponse
```

Methods:

- <code title="patch /system/{tenant_id}/patient-ctms-exports/{patient_ctms_export_id}">client.system.patient_ctms_exports.<a href="./src/web_recruitment_sdk/resources/system/patient_ctms_exports.py">update</a>(patient_ctms_export_id, \*, tenant_id, \*\*<a href="src/web_recruitment_sdk/types/system/patient_ctms_export_update_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/system/patient_ctms_export_update_response.py">PatientCtmsExportUpdateResponse</a></code>

# FeatureFlags

Types:

```python
from web_recruitment_sdk.types import FeatureFlag
```

Methods:

- <code title="get /feature-flags/{flag_key}">client.feature_flags.<a href="./src/web_recruitment_sdk/resources/feature_flags.py">retrieve</a>(flag_key) -> <a href="./src/web_recruitment_sdk/types/feature_flag.py">FeatureFlag</a></code>

# ExportJobs

Types:

```python
from web_recruitment_sdk.types import ExportJobRead, ExportJobStatusRead, ExportJobListResponse
```

Methods:

- <code title="get /export-jobs">client.export_jobs.<a href="./src/web_recruitment_sdk/resources/export_jobs/export_jobs.py">list</a>() -> <a href="./src/web_recruitment_sdk/types/export_job_list_response.py">ExportJobListResponse</a></code>

## Sites

Methods:

- <code title="post /export-job/sites/{site_id}">client.export_jobs.sites.<a href="./src/web_recruitment_sdk/resources/export_jobs/sites.py">create</a>(site_id, \*\*<a href="src/web_recruitment_sdk/types/export_jobs/site_create_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/export_job_read.py">ExportJobRead</a></code>

# Dashboards

## Medications

Methods:

- <code title="get /dashboards/medications">client.dashboards.medications.<a href="./src/web_recruitment_sdk/resources/dashboards/medications.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/medication_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>

## Conditions

Methods:

- <code title="get /dashboards/conditions">client.dashboards.conditions.<a href="./src/web_recruitment_sdk/resources/dashboards/conditions.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/condition_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>

## Procedures

Methods:

- <code title="get /dashboards/procedures">client.dashboards.procedures.<a href="./src/web_recruitment_sdk/resources/dashboards/procedures.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/procedure_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>

## AgeDistribution

Methods:

- <code title="get /dashboards/age-distribution">client.dashboards.age_distribution.<a href="./src/web_recruitment_sdk/resources/dashboards/age_distribution.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/age_distribution_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>

## GenderDistribution

Methods:

- <code title="get /dashboards/gender-distribution">client.dashboards.gender_distribution.<a href="./src/web_recruitment_sdk/resources/dashboards/gender_distribution.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/gender_distribution_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>

## EthnicDistribution

Methods:

- <code title="get /dashboards/ethnic-distribution">client.dashboards.ethnic_distribution.<a href="./src/web_recruitment_sdk/resources/dashboards/ethnic_distribution.py">list</a>(\*\*<a href="src/web_recruitment_sdk/types/dashboards/ethnic_distribution_list_params.py">params</a>) -> <a href="./src/web_recruitment_sdk/types/shared/chart_response.py">ChartResponse</a></code>
