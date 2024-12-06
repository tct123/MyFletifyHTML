import flet as ft
from myfletify import MyFletifyHTML


html_content = "example.html"
flet_code = MyFletifyHTML(html=html_content)


def main(page: ft.Page):
    page.scroll = "always"
    page.add(flet_code.get_flet())
    page.update()


ft.app(target=main)
