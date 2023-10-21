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
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.PipelineBodyV0Files(
            content='9G&x$kc[eA'.encode(),
            files='string',
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


### [pipeline_v0](docs/sdks/pipelinev0/README.md)

* [build](docs/sdks/pipelinev0/README.md#build) - Pipeline 1

### [pipeline_v0_0_31](docs/sdks/pipelinev0031/README.md)

* [build](docs/sdks/pipelinev0031/README.md#build) - Pipeline 1
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
