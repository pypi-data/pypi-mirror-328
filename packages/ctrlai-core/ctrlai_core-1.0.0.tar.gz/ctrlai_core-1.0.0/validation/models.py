# ctrlai-core/validation/models.py
from pydantic import BaseModel, Field, HttpUrl, validator
from typing import List, Optional, Union
from datetime import datetime
from uuid import UUID

class CtrlAIGroupBase(BaseModel):
    name: str = Field(..., description="Name of the Ctrl AI group.")

class CtrlAIGroup(CtrlAIGroupBase):
    id: UUID = Field(..., description="Unique identifier for the Ctrl AI group.")
    user_id: UUID = Field(..., description="Identifier of the user who owns the group.")
    created_at: datetime = Field(..., description="Timestamp of group creation.")
    updated_at: datetime = Field(..., description="Timestamp of last group update.")

    class Config:
        orm_mode = True # This is only really needed if you're using an ORM (like SQLAlchemy)


class CtrlAIBase(BaseModel):
    type: str = Field(..., description="Type of Ctrl AI entry (e.g., 'preference:dietary', 'context:project').")
    value: Union[str, dict] = Field(..., description="The content of the Ctrl AI entry (text or structured data as JSON).")
    source: str = Field(..., description="Source of the information (e.g., 'userInput', 'companyWiki').")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence level (0.0 to 1.0).")
    expires: Optional[datetime] = Field(None, description="Timestamp when the Ctrl AI expires (optional).")
    valid_from: Optional[datetime] = Field(None, description="Timestamp when the Ctrl AI becomes valid (optional).")
    scope: str = Field(..., description="Scope of the information (e.g., 'personal', 'project:ProjectX').")
    keywords: List[str] = Field([], description="User-defined keywords.")
    related_entities: List[HttpUrl] = Field([], description="Links to other entities (optional - URIs).")


class CtrlAI(CtrlAIBase):
    id: UUID = Field(..., description="Unique identifier for the Ctrl AI (UUID).")
    user_id: UUID = Field(..., description="Identifier of the user who owns the Ctrl AI.")
    ctrlai_group_id: UUID = Field(..., description="Identifier of the Ctrl AI group.")
    dateCreated: datetime = Field(..., description="Timestamp of creation.")
    dateModified: datetime = Field(..., description="Timestamp of last modification.")
    embedding: List[float] = Field(..., description="Vector embedding of the value field.")

    class Config:
        orm_mode = True

    @validator('type')
    def validate_type(cls, v):
        valid_types = [
            # Preferences
            'preference:dietary',
            'preference:communication_style',
            'preference:writing_style',
            'preference:personality',
            'preference:personal_interest',
            
            # Context
            'context:project',
            'context:location',
            'context:time_sensitive',
            'context:goal',
            
            # Knowledge
            'knowledge:company_fact',
            'knowledge:product_spec',
            'knowledge:competitor_info',
            'knowledge:personal_fact',
            'knowledge:calendar',
            'knowledge:skills',
            'knowledge:external'
        ]
        if v not in valid_types:
            raise ValueError(f'Invalid type: {v}. Must be one of: {", ".join(valid_types)}')
        return v

    @validator('scope')
    def validate_scope(cls, v):
        valid_scopes = ['personal', 'project:', 'department:', 'company']
        if not any(v.startswith(scope) for scope in valid_scopes):
            raise ValueError(f'Invalid scope: {v}')
        return v

# Add config class with version info
class Config:
    VERSION = "1.0.0"
    SCHEMA_VERSION = "1.0"
    API_VERSION = "v1"  