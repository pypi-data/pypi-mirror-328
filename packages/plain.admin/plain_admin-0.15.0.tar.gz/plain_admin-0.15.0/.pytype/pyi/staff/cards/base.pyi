# (generated with --quick)

import enum
from typing import Any, Literal, Optional, Union

Enum: type[enum.Enum]
HttpRequest: Any
Template: Any
View: Any
slugify: Any

class Card:
    class Sizes(enum.Enum):
        FULL: Literal[4]
        LARGE: Literal[3]
        MEDIUM: Literal[2]
        SMALL: Literal[1]
    description: str
    link: str
    number: Optional[int]
    request: Any
    size: Card.Sizes
    slug: str
    template_name: str
    text: str
    title: str
    view: Any
    def get_description(self) -> str: ...
    def get_link(self) -> str: ...
    def get_number(self) -> Optional[int]: ...
    def get_slug(self) -> str: ...
    def get_template_context(self) -> dict[str, Optional[Union[int, str]]]: ...
    def get_text(self) -> str: ...
    def get_title(self) -> str: ...
    def render(self, view, request) -> Any: ...
    @classmethod
    def view_name(cls) -> str: ...
