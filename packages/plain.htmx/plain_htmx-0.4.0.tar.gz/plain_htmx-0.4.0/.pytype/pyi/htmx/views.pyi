# (generated with --quick)

import re
from typing import Annotated, Any

patch_vary_headers: Any

class HTMXViewMixin:
    htmx_action_name: Annotated[Any, 'property']
    htmx_fragment_name: Annotated[Any, 'property']
    htmx_template_name: str
    is_htmx_request: Annotated[Any, 'property']
    def get_request_handler(self) -> Any: ...
    def get_response(self) -> Any: ...
    def get_template_names(self) -> Any: ...
    def render_template(self) -> Any: ...

def render_template_fragment(*, template, fragment_name, context) -> Any: ...
