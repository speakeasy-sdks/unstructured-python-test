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