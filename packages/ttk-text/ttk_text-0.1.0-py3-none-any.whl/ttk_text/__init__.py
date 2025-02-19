from tkinter import Event, EventType, Grid, Pack, Place, Text
from tkinter.ttk import Frame, Style

__all__ = ["ThemedText"]


class ThemedText(Text):
    def __init__(
            self,
            master=None,
            relief=None,
            width=None,
            height=None,
            style="TextFrame.TEntry",
            class_="TextFrame",
            **kw
    ):
        self.frame = Frame(
            master,
            width=width,
            height=height,
            relief=relief,
            style=style,
            class_=class_
        )
        Text.__init__(
            self,
            self.frame,
            width=0,
            height=0,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            **kw
        )
        self.pack(side="left", fill="both", expand=True)
        for sequence in ("<FocusIn>", "<FocusOut>", "<Enter>", "<Leave>", "<ButtonPress-1>", "<ButtonRelease-1>"):
            self.bind(sequence, self.__on_change_state, "+")
        self.bind("<<ThemeChanged>>", self.__on_theme_changed, "+")
        self.__copy_geometry_methods()
        self._apply_theme()

    def _apply_theme(self):
        style_obj = Style(self)
        style = self.frame.cget("style")
        self.configure(
            selectbackground=style_obj.lookup(style, "selectbackground", ["focus"]) or None,
            selectforeground=style_obj.lookup(style, "selectforeground", ["focus"]) or None,
            insertwidth=style_obj.lookup(style, "insertwidth", ["focus"], 1),
            font=style_obj.lookup(style, "font", None, "TkDefaultFont"),
        )
        self.frame.configure(
            padding=style_obj.lookup(style, "padding", None, 1),
            borderwidth=style_obj.lookup(style, "borderwidth", None, 1),
        )

    def __on_change_state(self, event: Event):
        match event.type:
            case EventType.FocusIn:
                self.frame.state(["focus"])
            case EventType.FocusOut:
                self.frame.state(["!focus"])
            case EventType.Enter:
                self.frame.state(["hover"])
            case EventType.Leave:
                self.frame.state(["!hover"])
            case EventType.ButtonPress:
                if event.num == 1:
                    self.frame.state(["pressed"])
            case EventType.ButtonRelease:
                if event.num == 1:
                    self.frame.state(["!pressed"])

    def __on_theme_changed(self, _: Event):
        self._apply_theme()

    def __copy_geometry_methods(self):
        """
        Copy geometry methods of self.frame without overriding Text methods.
        """

        for m in (vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()).difference(vars(Text).keys()):
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


def example():
    from tkinter import Tk

    root = Tk()
    root.geometry("300x300")
    root.title("ThemedText")
    text = ThemedText(root)
    text.pack(fill="both", expand=True, padx="7p", pady="7p")
    text.insert("1.0", "Hello, ThemedText!")
    root.mainloop()


if __name__ == "__main__":
    example()
