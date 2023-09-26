# PipelineV0

### Available Operations

* [build](#build) - Pipeline 1

## build

Pipeline 1

### Example Usage

```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()


res = s.pipeline_v0.build(pipeline_body_v0=shared.PipelineBodyV0(
    coordinates=[
        'voluptatum',
    ],
    encoding=[
        'iusto',
    ],
    files=[
        'excepturi'.encode(),
    ],
    gz_uncompressed_content_type='nisi',
    hi_res_model_name=[
        'recusandae',
    ],
    ocr_languages=[
        'temporibus',
    ],
    output_format='ab',
    pdf_infer_table_structure=[
        'quis',
    ],
    strategy=[
        'veritatis',
    ],
    xml_keep_tags=[
        'deserunt',
    ],
), unstructured_api_key='perferendis')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `pipeline_body_v0`                                                       | [Optional[shared.PipelineBodyV0]](../../models/shared/pipelinebodyv0.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `unstructured_api_key`                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |


### Response

**[operations.Pipeline1GeneralV0GeneralPostResponse](../../models/operations/pipeline1generalv0generalpostresponse.md)**

