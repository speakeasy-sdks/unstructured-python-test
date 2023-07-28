# pipeline_v0_0_31

### Available Operations

* [build](#build) - Pipeline 1

## build

Pipeline 1

### Example Usage

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()

req = operations.Pipeline1GeneralV0031GeneralPostRequest(
    pipeline_body_v0_0_31=shared.PipelineBodyV0031(
        coordinates=[
            'ad',
        ],
        encoding=[
            'sed',
            'iste',
            'dolor',
        ],
        files=[
            'laboriosam'.encode(),
            'hic'.encode(),
            'saepe'.encode(),
        ],
        gz_uncompressed_content_type='fuga',
        hi_res_model_name=[
            'corporis',
            'iste',
        ],
        ocr_languages=[
            'saepe',
            'quidem',
        ],
        output_format='architecto',
        pdf_infer_table_structure=[
            'reiciendis',
        ],
        strategy=[
            'mollitia',
            'laborum',
            'dolores',
        ],
        xml_keep_tags=[
            'corporis',
        ],
    ),
    unstructured_api_key='explicabo',
)

res = s.pipeline_v0_0_31.build(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.Pipeline1GeneralV0031GeneralPostRequest](../../models/operations/pipeline1generalv0031generalpostrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.Pipeline1GeneralV0031GeneralPostResponse](../../models/operations/pipeline1generalv0031generalpostresponse.md)**

