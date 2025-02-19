# API

## Workers

Types:

```python
from brainbase_labs.types.api import (
    Workers,
    WorkerListResponse,
    WorkerCreateTwilioIntegrationResponse,
)
```

Methods:

- <code title="post /api/workers">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">create</a>(\*\*<a href="src/brainbase_labs/types/api/worker_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/workers.py">Workers</a></code>
- <code title="get /api/workers/{id}">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">retrieve</a>(id) -> <a href="./src/brainbase_labs/types/api/workers/workers.py">Workers</a></code>
- <code title="patch /api/workers/{id}">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">update</a>(id, \*\*<a href="src/brainbase_labs/types/api/worker_update_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/workers.py">Workers</a></code>
- <code title="get /api/workers">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">list</a>() -> <a href="./src/brainbase_labs/types/api/worker_list_response.py">WorkerListResponse</a></code>
- <code title="delete /api/workers/{id}">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">delete</a>(id) -> None</code>
- <code title="post /api/workers/{workerId}/integrations/twilio/create">client.api.workers.<a href="./src/brainbase_labs/resources/api/workers/workers.py">create_twilio_integration</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/worker_create_twilio_integration_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/worker_create_twilio_integration_response.py">WorkerCreateTwilioIntegrationResponse</a></code>

### Deployments

#### Voice

Types:

```python
from brainbase_labs.types.api.workers.deployments import VoiceDeployment, VoiceListResponse
```

Methods:

