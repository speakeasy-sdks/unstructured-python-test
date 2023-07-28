<!-- Start SDK Example Usage -->


```python
import unstructured
from unstructured.models import operations, shared

s = unstructured.Unstructured()

req = operations.Pipeline1GeneralV0GeneralPostRequest(
    pipeline_body_v0=shared.PipelineBodyV0(
        coordinates=[
            'provident',
            'distinctio',
            'quibusdam',
        ],
        encoding=[
            'nulla',
            'corrupti',
            'illum',
        ],
        files=[
            'error'.encode(),
            'deserunt'.encode(),
        ],
        gz_uncompressed_content_type='suscipit',
        hi_res_model_name=[
            'magnam',
            'debitis',
        ],
        ocr_languages=[
            'delectus',
        ],
        output_format='tempora',
        pdf_infer_table_structure=[
            'molestiae',
            'minus',
        ],
        strategy=[
            'voluptatum',
            'iusto',
            'excepturi',
            'nisi',
        ],
        xml_keep_tags=[
            'temporibus',
            'ab',
            'quis',
            'veritatis',
        ],
    ),
    unstructured_api_key='deserunt',
)

res = s.pipeline_v0.build(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->