# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .team import (
    TeamResource,
    AsyncTeamResource,
    TeamResourceWithRawResponse,
    AsyncTeamResourceWithRawResponse,
    TeamResourceWithStreamingResponse,
    AsyncTeamResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .workers.workers import (
    WorkersResource,
    AsyncWorkersResource,
    WorkersResourceWithRawResponse,
    AsyncWorkersResourceWithRawResponse,
    WorkersResourceWithStreamingResponse,
    AsyncWorkersResourceWithStreamingResponse,
)

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def workers(self) -> WorkersResource:
        return WorkersResource(self._client)

    @cached_property
    def team(self) -> TeamResource:
        return TeamResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-labs-python-sdk#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-labs-python-sdk#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def workers(self) -> AsyncWorkersResource:
        return AsyncWorkersResource(self._client)

    @cached_property
    def team(self) -> AsyncTeamResource:
        return AsyncTeamResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-labs-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/BrainbaseHQ/brainbase-labs-python-sdk#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def workers(self) -> WorkersResourceWithRawResponse:
        return WorkersResourceWithRawResponse(self._api.workers)

    @cached_property
    def team(self) -> TeamResourceWithRawResponse:
        return TeamResourceWithRawResponse(self._api.team)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def workers(self) -> AsyncWorkersResourceWithRawResponse:
        return AsyncWorkersResourceWithRawResponse(self._api.workers)

    @cached_property
    def team(self) -> AsyncTeamResourceWithRawResponse:
        return AsyncTeamResourceWithRawResponse(self._api.team)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def workers(self) -> WorkersResourceWithStreamingResponse:
        return WorkersResourceWithStreamingResponse(self._api.workers)

    @cached_property
    def team(self) -> TeamResourceWithStreamingResponse:
        return TeamResourceWithStreamingResponse(self._api.team)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def workers(self) -> AsyncWorkersResourceWithStreamingResponse:
        return AsyncWorkersResourceWithStreamingResponse(self._api.workers)

    @cached_property
    def team(self) -> AsyncTeamResourceWithStreamingResponse:
        return AsyncTeamResourceWithStreamingResponse(self._api.team)
