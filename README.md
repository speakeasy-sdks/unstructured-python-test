# Petstore

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/unstructured-python-test.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()


res = s.pipeline_v0_0_31.build(pipeline_body_v0_0_31=shared.PipelineBodyV0031(
    coordinates=[
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.PipelineBodyV0031Files(
            content='0x591E0BfdA7'.encode(),
            file_name='cab_touring_henry.mpg4',
        ),
    ],
    hi_res_model_name=[
        'string',
    ],
    ocr_languages=[
        'string',
    ],
    pdf_infer_table_structure=[
        'string',
    ],
    strategy=[
        'string',
    ],
    xml_keep_tags=[
        'string',
    ],
), unstructured_api_key='string')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [pipeline_v0_0_31](docs/sdks/pipelinev0031/README.md)

* [build](docs/sdks/pipelinev0031/README.md#build) - Pipeline 1

### [pipeline_v0](docs/sdks/pipelinev0/README.md)

* [build](docs/sdks/pipelinev0/README.md#build) - Pipeline 1
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |


## Example

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()


res = None
try:
    res = s.pipeline_v0_0_31.build(pipeline_body_v0_0_31=shared.PipelineBodyV0031(
    coordinates=[
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.PipelineBodyV0031Files(
            content='0x591E0BfdA7'.encode(),
            file_name='cab_touring_henry.mpg4',
        ),
    ],
    hi_res_model_name=[
        'string',
    ],
    ocr_languages=[
        'string',
    ],
    pdf_infer_table_structure=[
        'string',
    ],
    strategy=[
        'string',
    ],
    xml_keep_tags=[
        'string',
    ],
), unstructured_api_key='string')
except (errors.HTTPValidationError) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.status_code == 200:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.unstructured.io` | None |

For example:

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured(
    server_idx=0,
)


res = s.pipeline_v0_0_31.build(pipeline_body_v0_0_31=shared.PipelineBodyV0031(
    coordinates=[
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.PipelineBodyV0031Files(
            content='0x591E0BfdA7'.encode(),
            file_name='cab_touring_henry.mpg4',
        ),
    ],
    hi_res_model_name=[
        'string',
    ],
    ocr_languages=[
        'string',
    ],
    pdf_infer_table_structure=[
        'string',
    ],
    strategy=[
        'string',
    ],
    xml_keep_tags=[
        'string',
    ],
), unstructured_api_key='string')

if res.status_code == 200:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured(
    server_url="https://api.unstructured.io",
)


res = s.pipeline_v0_0_31.build(pipeline_body_v0_0_31=shared.PipelineBodyV0031(
    coordinates=[
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.PipelineBodyV0031Files(
            content='0x591E0BfdA7'.encode(),
            file_name='cab_touring_henry.mpg4',
        ),
    ],
    hi_res_model_name=[
        'string',
    ],
    ocr_languages=[
        'string',
    ],
    pdf_infer_table_structure=[
        'string',
    ],
    strategy=[
        'string',
    ],
    xml_keep_tags=[
        'string',
    ],
), unstructured_api_key='string')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that this sdk makes as follows:

```python
import unstructured
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = unstructured.Unstructured(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
