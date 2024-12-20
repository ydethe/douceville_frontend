"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from supabase import create_client, Client

from rxconfig import config


def create_access_token(supabase_url: str, supabase_key: str, email: str, password: str) -> str:
    supabase: Client = create_client(supabase_url, supabase_key)
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})

    token = response.session.access_token
    supabase.auth.sign_out()
    return token


class State(rx.State):
    """The app state."""

    username: str
    password: str
    token: str

    @rx.event
    def connect(self):
        self.token = create_access_token(
            config.SUPABASE_URL, config.SUPABASE_KEY, self.username, self.password
        )
        return rx.redirect("/map")


def login_default_icons() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.jpg",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Se connecter",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Courriel",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                    on_blur=State.set_username,
                ),
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Mot de passe",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Mot de passe oublié ?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Mot de passe",
                    type="password",
                    size="3",
                    width="100%",
                    on_blur=State.set_password,
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Connection", size="3", width="100%", on_click=State.connect),
            rx.center(
                rx.text("Pas encore de compte ?", size="3"),
                rx.link("Créer un compte", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )


def index() -> rx.Component:
    return (
        rx.cond(
            State.token == "",
            rx.container(
                login_default_icons(),
                rx.logo(),
            ),
            map(),
        ),
    )


def map() -> rx.Component:
    return rx.box(rx.text("This is a page"))


app = rx.App()
app.add_page(index)
app.add_page(map)
