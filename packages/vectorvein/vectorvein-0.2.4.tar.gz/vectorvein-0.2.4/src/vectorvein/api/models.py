"""向量脉络 API 数据模型定义"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any


@dataclass
class VApp:
    """VApp 信息"""

    app_id: str
    title: str
    description: str
    info: Dict[str, Any]
    images: List[str]


@dataclass
class AccessKey:
    """访问密钥信息"""

    access_key: str
    access_key_type: str  # O: 一次性, M: 多次, L: 长期
    use_count: int
    max_use_count: Optional[int]
    max_credits: Optional[int]
    used_credits: int
    v_app: Optional[VApp]
    v_apps: List[VApp]
    records: List[Any]
    status: str  # AC: 有效, IN: 无效, EX: 已过期, US: 已使用
    access_scope: str  # S: 单应用, M: 多应用
    description: str
    create_time: str
    expire_time: str
    last_use_time: Optional[str]


@dataclass
class WorkflowInputField:
    """工作流输入字段"""

    node_id: str
    field_name: str
    value: Any


@dataclass
class WorkflowOutput:
    """工作流输出结果"""

    type: str
    title: str
    value: Any


@dataclass
class WorkflowRunResult:
    """工作流运行结果"""

    rid: str
    status: int
    msg: str
    data: List[WorkflowOutput]


@dataclass
class AccessKeyListResponse:
    """访问密钥列表响应"""

    access_keys: List[AccessKey]
    total: int
    page_size: int
    page: int
