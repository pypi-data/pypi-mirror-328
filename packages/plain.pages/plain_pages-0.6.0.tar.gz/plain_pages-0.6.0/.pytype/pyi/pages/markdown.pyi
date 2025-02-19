# (generated with --quick)

import _typeshed
import html.parser
import mistune
import pygments.formatter
import pygments.lexer
from pygments.formatters import html
from typing import Any, TypeVar, overload

HTMLParser: type[html.parser.HTMLParser]
slugify: Any

_T = TypeVar('_T', str, bytes)

class InnerTextParser(html.parser.HTMLParser):
    text_content: list
    def __init__(self) -> None: ...
    def handle_data(self, data) -> None: ...

class PagesRenderer(Any):
    def block_code(self, code, info = ...) -> str: ...
    def heading(self, text, level, **attrs) -> Any: ...

def get_inner_text(html_content) -> str: ...
def get_lexer_by_name(_alias: str, **options) -> pygments.lexer.Lexer: ...
@overload
def highlight(code, lexer, formatter: pygments.formatter.Formatter[_T], outfile: _typeshed.SupportsWrite[_T]) -> None: ...
@overload
def highlight(code, lexer, formatter: pygments.formatter.Formatter[_T], outfile: None = ...) -> _T: ...
def render_markdown(content) -> Any: ...
