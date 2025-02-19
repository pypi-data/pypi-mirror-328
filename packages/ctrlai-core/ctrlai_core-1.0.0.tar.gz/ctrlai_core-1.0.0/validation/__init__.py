"""
CtrlAI Core Validation Package

This package provides validation tools for the CtrlAI protocol,
ensuring data conformity with the schema and vocabulary.
"""

from .models import CtrlAI, CtrlAIGroup, CtrlAIBase
from .validate import (
    validate_ctrlai_json,
    validate_ctrlai_pydantic,
    validate_ctrlai_embedding,
    validate_ctrlai_group,
)

__version__ = "1.0.0"
__author__ = "CtrlAI Team"
__license__ = "MIT"

__all__ = [
    "CtrlAI",
    "CtrlAIGroup",
    "CtrlAIBase",
    "validate_ctrlai_json",
    "validate_ctrlai_pydantic",
    "validate_ctrlai_embedding",
    "validate_ctrlai_group",
]