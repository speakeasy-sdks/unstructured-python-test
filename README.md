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


res = s.pipeline_v0.build(pipeline_body_v0=shared.PipelineBodyV0(
    coordinates=[
        'corrupti',
    ],
    encoding=[
        'provident',
    ],
    files=[
        'distinctio'.encode(),
    ],
    gz_uncompressed_content_type='quibusdam',
    hi_res_model_name=[
        'unde',
    ],
    ocr_languages=[
        'nulla',
    ],
    output_format='corrupti',
    pdf_infer_table_structure=[
        'illum',
    ],
    strategy=[
        'vel',
    ],
    xml_keep_tags=[
        'error',
    ],
), unstructured_api_key='deserunt')

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