- <code title="post /api/workers/{workerId}/deployments/voice">client.api.workers.deployments.voice.<a href="./src/brainbase_labs/resources/api/workers/deployments/voice.py">create</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/deployments/voice_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/deployments/voice_deployment.py">VoiceDeployment</a></code>
- <code title="get /api/workers/{workerId}/deployments/voice/{deploymentId}">client.api.workers.deployments.voice.<a href="./src/brainbase_labs/resources/api/workers/deployments/voice.py">retrieve</a>(deployment_id, \*, worker_id) -> <a href="./src/brainbase_labs/types/api/workers/deployments/voice_deployment.py">VoiceDeployment</a></code>
- <code title="put /api/workers/{workerId}/deployments/voice/{deploymentId}">client.api.workers.deployments.voice.<a href="./src/brainbase_labs/resources/api/workers/deployments/voice.py">update</a>(deployment_id, \*, worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/deployments/voice_update_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/deployments/voice_deployment.py">VoiceDeployment</a></code>
- <code title="get /api/workers/{workerId}/deployments/voice">client.api.workers.deployments.voice.<a href="./src/brainbase_labs/resources/api/workers/deployments/voice.py">list</a>(worker_id) -> <a href="./src/brainbase_labs/types/api/workers/deployments/voice_list_response.py">VoiceListResponse</a></code>
- <code title="delete /api/workers/{workerId}/deployments/voice/{deploymentId}">client.api.workers.deployments.voice.<a href="./src/brainbase_labs/resources/api/workers/deployments/voice.py">delete</a>(deployment_id, \*, worker_id) -> None</code>

### Flows

Types:

```python
from brainbase_labs.types.api.workers import Flows, FlowListResponse
```

Methods:

- <code title="post /api/workers/{workerId}/flows">client.api.workers.flows.<a href="./src/brainbase_labs/resources/api/workers/flows.py">create</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/flow_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/flows.py">Flows</a></code>
- <code title="get /api/workers/{workerId}/flows/{flowId}">client.api.workers.flows.<a href="./src/brainbase_labs/resources/api/workers/flows.py">retrieve</a>(flow_id, \*, worker_id) -> <a href="./src/brainbase_labs/types/api/workers/flows.py">Flows</a></code>
- <code title="put /api/workers/{workerId}/flows/{flowId}">client.api.workers.flows.<a href="./src/brainbase_labs/resources/api/workers/flows.py">update</a>(flow_id, \*, worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/flow_update_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/flows.py">Flows</a></code>
- <code title="get /api/workers/{workerId}/flows">client.api.workers.flows.<a href="./src/brainbase_labs/resources/api/workers/flows.py">list</a>(worker_id) -> <a href="./src/brainbase_labs/types/api/workers/flow_list_response.py">FlowListResponse</a></code>
- <code title="delete /api/workers/{workerId}/flows/{flowId}">client.api.workers.flows.<a href="./src/brainbase_labs/resources/api/workers/flows.py">delete</a>(flow_id, \*, worker_id) -> None</code>

### Resources

Types:

```python
from brainbase_labs.types.api.workers import RagResource
```

Methods:

- <code title="get /api/workers/{workerId}/resources/{resourceId}">client.api.workers.resources.<a href="./src/brainbase_labs/resources/api/workers/resources/resources.py">retrieve</a>(resource_id, \*, worker_id) -> <a href="./src/brainbase_labs/types/api/workers/rag_resource.py">RagResource</a></code>
- <code title="delete /api/workers/{workerId}/resources/{resourceId}">client.api.workers.resources.<a href="./src/brainbase_labs/resources/api/workers/resources/resources.py">delete</a>(resource_id, \*, worker_id) -> None</code>

#### Link

Types:

```python
from brainbase_labs.types.api.workers.resources import LinkListResponse
```

Methods:

- <code title="post /api/workers/{workerId}/resources/link">client.api.workers.resources.link.<a href="./src/brainbase_labs/resources/api/workers/resources/link.py">create</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/resources/link_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/rag_resource.py">RagResource</a></code>
- <code title="get /api/workers/{workerId}/resources/link">client.api.workers.resources.link.<a href="./src/brainbase_labs/resources/api/workers/resources/link.py">list</a>(worker_id) -> <a href="./src/brainbase_labs/types/api/workers/resources/link_list_response.py">LinkListResponse</a></code>

#### File

Types:

```python
from brainbase_labs.types.api.workers.resources import FileListResponse
```

Methods:

- <code title="post /api/workers/{workerId}/resources/file">client.api.workers.resources.file.<a href="./src/brainbase_labs/resources/api/workers/resources/file.py">create</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/resources/file_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/rag_resource.py">RagResource</a></code>
- <code title="get /api/workers/{workerId}/resources/file">client.api.workers.resources.file.<a href="./src/brainbase_labs/resources/api/workers/resources/file.py">list</a>(worker_id) -> <a href="./src/brainbase_labs/types/api/workers/resources/file_list_response.py">FileListResponse</a></code>

### Tests

Types:

```python
from brainbase_labs.types.api.workers import TestCreateResponse
```

Methods:

- <code title="post /api/workers/{workerId}/tests">client.api.workers.tests.<a href="./src/brainbase_labs/resources/api/workers/tests.py">create</a>(worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/test_create_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/workers/test_create_response.py">TestCreateResponse</a></code>
- <code title="put /api/workers/{workerId}/tests/{testId}">client.api.workers.tests.<a href="./src/brainbase_labs/resources/api/workers/tests.py">update</a>(test_id, \*, worker_id, \*\*<a href="src/brainbase_labs/types/api/workers/test_update_params.py">params</a>) -> None</code>
- <code title="delete /api/workers/{workerId}/tests/{testId}">client.api.workers.tests.<a href="./src/brainbase_labs/resources/api/workers/tests.py">delete</a>(test_id, \*, worker_id) -> None</code>
- <code title="get /api/workers/{workerId}/tests/{testId}/runs">client.api.workers.tests.<a href="./src/brainbase_labs/resources/api/workers/tests.py">get_runs</a>(test_id, \*, worker_id) -> None</code>
- <code title="post /api/workers/{workerId}/tests/{testId}/run">client.api.workers.tests.<a href="./src/brainbase_labs/resources/api/workers/tests.py">run</a>(test_id, \*, worker_id) -> None</code>

## Team

Types:

```python
from brainbase_labs.types.api import TeamRetrieveResponse, TeamRegisterPhoneNumberResponse
```

Methods:

- <code title="get /api/team">client.api.team.<a href="./src/brainbase_labs/resources/api/team.py">retrieve</a>(\*\*<a href="src/brainbase_labs/types/api/team_retrieve_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/team_retrieve_response.py">TeamRetrieveResponse</a></code>
- <code title="post /api/team/register_phone_number">client.api.team.<a href="./src/brainbase_labs/resources/api/team.py">register_phone_number</a>(\*\*<a href="src/brainbase_labs/types/api/team_register_phone_number_params.py">params</a>) -> <a href="./src/brainbase_labs/types/api/team_register_phone_number_response.py">TeamRegisterPhoneNumberResponse</a></code>
