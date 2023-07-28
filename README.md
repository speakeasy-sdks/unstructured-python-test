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

req = operations.Pipeline1GeneralV0GeneralPostRequest(
    pipeline_body_v0=shared.PipelineBodyV0(
        coordinates=[
            'provident',
            'distinctio',
            'quibusdam',
        ],
        encoding=[
            'nulla',
            'corrupti',
            'illum',
        ],
        files=[
            'error'.encode(),
            'deserunt'.encode(),
        ],
        gz_uncompressed_content_type='suscipit',
        hi_res_model_name=[
            'magnam',
            'debitis',
        ],
        ocr_languages=[
            'delectus',
        ],
        output_format='tempora',
        pdf_infer_table_structure=[
            'molestiae',
            'minus',
        ],
        strategy=[
            'voluptatum',
            'iusto',
            'excepturi',
            'nisi',
        ],
        xml_keep_tags=[
            'temporibus',
            'ab',
            'quis',
            'veritatis',
        ],
    ),
    unstructured_api_key='deserunt',
)

res = s.pipeline_v0.build(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [pipeline_v0](docs/sdks/pipelinev0/README.md)

* [build](docs/sdks/pipelinev0/README.md#build) - Pipeline 1

### [pipeline_v0_0_31](docs/sdks/pipelinev0031/README.md)

* [build](docs/sdks/pipelinev0031/README.md#build) - Pipeline 1
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
