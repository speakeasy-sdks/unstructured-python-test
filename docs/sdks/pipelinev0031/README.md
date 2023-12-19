# PipelineV0031
(*pipeline_v0_0_31*)

### Available Operations

* [build](#build) - Pipeline 1

## build

Pipeline 1

### Example Usage

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `pipeline_body_v0_0_31`                                                        | [Optional[shared.PipelineBodyV0031]](../../models/shared/pipelinebodyv0031.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `unstructured_api_key`                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.Pipeline1GeneralV0031GeneralPostResponse](../../models/operations/pipeline1generalv0031generalpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
