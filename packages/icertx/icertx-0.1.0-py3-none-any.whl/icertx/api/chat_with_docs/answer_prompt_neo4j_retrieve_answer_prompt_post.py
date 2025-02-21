from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.prompt_answer import PromptAnswer
from ...models.prompt_input import PromptInput
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PromptInput,
    api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["api_key"] = api_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/neo4j/retrieve/answer_prompt",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PromptAnswer]]:
    if response.status_code == 200:
        response_200 = PromptAnswer.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, PromptAnswer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PromptInput,
    api_key: str,
) -> Response[Union[HTTPValidationError, PromptAnswer]]:
    """Answer a custom prompt

     Provides an answer to a custom prompt. The Answer is generated based on knowledgegraph Ensure you
    did run neo4j knowledge graph first

    Args:
        api_key (str): API access key
        body (PromptInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PromptAnswer]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PromptInput,
    api_key: str,
) -> Optional[Union[HTTPValidationError, PromptAnswer]]:
    """Answer a custom prompt

     Provides an answer to a custom prompt. The Answer is generated based on knowledgegraph Ensure you
    did run neo4j knowledge graph first

    Args:
        api_key (str): API access key
        body (PromptInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PromptAnswer]
    """

    return sync_detailed(
        client=client,
        body=body,
        api_key=api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PromptInput,
    api_key: str,
) -> Response[Union[HTTPValidationError, PromptAnswer]]:
    """Answer a custom prompt

     Provides an answer to a custom prompt. The Answer is generated based on knowledgegraph Ensure you
    did run neo4j knowledge graph first

    Args:
        api_key (str): API access key
        body (PromptInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PromptAnswer]]
    """

    kwargs = _get_kwargs(
        body=body,
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PromptInput,
    api_key: str,
) -> Optional[Union[HTTPValidationError, PromptAnswer]]:
    """Answer a custom prompt

     Provides an answer to a custom prompt. The Answer is generated based on knowledgegraph Ensure you
    did run neo4j knowledge graph first

    Args:
        api_key (str): API access key
        body (PromptInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PromptAnswer]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            api_key=api_key,
        )
    ).parsed
