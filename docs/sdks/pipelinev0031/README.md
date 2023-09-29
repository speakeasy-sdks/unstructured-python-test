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
        'Practical',
    ],
    encoding=[
        'Gasoline',
    ],
    files=[
        '[eAhpDJhn\''.encode(),
    ],
    gz_uncompressed_content_type='Shoes',
    hi_res_model_name=[
        'what',
    ],
    ocr_languages=[
        'whether',
    ],
    output_format='Direct',
    pdf_infer_table_structure=[
        'gee',
    ],
    strategy=[
        'Metal',
    ],
    xml_keep_tags=[
        'Avon',
    ],
), unstructured_api_key='questioningly')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `pipeline_body_v0_0_31`                                                        | [Optional[shared.PipelineBodyV0031]](../../models/shared/pipelinebodyv0031.md) | :heavy_minus_sign:                                                             | N/A                                                                            |
| `unstructured_api_key`                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.Pipeline1GeneralV0031GeneralPostResponse](../../models/operations/pipeline1generalv0031generalpostresponse.md)**

