# pipeline_v0

### Available Operations

* [build](#build) - Pipeline 1

## build

Pipeline 1

### Example Usage

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()

req = operations.Pipeline1GeneralV0GeneralPostRequest(
    pipeline_body_v0=shared.PipelineBodyV0(
        coordinates=[
            'ipsam',
        ],
        encoding=[
            'sapiente',
            'quo',
            'odit',
            'at',
        ],
        files=[
            'maiores'.encode(),
            'molestiae'.encode(),
            'quod'.encode(),
            'quod'.encode(),
        ],
        gz_uncompressed_content_type='esse',
        hi_res_model_name=[
            'porro',
            'dolorum',
            'dicta',
        ],
        ocr_languages=[
            'officia',
            'occaecati',
            'fugit',
        ],
        output_format='deleniti',
        pdf_infer_table_structure=[
            'optio',
            'totam',
            'beatae',
            'commodi',
        ],
        strategy=[
            'modi',
            'qui',
        ],
        xml_keep_tags=[
            'cum',
            'esse',
            'ipsum',
            'excepturi',
        ],
    ),
    unstructured_api_key='aspernatur',
)

res = s.pipeline_v0.build(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.Pipeline1GeneralV0GeneralPostRequest](../../models/operations/pipeline1generalv0generalpostrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.Pipeline1GeneralV0GeneralPostResponse](../../models/operations/pipeline1generalv0generalpostresponse.md)**

