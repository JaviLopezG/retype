import reflex as rx

from ..layouts.nav_bar import nav_bar
from ..layouts.header_var import header_var
from ..layouts.body import body
from ..layouts.footer import footer
from ..components.main_stats import main_stats


def stats() -> rx.Component:
    return rx.center(
        rx.box(
            nav_bar(),
            header_var(),
            main_stats(),
            footer(),
            width="100%",
        ),
    )