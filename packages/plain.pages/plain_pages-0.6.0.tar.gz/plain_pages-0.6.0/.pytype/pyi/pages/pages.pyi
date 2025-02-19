# (generated with --quick)

import frontmatter
import os
from typing import Annotated, Any

Template: Any
cached_property: Any
render_markdown: Any

class Page:
    _frontmatter: Any
    absolute_path: Any
    content: Any
    content_type: Annotated[Any, 'property']
    relative_path: Any
    title: Any
    url_path: Any
    vars: Any
    def __init__(self, url_path, relative_path, absolute_path) -> None: ...
    def get_template_name(self) -> Any: ...
