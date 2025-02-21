__version__ = "0.2.0"

# 暴露常用功能
from .math import add, multiply
from .web import get_json

__all__ = ['add', 'multiply', 'get_json']