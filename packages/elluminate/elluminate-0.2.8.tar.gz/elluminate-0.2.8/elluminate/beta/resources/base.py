from __future__ import annotations

import asyncio
import time
from typing import TYPE_CHECKING, Type

from pydantic import BaseModel

from elluminate.beta.schemas.base import BatchCreateStatus, TResult

if TYPE_CHECKING:
    from elluminate.beta.client import Client


class BaseResource:
    def __init__(self, client: Client) -> None:
        self._client = client
        self._aget = client._aget
        self._apost = client._apost
        self._aput = client._aput
        self._adelete = client._adelete
        self._semaphore = client._semaphore

    async def _abatch_create(
        self,
        path: str,
        batch_request: BaseModel,
        batch_response_type: Type[BatchCreateStatus[TResult]],
        timeout: float | None = None,
        polling_interval: float = 3.0,
    ) -> list[TResult]:
        """Generic batch create operation that waits for completion.

        Args:
            path (str): API endpoint path
            batch_request (BaseModel): Batch request object containing items and options
            batch_response_type (Type[BatchCreateStatus[TResult]]): Type of the batch response
            timeout (float | None): Optional timeout in seconds
            polling_interval (float): Time between status checks

        Returns:
            List of created items

        Raises:
            TimeoutError: If operation times out
            RuntimeError: If operation fails

        """
        # Initiate batch operation
        response = await self._apost(f"{path}", json=batch_request.model_dump())
        task_id = response.json()

        # Poll for completion
        start_time = time.time()
        while timeout is None or time.time() - start_time < timeout:
            status_response = await self._aget(f"{path}/{task_id}")
            status = batch_response_type.model_validate(status_response.json())

            if status.status == "FAILURE":
                raise RuntimeError(f"Batch creation failed: {status.error_msg}")
            elif status.status == "SUCCESS":
                if status.result is None:
                    raise RuntimeError("Batch creation succeeded but no results returned")
                return status.result

            await asyncio.sleep(polling_interval)

        raise TimeoutError(f"Batch operation timed out after {timeout} seconds")
