from contextvars import ContextVar
from typing import Dict, Any
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.constant.constant import ENV_PREFIX

# Context variable for storing dynamic state
_ctx_var: ContextVar[Dict[Any, Any]] = ContextVar("ctx_var", default={})



class _db_settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix=ENV_PREFIX,  # Match prefix with your .env file #development_
        env_file='.env',
        populate_by_name=True,  # Use field aliases
        extra='ignore',  # Ignore extra inputs from the .env file
        env_file_encoding='utf-8',
    )

    # Match these aliases to .env field keys
    db_host:str = Field(alias='database_host')
    db_username: str = Field(alias='database_username')
    db_password: str = Field(alias='database_password')
    db_name:str = Field(alias='database_name')
    db_port:str = Field(alias='database_port')
    # db_schema: str = Field(alias='DATABASE_SCHEMA')
