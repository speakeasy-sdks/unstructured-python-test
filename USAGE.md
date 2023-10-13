<!-- Start SDK Example Usage -->


```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()


res = s.pipeline_v0.build(pipeline_body_v0=shared.PipelineBodyV0(
    coordinates=[
        'Practical',
    ],
    encoding=[
        'Gasoline',
    ],
    files=[
        '[eAhpDJhn\''.encode(),
    ],
    hi_res_model_name=[
        'henry',
    ],
    ocr_languages=[
        'Meitnerium',
    ],
    pdf_infer_table_structure=[
        'Convertible',
    ],
    strategy=[
        'Direct',
    ],
    xml_keep_tags=[
        'gee',
    ],
), unstructured_api_key='Metal')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->