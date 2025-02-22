from dataclasses import dataclass

from aisle.parser.nodes.legend import LegendSelector


@dataclass(init=False)
class StylingAttributes:
    """Style attrs."""

    bg: str | None = None
    fg: str | None = None

    def __init__(self, **kwargs):
        """Custom init for allowing excessive arguments."""
        for kw_k, kw_v in kwargs.items():
            setattr(self, kw_k, kw_v)


@dataclass
class LegendStyling:
    """Legend style declaration."""

    selector: LegendSelector
    attrs: StylingAttributes
    description: str
