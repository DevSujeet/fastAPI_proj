import ast
import json
import uuid
from logging import getLogger

from httpx import AsyncClient, Response, Client

MAX_RETRY = 0

logger = getLogger(__name__)

'''
Sample usage of sync and async API request
# POST request with query parameter
    url_with_query = "https://example.com/api/resource"
    query_params = {"param1": "value1"}
    response_with_query = await async_api_request(
        url=url_with_query,
        method="POST",
        params=query_params,
        headers={"Content-Type": "application/json"}
    )
    print(f"Response with query params: {response_with_query.status_code}, {response_with_query.text}")

    # POST request with JSON payload
    url_with_json = "https://example.com/api/resource"
    json_payload = {"key1": "value1", "key2": "value2"}
    response_with_json = await async_api_request(
        url=url_with_json,
        method="POST",
        json=json_payload,
        headers={"Content-Type": "application/json"}
    )
    print(f"Response with JSON payload: {response_with_json.status_code}, {response_with_json.text}")

'''
def url_builder(base_url, *args):
    return "/".join([base_url.strip("/"), *[x.strip("/") for x in args]])


def sync_api_request(url, files=None, **kwargs) -> Response:
    """
    This function will take values in
    :param url:
    :param files:
    :param kwargs:
    :return:
    """
    parameters = {
        "url": url,
        "files": files,
        "method": kwargs.get("method", "GET").upper(),
        **kwargs
    }
    logger.debug(f"Sync API call {url} headers {kwargs.get('headers',None)}")
    with Client(timeout=kwargs.get("timeout", 90)) as client:
        return client.request(**parameters)


async def async_api_request(url, timeout: 90, **kwargs) -> Response:
    parameters = {
        "url": url,
        **kwargs
    }
    logger.debug(f"Async API call {url} headers {kwargs.get('headers')}")
    async with AsyncClient(timeout=kwargs.get("timeout", timeout)) as async_client:
        return await async_client.request(**parameters)