from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Header, Footer


class Canvas(Widget):
    def render(self) -> RenderResult:
        return ('█' * 70 + '\n') * 10 + 'XO║═╗╝╚╔'


class SnakeApp(App):
    TITLE = 'Snake'
    CSS_PATH = 'app.css'

    def compose(self) -> ComposeResult:
        yield Header()
        yield Canvas()
        yield Footer()

    def on_mount(self) -> None:
        pass


if __name__ == '__main__':
    app = SnakeApp()
    app.run()
