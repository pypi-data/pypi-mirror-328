from typing import Dict, Optional, Union, Any
from pydantic import BaseModel

class FiltersConfig(BaseModel):
    page: Optional[int] = None
    rows_per_page: Optional[int] = None
    sort: Optional[Dict[str, int]] = None
    filters: Optional[Dict[str, Any]] = None
    text: Optional[str] = None
    return_props: Optional[Dict[str, Union[int, float]]] = None
