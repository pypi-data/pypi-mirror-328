import rio
import typing as t
from pathlib import Path


class LoginPage(rio.Component):
    text_value: str = ""

    def build(self) -> rio.Component:
        return rio.TextInput(
            self.bind().text_value,
            on_confirm=lambda e: None,
            align_x=0.5,
            align_y=0.5,
            min_width=30,
        )


app = rio.App(
    build=LoginPage,
)
