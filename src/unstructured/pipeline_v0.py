"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from unstructured import utils
from unstructured.models import errors, operations, shared

class PipelineV0:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def build(self, pipeline_body_v0: Optional[shared.PipelineBodyV0] = None, unstructured_api_key: Optional[str] = None) -> operations.Pipeline1GeneralV0GeneralPostResponse:
        r"""Pipeline 1"""
        request = operations.Pipeline1GeneralV0GeneralPostRequest(
            pipeline_body_v0=pipeline_body_v0,
            unstructured_api_key=unstructured_api_key,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/general/v0/general'
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, operations.Pipeline1GeneralV0GeneralPostRequest, "pipeline_body_v0", False, True, 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.Pipeline1GeneralV0GeneralPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    