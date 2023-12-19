# PipelineV0
(*pipeline_v0*)

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
        'string',
    ],
    encoding=[
        'string',
    ],
    files=[
        shared.Files(
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

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `pipeline_body_v0`                                                       | [Optional[shared.PipelineBodyV0]](../../models/shared/pipelinebodyv0.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `unstructured_api_key`                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | N/A                                                                      |


### Response

**[operations.Pipeline1GeneralV0GeneralPostResponse](../../models/operations/pipeline1generalv0generalpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
