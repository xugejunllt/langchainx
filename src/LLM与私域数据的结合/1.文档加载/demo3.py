from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError

s = UnstructuredClient(api_key_auth="YOUR_API_KEY")

filename = "pdf_loader_demo.pdf"

with open(filename, "rb") as f:
    # Note that this currently only supports a single file
    files = shared.Files(
        content=f.read(),
        file_name=filename,
    )

req = shared.PartitionParameters(
    files=files,
    # Other partition params
    strategy='ocr_only',
    languages=["eng"],
)

try:
    resp = s.general.partition(req)
    print(resp.elements[0])
except SDKError as e:
    print(e)
