"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import pipeline_body_v0 as shared_pipeline_body_v0
from typing import Optional


@dataclasses.dataclass
class Pipeline1GeneralV0GeneralPostRequest:
    pipeline_body_v0: Optional[shared_pipeline_body_v0.PipelineBodyV0] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    unstructured_api_key: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'unstructured-api-key', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class Pipeline1GeneralV0GeneralPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

