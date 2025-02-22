"""向量脉络 API 异常类定义"""

from typing import Optional


class VectorVeinAPIError(Exception):
    """向量脉络 API 基础异常类"""

    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class APIKeyError(VectorVeinAPIError):
    """API密钥相关错误"""

    pass


class WorkflowError(VectorVeinAPIError):
    """工作流相关错误"""

    pass


class AccessKeyError(VectorVeinAPIError):
    """访问密钥相关错误"""

    pass


class RequestError(VectorVeinAPIError):
    """请求相关错误"""

    pass


class TimeoutError(VectorVeinAPIError):
    """超时错误"""

    pass
