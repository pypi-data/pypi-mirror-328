"""向量脉络 API 客户端"""

import time
import base64
import asyncio
from urllib.parse import quote
from typing import List, Optional, Dict, Any, Union, Literal, overload

import httpx
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from .exceptions import (
    VectorVeinAPIError,
    APIKeyError,
    WorkflowError,
    AccessKeyError,
    RequestError,
    TimeoutError,
)
from .models import (
    AccessKey,
    WorkflowInputField,
    WorkflowOutput,
    WorkflowRunResult,
    AccessKeyListResponse,
)


class VectorVeinClient:
    """向量脉络 API 客户端类"""

    API_VERSION = "20240508"
    BASE_URL = "https://vectorvein.com/api/v1/open-api"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """初始化客户端

        Args:
            api_key: API密钥
            base_url: API基础URL，默认为https://vectorvein.com/api/v1/open-api

        Raises:
            APIKeyError: API密钥为空或格式不正确
        """
        if not api_key or not isinstance(api_key, str):
            raise APIKeyError("API密钥不能为空且必须是字符串类型")

        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self.default_headers = {
            "VECTORVEIN-API-KEY": api_key,
            "VECTORVEIN-API-VERSION": self.API_VERSION,
        }
        self._client = httpx.Client(timeout=60)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        **kwargs,
    ) -> Dict[str, Any]:
        """发送HTTP请求

        Args:
            method: HTTP方法
            endpoint: API端点
            params: URL参数
            json: JSON请求体
            **kwargs: 其他请求参数

        Returns:
            Dict[str, Any]: API响应

        Raises:
            RequestError: 请求错误
            VectorVeinAPIError: API错误
            APIKeyError: API密钥无效或已过期
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self.default_headers.copy()
        if api_key_type == "VAPP":
            headers["VECTORVEIN-API-KEY-TYPE"] = "VAPP"
        try:
            response = self._client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
                **kwargs,
            )
            result = response.json()

            if result["status"] in [401, 403]:
                raise APIKeyError("API密钥无效或已过期")
            if result["status"] != 200 and result["status"] != 202:
                raise VectorVeinAPIError(message=result.get("msg", "Unknown error"), status_code=result["status"])
            return result
        except httpx.HTTPError as e:
            raise RequestError(f"Request failed: {str(e)}")

    @overload
    def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: Literal[False] = False,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> str: ...

    @overload
    def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: Literal[True] = True,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> WorkflowRunResult: ...

    def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: bool = False,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> Union[str, WorkflowRunResult]:
        """运行工作流

        Args:
            wid: 工作流ID
            input_fields: 输入字段列表
            output_scope: 输出范围，可选值：'all' 或 'output_fields_only'
            wait_for_completion: 是否等待完成
            api_key_type: 密钥类型，可选值：'WORKFLOW' 或 'VAPP'
            timeout: 超时时间（秒）

        Returns:
            Union[str, WorkflowRunResult]: 工作流运行ID或运行结果

        Raises:
            WorkflowError: 工作流运行错误
            TimeoutError: 超时错误
        """
        payload = {
            "wid": wid,
            "output_scope": output_scope,
            "wait_for_completion": wait_for_completion,
            "input_fields": [
                {"node_id": field.node_id, "field_name": field.field_name, "value": field.value}
                for field in input_fields
            ],
        }

        result = self._request("POST", "workflow/run", json=payload, api_key_type=api_key_type)

        if not wait_for_completion:
            return result["data"]["rid"]

        rid = result.get("rid") or (isinstance(result["data"], dict) and result["data"].get("rid")) or ""
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Workflow execution timed out after {timeout} seconds")

            if api_key_type == "WORKFLOW":
                result = self.check_workflow_status(rid, api_key_type=api_key_type)
            else:
                result = self.check_workflow_status(rid, wid=wid, api_key_type=api_key_type)
            if result.status == 200:
                return result
            elif result.status == 500:
                raise WorkflowError(f"Workflow execution failed: {result.msg}")

            time.sleep(5)

    @overload
    def check_workflow_status(
        self, rid: str, wid: Optional[str] = None, api_key_type: Literal["WORKFLOW"] = "WORKFLOW"
    ) -> WorkflowRunResult: ...

    @overload
    def check_workflow_status(
        self, rid: str, wid: str, api_key_type: Literal["VAPP"] = "VAPP"
    ) -> WorkflowRunResult: ...

    def check_workflow_status(
        self, rid: str, wid: Optional[str] = None, api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW"
    ) -> WorkflowRunResult:
        """检查工作流运行状态

        Args:
            rid: 工作流运行记录ID
            wid: 工作流ID，非必填，api_key_type 为 'VAPP' 时必填
            api_key_type: 密钥类型，可选值：'WORKFLOW' 或 'VAPP'

        Returns:
            WorkflowRunResult: 工作流运行结果

        Raises:
            VectorVeinAPIError: 工作流错误
        """
        payload = {"rid": rid}
        if api_key_type == "VAPP" and not wid:
            raise VectorVeinAPIError("api_key_type 为 'VAPP' 时工作流 ID 不能为空")
        if wid:
            payload["wid"] = wid
        response = self._request("POST", "workflow/check-status", json=payload, api_key_type=api_key_type)
        if response["status"] in [200, 202]:
            return WorkflowRunResult(
                rid=rid,
                status=response["status"],
                msg=response["msg"],
                data=[WorkflowOutput(**output) for output in response["data"]],
            )
        else:
            raise WorkflowError(f"Workflow execution failed: {response['msg']}")

    def get_access_keys(
        self, access_keys: Optional[List[str]] = None, get_type: Literal["selected", "all"] = "selected"
    ) -> List[AccessKey]:
        """获取访问密钥信息

        Args:
            access_keys: 访问密钥列表
            get_type: 获取类型，可选值：'selected' 或 'all'

        Returns:
            List[AccessKey]: 访问密钥信息列表

        Raises:
            AccessKeyError: 访问密钥不存在或已失效
        """
        params = {"get_type": get_type}
        if access_keys:
            params["access_keys"] = ",".join(access_keys)

        try:
            result = self._request("GET", "vapp/access-key/get", params=params)
            return [AccessKey(**key) for key in result["data"]]
        except VectorVeinAPIError as e:
            if e.status_code == 404:
                raise AccessKeyError("访问密钥不存在")
            elif e.status_code == 403:
                raise AccessKeyError("访问密钥已失效")
            raise

    def create_access_keys(
        self,
        access_key_type: Literal["O", "M", "L"],
        app_id: Optional[str] = None,
        app_ids: Optional[List[str]] = None,
        count: int = 1,
        expire_time: Optional[str] = None,
        max_credits: Optional[int] = None,
        max_use_count: Optional[int] = None,
        description: Optional[str] = None,
    ) -> List[AccessKey]:
        """创建访问密钥

        Args:
            access_key_type: 密钥类型，可选值：'O'(一次性)、'M'(多次)、'L'(长期)
            app_id: 单个应用ID
            app_ids: 多个应用ID列表
            count: 创建数量
            expire_time: 过期时间
            max_credits: 最大积分限制
            max_use_count: 最大使用次数
            description: 描述信息

        Returns:
            List[AccessKey]: 创建的访问密钥列表

        Raises:
            AccessKeyError: 创建访问密钥失败，如类型无效、应用不存在等
        """
        if access_key_type not in ["O", "M", "L"]:
            raise AccessKeyError("无效的访问密钥类型，必须是 'O'(一次性)、'M'(多次) 或 'L'(长期)")

        if app_id and app_ids:
            raise AccessKeyError("不能同时指定 app_id 和 app_ids")

        payload = {"access_key_type": access_key_type, "count": count}

        if app_id:
            payload["app_id"] = app_id
        if app_ids:
            payload["app_ids"] = app_ids
        if expire_time:
            payload["expire_time"] = expire_time
        if max_credits is not None:
            payload["max_credits"] = max_credits
        if max_use_count is not None:
            payload["max_use_count"] = max_use_count
        if description:
            payload["description"] = description

        try:
            result = self._request("POST", "vapp/access-key/create", json=payload)
            return [AccessKey(**key) for key in result["data"]]
        except VectorVeinAPIError as e:
            if e.status_code == 404:
                raise AccessKeyError("指定的应用不存在")
            elif e.status_code == 403:
                raise AccessKeyError("没有权限创建访问密钥")
            raise

    def list_access_keys(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_field: str = "create_time",
        sort_order: str = "descend",
        app_id: Optional[str] = None,
        status: Optional[List[str]] = None,
        access_key_type: Optional[Literal["O", "M", "L"]] = None,
    ) -> AccessKeyListResponse:
        """列出访问密钥

        Args:
            page: 页码
            page_size: 每页数量
            sort_field: 排序字段
            sort_order: 排序顺序
            app_id: 应用ID
            status: 状态列表
            access_key_type: 密钥类型列表，可选值：'O'(一次性)、'M'(多次)、'L'(长期)

        Returns:
            AccessKeyListResponse: 访问密钥列表响应
        """
        payload = {"page": page, "page_size": page_size, "sort_field": sort_field, "sort_order": sort_order}

        if app_id:
            payload["app_id"] = app_id
        if status:
            payload["status"] = status
        if access_key_type:
            payload["access_key_type"] = access_key_type

        result = self._request("POST", "vapp/access-key/list", json=payload)
        return AccessKeyListResponse(**result["data"])

    def delete_access_keys(self, app_id: str, access_keys: List[str]) -> None:
        """删除访问密钥

        Args:
            app_id: 应用ID
            access_keys: 要删除的访问密钥列表
        """
        payload = {"app_id": app_id, "access_keys": access_keys}
        self._request("POST", "vapp/access-key/delete", json=payload)

    def update_access_keys(
        self,
        access_key: Optional[str] = None,
        access_keys: Optional[List[str]] = None,
        app_id: Optional[str] = None,
        app_ids: Optional[List[str]] = None,
        expire_time: Optional[str] = None,
        max_use_count: Optional[int] = None,
        max_credits: Optional[int] = None,
        description: Optional[str] = None,
        access_key_type: Optional[Literal["O", "M", "L"]] = None,
    ) -> None:
        """更新访问密钥

        Args:
            access_key: 单个访问密钥
            access_keys: 多个访问密钥列表
            app_id: 单个应用ID
            app_ids: 多个应用ID列表
            expire_time: 过期时间
            max_use_count: 最大使用次数
            max_credits: 最大积分限制
            description: 描述信息
            access_key_type: 密钥类型，可选值：'O'(一次性)、'M'(多次)、'L'(长期)
        """
        payload = {}
        if access_key:
            payload["access_key"] = access_key
        if access_keys:
            payload["access_keys"] = access_keys
        if app_id:
            payload["app_id"] = app_id
        if app_ids:
            payload["app_ids"] = app_ids
        if expire_time:
            payload["expire_time"] = expire_time
        if max_use_count is not None:
            payload["max_use_count"] = max_use_count
        if max_credits is not None:
            payload["max_credits"] = max_credits
        if description:
            payload["description"] = description
        if access_key_type:
            payload["access_key_type"] = access_key_type

        self._request("POST", "vapp/access-key/update", json=payload)

    def add_apps_to_access_keys(self, access_keys: List[str], app_ids: List[str]) -> None:
        """向访问密钥添加应用

        Args:
            access_keys: 访问密钥列表
            app_ids: 要添加的应用ID列表
        """
        payload = {"access_keys": access_keys, "app_ids": app_ids}
        self._request("POST", "vapp/access-key/add-apps", json=payload)

    def remove_apps_from_access_keys(self, access_keys: List[str], app_ids: List[str]) -> None:
        """从访问密钥移除应用

        Args:
            access_keys: 访问密钥列表
            app_ids: 要移除的应用ID列表
        """
        payload = {"access_keys": access_keys, "app_ids": app_ids}
        self._request("POST", "vapp/access-key/remove-apps", json=payload)

    def generate_vapp_url(
        self,
        app_id: str,
        access_key: str,
        key_id: str,
        timeout: int = 15 * 60,
        base_url: str = "https://vectorvein.com",
    ) -> str:
        """生成VApp访问链接

        Args:
            app_id: VApp ID
            access_key: 访问密钥
            key_id: 密钥ID
            timeout: 超时时间（秒）
            base_url: 基础URL

        Returns:
            str: VApp访问链接
        """
        timestamp = int(time.time())
        message = f"{app_id}:{access_key}:{timestamp}:{timeout}"
        encryption_key = self.api_key.encode()

        cipher = AES.new(encryption_key, AES.MODE_CBC)
        padded_data = pad(message.encode(), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        final_data = bytes(cipher.iv) + encrypted_data
        token = base64.b64encode(final_data).decode("utf-8")
        quoted_token = quote(token)

        return f"{base_url}/public/v-app/{app_id}?token={quoted_token}&key_id={key_id}"


class AsyncVectorVeinClient:
    """向量脉络 API 异步客户端类"""

    API_VERSION = "20240508"
    BASE_URL = "https://vectorvein.com/api/v1/open-api"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """初始化异步客户端

        Args:
            api_key: API密钥
            base_url: API基础URL，默认为https://vectorvein.com/api/v1/open-api

        Raises:
            APIKeyError: API密钥为空或格式不正确
        """
        if not api_key or not isinstance(api_key, str):
            raise APIKeyError("API密钥不能为空且必须是字符串类型")

        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self.default_headers = {
            "VECTORVEIN-API-KEY": api_key,
            "VECTORVEIN-API-VERSION": self.API_VERSION,
        }
        self._client = httpx.AsyncClient(timeout=60)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.aclose()

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        **kwargs,
    ) -> Dict[str, Any]:
        """发送异步HTTP请求

        Args:
            method: HTTP方法
            endpoint: API端点
            params: URL参数
            json: JSON请求体
            **kwargs: 其他请求参数

        Returns:
            Dict[str, Any]: API响应

        Raises:
            RequestError: 请求错误
            VectorVeinAPIError: API错误
            APIKeyError: API密钥无效或已过期
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self.default_headers.copy()
        if api_key_type == "VAPP":
            headers["VECTORVEIN-API-KEY-TYPE"] = "VAPP"
        try:
            response = await self._client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
                **kwargs,
            )
            result = response.json()

            if result["status"] in [401, 403]:
                raise APIKeyError("API密钥无效或已过期")
            if result["status"] != 200 and result["status"] != 202:
                raise VectorVeinAPIError(message=result.get("msg", "Unknown error"), status_code=result["status"])
            return result
        except httpx.HTTPError as e:
            raise RequestError(f"Request failed: {str(e)}")

    @overload
    async def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: Literal[False] = False,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> str: ...

    @overload
    async def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: Literal[True] = True,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> WorkflowRunResult: ...

    async def run_workflow(
        self,
        wid: str,
        input_fields: List[WorkflowInputField],
        output_scope: Literal["all", "output_fields_only"] = "output_fields_only",
        wait_for_completion: bool = False,
        api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW",
        timeout: int = 30,
    ) -> Union[str, WorkflowRunResult]:
        """异步运行工作流

        Args:
            wid: 工作流ID
            input_fields: 输入字段列表
            output_scope: 输出范围，可选值：'all' 或 'output_fields_only'
            wait_for_completion: 是否等待完成
            api_key_type: 密钥类型，可选值：'WORKFLOW' 或 'VAPP'
            timeout: 超时时间（秒）

        Returns:
            Union[str, WorkflowRunResult]: 工作流运行ID或运行结果

        Raises:
            WorkflowError: 工作流运行错误
            TimeoutError: 超时错误
        """
        payload = {
            "wid": wid,
            "output_scope": output_scope,
            "wait_for_completion": wait_for_completion,
            "input_fields": [
                {"node_id": field.node_id, "field_name": field.field_name, "value": field.value}
                for field in input_fields
            ],
        }

        result = await self._request("POST", "workflow/run", json=payload, api_key_type=api_key_type)

        if not wait_for_completion:
            return result["data"]["rid"]

        rid = result.get("rid") or (isinstance(result["data"], dict) and result["data"].get("rid")) or ""
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Workflow execution timed out after {timeout} seconds")

            if api_key_type == "WORKFLOW":
                result = await self.check_workflow_status(rid, api_key_type=api_key_type)
            else:
                result = await self.check_workflow_status(rid, wid=wid, api_key_type=api_key_type)
            if result.status == 200:
                return result
            elif result.status == 500:
                raise WorkflowError(f"Workflow execution failed: {result.msg}")

            await asyncio.sleep(5)

    @overload
    async def check_workflow_status(
        self, rid: str, wid: Optional[str] = None, api_key_type: Literal["WORKFLOW"] = "WORKFLOW"
    ) -> WorkflowRunResult: ...

    @overload
    async def check_workflow_status(
        self, rid: str, wid: str, api_key_type: Literal["VAPP"] = "VAPP"
    ) -> WorkflowRunResult: ...

    async def check_workflow_status(
        self, rid: str, wid: Optional[str] = None, api_key_type: Literal["WORKFLOW", "VAPP"] = "WORKFLOW"
    ) -> WorkflowRunResult:
        """异步检查工作流运行状态

        Args:
            rid: 工作流运行记录ID
            wid: 工作流ID，非必填，api_key_type 为 'VAPP' 时必填
            api_key_type: 密钥类型，可选值：'WORKFLOW' 或 'VAPP'

        Raises:
            VectorVeinAPIError: 工作流错误
        """
        payload = {"rid": rid}
        if api_key_type == "VAPP" and not wid:
            raise VectorVeinAPIError("api_key_type 为 'VAPP' 时工作流 ID 不能为空")
        if wid:
            payload["wid"] = wid
        response = await self._request("POST", "workflow/check-status", json=payload, api_key_type=api_key_type)
        if response["status"] in [200, 202]:
            return WorkflowRunResult(
                rid=rid,
                status=response["status"],
                msg=response["msg"],
                data=[WorkflowOutput(**output) for output in response["data"]],
            )
        else:
            raise WorkflowError(f"Workflow execution failed: {response['msg']}")

    async def get_access_keys(
        self, access_keys: Optional[List[str]] = None, get_type: Literal["selected", "all"] = "selected"
    ) -> List[AccessKey]:
        """异步获取访问密钥信息

        Args:
            access_keys: 访问密钥列表
            get_type: 获取类型，可选值：'selected' 或 'all'

        Returns:
            List[AccessKey]: 访问密钥信息列表

        Raises:
            AccessKeyError: 访问密钥不存在或已失效
        """
        params = {"get_type": get_type}
        if access_keys:
            params["access_keys"] = ",".join(access_keys)

        try:
            result = await self._request("GET", "vapp/access-key/get", params=params)
            return [AccessKey(**key) for key in result["data"]]
        except VectorVeinAPIError as e:
            if e.status_code == 404:
                raise AccessKeyError("访问密钥不存在")
            elif e.status_code == 403:
                raise AccessKeyError("访问密钥已失效")
            raise

    async def create_access_keys(
        self,
        access_key_type: Literal["O", "M", "L"],
        app_id: Optional[str] = None,
        app_ids: Optional[List[str]] = None,
        count: int = 1,
        expire_time: Optional[str] = None,
        max_credits: Optional[int] = None,
        max_use_count: Optional[int] = None,
        description: Optional[str] = None,
    ) -> List[AccessKey]:
        """异步创建访问密钥

        Args:
            access_key_type: 密钥类型，可选值：'O'(一次性)、'M'(多次)、'L'(长期)
            app_id: 单个应用ID
            app_ids: 多个应用ID列表
            count: 创建数量
            expire_time: 过期时间
            max_credits: 最大积分限制
            max_use_count: 最大使用次数
            description: 描述信息

        Returns:
            List[AccessKey]: 创建的访问密钥列表

        Raises:
            AccessKeyError: 创建访问密钥失败，如类型无效、应用不存在等
        """
        if access_key_type not in ["O", "M", "L"]:
            raise AccessKeyError("无效的访问密钥类型，必须是 'O'(一次性)、'M'(多次) 或 'L'(长期)")

        if app_id and app_ids:
            raise AccessKeyError("不能同时指定 app_id 和 app_ids")

        payload = {"access_key_type": access_key_type, "count": count}

        if app_id:
            payload["app_id"] = app_id
        if app_ids:
            payload["app_ids"] = app_ids
        if expire_time:
            payload["expire_time"] = expire_time
        if max_credits is not None:
            payload["max_credits"] = max_credits
        if max_use_count is not None:
            payload["max_use_count"] = max_use_count
        if description:
            payload["description"] = description

        try:
            result = await self._request("POST", "vapp/access-key/create", json=payload)
            return [AccessKey(**key) for key in result["data"]]
        except VectorVeinAPIError as e:
            if e.status_code == 404:
                raise AccessKeyError("指定的应用不存在")
            elif e.status_code == 403:
                raise AccessKeyError("没有权限创建访问密钥")
            raise

    async def list_access_keys(
        self,
        page: int = 1,
        page_size: int = 10,
        sort_field: str = "create_time",
        sort_order: str = "descend",
        app_id: Optional[str] = None,
        status: Optional[List[str]] = None,
        access_key_type: Optional[Literal["O", "M", "L"]] = None,
    ) -> AccessKeyListResponse:
        """异步列出访问密钥

        Args:
            page: 页码
            page_size: 每页数量
            sort_field: 排序字段
            sort_order: 排序顺序
            app_id: 应用ID
            status: 状态列表
            access_key_type: 密钥类型列表，可选值：'O'(一次性)、'M'(多次)、'L'(长期)

        Returns:
            AccessKeyListResponse: 访问密钥列表响应
        """
        payload = {"page": page, "page_size": page_size, "sort_field": sort_field, "sort_order": sort_order}

        if app_id:
            payload["app_id"] = app_id
        if status:
            payload["status"] = status
        if access_key_type:
            payload["access_key_type"] = access_key_type

        result = await self._request("POST", "vapp/access-key/list", json=payload)
        return AccessKeyListResponse(**result["data"])

    async def delete_access_keys(self, app_id: str, access_keys: List[str]) -> None:
        """异步删除访问密钥

        Args:
            app_id: 应用ID
            access_keys: 要删除的访问密钥列表
        """
        payload = {"app_id": app_id, "access_keys": access_keys}
        await self._request("POST", "vapp/access-key/delete", json=payload)

    async def update_access_keys(
        self,
        access_key: Optional[str] = None,
        access_keys: Optional[List[str]] = None,
        app_id: Optional[str] = None,
        app_ids: Optional[List[str]] = None,
        expire_time: Optional[str] = None,
        max_use_count: Optional[int] = None,
        max_credits: Optional[int] = None,
        description: Optional[str] = None,
        access_key_type: Optional[Literal["O", "M", "L"]] = None,
    ) -> None:
        """异步更新访问密钥

        Args:
            access_key: 单个访问密钥
            access_keys: 多个访问密钥列表
            app_id: 单个应用ID
            app_ids: 多个应用ID列表
            expire_time: 过期时间
            max_use_count: 最大使用次数
            max_credits: 最大积分限制
            description: 描述信息
            access_key_type: 密钥类型，可选值：'O'(一次性)、'M'(多次)、'L'(长期)
        """
        payload = {}
        if access_key:
            payload["access_key"] = access_key
        if access_keys:
            payload["access_keys"] = access_keys
        if app_id:
            payload["app_id"] = app_id
        if app_ids:
            payload["app_ids"] = app_ids
        if expire_time:
            payload["expire_time"] = expire_time
        if max_use_count is not None:
            payload["max_use_count"] = max_use_count
        if max_credits is not None:
            payload["max_credits"] = max_credits
        if description:
            payload["description"] = description
        if access_key_type:
            payload["access_key_type"] = access_key_type

        await self._request("POST", "vapp/access-key/update", json=payload)

    async def add_apps_to_access_keys(self, access_keys: List[str], app_ids: List[str]) -> None:
        """异步向访问密钥添加应用

        Args:
            access_keys: 访问密钥列表
            app_ids: 要添加的应用ID列表
        """
        payload = {"access_keys": access_keys, "app_ids": app_ids}
        await self._request("POST", "vapp/access-key/add-apps", json=payload)

    async def remove_apps_from_access_keys(self, access_keys: List[str], app_ids: List[str]) -> None:
        """异步从访问密钥移除应用

        Args:
            access_keys: 访问密钥列表
            app_ids: 要移除的应用ID列表
        """
        payload = {"access_keys": access_keys, "app_ids": app_ids}
        await self._request("POST", "vapp/access-key/remove-apps", json=payload)

    async def generate_vapp_url(
        self,
        app_id: str,
        access_key: str,
        key_id: str,
        timeout: int = 15 * 60,
        base_url: str = "https://vectorvein.com",
    ) -> str:
        """异步生成VApp访问链接

        Args:
            app_id: VApp ID
            access_key: 访问密钥
            key_id: 密钥ID
            timeout: 超时时间（秒）
            base_url: 基础URL

        Returns:
            str: VApp访问链接
        """
        timestamp = int(time.time())
        message = f"{app_id}:{access_key}:{timestamp}:{timeout}"
        encryption_key = self.api_key.encode()

        cipher = AES.new(encryption_key, AES.MODE_CBC)
        padded_data = pad(message.encode(), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        final_data = bytes(cipher.iv) + encrypted_data
        token = base64.b64encode(final_data).decode("utf-8")
        quoted_token = quote(token)

        return f"{base_url}/public/v-app/{app_id}?token={quoted_token}&key_id={key_id}"
