from pydantic import BaseModel


class ProcessedComponents(BaseModel):
    body: dict | list | str
    input_headers: dict
    headers: dict
    context: dict | list | str | None = None
    params: dict | None = None
