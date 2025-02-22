from __future__ import annotations

import json
import logging
from typing import List
import asyncio

from zmp_zcp_toolkit.wrapper.parameters import (
    GetAlerts,
    GetAlertDetail,
    GetChannels,
    GetIntegrations,
)
from zmp_zcp_toolkit.wrapper.base_wrapper import BaseAPIWrapper

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


_ALERT_ROOT_PATH = "/api/alert/v1"
_MONITORING_ROOT_PATH = "/api/monitoring/v1"


class ZcpAnalysisAPIWrapper(BaseAPIWrapper):
    """Wrapper for ZCP Analysis API."""

    async def get_alerts(self, query: GetAlerts) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/alerts"
        params = query.model_dump(exclude_none=True)
        response = await self.async_client.get(api_path, params=params)
        return response.json()

    async def get_priorities(self) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/alert/priorities"
        response = await self.async_client.get(api_path)
        return response.json()

    async def get_severities(self) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/alert/severities"
        response = await self.async_client.get(api_path)
        return response.json()

    async def get_alert_detail(self, query: GetAlertDetail) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/alerts/{query.alert_id}"
        response = await self.async_client.get(api_path)
        return response.json()

    async def get_channels(self, query: GetChannels) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/channels"
        params = query.model_dump(exclude_none=True)
        response = await self.async_client.get(api_path, params=params)
        return response.json()

    async def get_integrations(self, query: GetIntegrations) -> List[dict]:
        api_path = f"{_ALERT_ROOT_PATH}/integrations"
        params = query.model_dump(exclude_none=True)
        response = await self.async_client.get(api_path, params=params)
        return response.json()

    def run(self, mode: str, query: str) -> str:
        if mode == "get_alerts":
            result = asyncio.run(self.get_alerts(query))
            return json.dumps(result)
        elif mode == "get_priorities":
            result = asyncio.run(self.get_priorities())
            return json.dumps(result)
        elif mode == "get_severities":
            result = asyncio.run(self.get_severities())
            return json.dumps(result)
        elif mode == "get_alert_detail":
            result = asyncio.run(self.get_alert_detail(query))
            return json.dumps(result)
        elif mode == "get_channels":
            result = asyncio.run(self.get_channels(query))
            return json.dumps(result)
        elif mode == "get_integrations":
            result = asyncio.run(self.get_integrations(query))
            return json.dumps(result)
        else:
            raise ValueError("Invalid mode" + mode)


class ZcpReportAPIWrapper(BaseAPIWrapper): ...
