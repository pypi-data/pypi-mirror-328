from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_attachment import CreateAttachment
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAttachment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/attachments",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 201:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 401:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAttachment,
) -> Response[Any]:
    """Upload file attachment

     This endpoint is used for uploading file attachments to various entities.


    For a detailed guide on uploading files to sections within ELN & Knowledgebase entities, including a
    step-by-step process and practical examples in **Python**, refer to our article on: [Uploading Files
    to Experiments via API](https://help.labguru.com/en/articles/9636468-uploading-files-to-experiments-
    via-api)


    Args:
        body (CreateAttachment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAttachment,
) -> Response[Any]:
    """Upload file attachment

     This endpoint is used for uploading file attachments to various entities.


    For a detailed guide on uploading files to sections within ELN & Knowledgebase entities, including a
    step-by-step process and practical examples in **Python**, refer to our article on: [Uploading Files
    to Experiments via API](https://help.labguru.com/en/articles/9636468-uploading-files-to-experiments-
    via-api)


    Args:
        body (CreateAttachment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
