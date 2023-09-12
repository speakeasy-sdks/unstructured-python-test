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