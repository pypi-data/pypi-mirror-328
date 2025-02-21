from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_project_estimation_estimate_project_estimation_post import (
    BodyProjectEstimationEstimateProjectEstimationPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.project_estimation_answer import ProjectEstimationAnswer
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyProjectEstimationEstimateProjectEstimationPost,
    api_key: str,
    business_info: Union[Unset, str] = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["api_key"] = api_key

    params["business_info"] = business_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/estimate/project_estimation",
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    if response.status_code == 200:
        response_200 = ProjectEstimationAnswer.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyProjectEstimationEstimateProjectEstimationPost,
    api_key: str,
    business_info: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    """Project estimation

     Analyzes an uploaded project file based on knowledgebase data and returns a project estimate with as
    much data as possible

    Args:
        api_key (str): API access key
        business_info (Union[Unset, str]): Optional business information Default: ''.
        body (BodyProjectEstimationEstimateProjectEstimationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ProjectEstimationAnswer]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
        business_info=business_info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyProjectEstimationEstimateProjectEstimationPost,
    api_key: str,
    business_info: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    """Project estimation

     Analyzes an uploaded project file based on knowledgebase data and returns a project estimate with as
    much data as possible

    Args:
        api_key (str): API access key
        business_info (Union[Unset, str]): Optional business information Default: ''.
        body (BodyProjectEstimationEstimateProjectEstimationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ProjectEstimationAnswer]
    """

    return sync_detailed(
        client=client,
        body=body,
        api_key=api_key,
        business_info=business_info,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyProjectEstimationEstimateProjectEstimationPost,
    api_key: str,
    business_info: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    """Project estimation

     Analyzes an uploaded project file based on knowledgebase data and returns a project estimate with as
    much data as possible

    Args:
        api_key (str): API access key
        business_info (Union[Unset, str]): Optional business information Default: ''.
        body (BodyProjectEstimationEstimateProjectEstimationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ProjectEstimationAnswer]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
        business_info=business_info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BodyProjectEstimationEstimateProjectEstimationPost,
    api_key: str,
    business_info: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ProjectEstimationAnswer]]:
    """Project estimation

     Analyzes an uploaded project file based on knowledgebase data and returns a project estimate with as
    much data as possible

    Args:
        api_key (str): API access key
        business_info (Union[Unset, str]): Optional business information Default: ''.
        body (BodyProjectEstimationEstimateProjectEstimationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ProjectEstimationAnswer]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            api_key=api_key,
            business_info=business_info,
        )
    ).parsed
