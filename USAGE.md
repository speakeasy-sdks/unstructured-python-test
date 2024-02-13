<!-- Start SDK Example Usage [usage] -->
```python
import unstructured
from unstructured.models import shared

s = unstructured.Unstructured()


res = s.pipeline_v0_0_31.build(pipeline_body_v0_0_31=shared.PipelineBodyV0031(), unstructured_api_key='string')

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->