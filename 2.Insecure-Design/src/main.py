import os
from base64 import urlsafe_b64decode, urlsafe_b64encode
from pathlib import Path
from secrets import compare_digest
from string import ascii_lowercase, ascii_uppercase, digits

import flet as ft
import flet_fastapi
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv
from flet import CrossAxisAlignment, MainAxisAlignment, alignment

load_dotenv(dotenv_path=Path("./.env").absolute())


class KeyLengthException(Exception):
    """Key length given is not equal to 8"""

    pass


class Crypto:
    des = None

    def __init__(self, key: str):
        if len(key) != 8:
            raise KeyLengthException
        key = key.encode()
        Crypto.des = DES.new(key, DES.MODE_ECB)

    @staticmethod
    def encrypt(plain_text: str):
        plain_text = plain_text.encode()
        return Crypto.des.encrypt(pad(plain_text, 8))

    @staticmethod
    def decrypt(cipher_text: bytes):
        return unpad(Crypto.des.decrypt(cipher_text), 8).decode()


class Form(ft.View):
    def __init__(self):
        super().__init__(vertical_alignment=MainAxisAlignment.CENTER)

        self.clubLogo = ft.Container(
            ft.Image(src="favicon.png", fit=ft.ImageFit.CONTAIN)
        )
        self.usernameEntry = ft.TextField(label="Username", on_submit=self.change_focus)
        self.passwordEntry = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            on_submit=self.change_focus,
        )
        self.submitButton = ft.ElevatedButton(text="submit", expand=True)
        self.secondaryOption = ft.ElevatedButton(
            text="option", data="route change", on_click=self.go_to
        )

        self.usernameEntry.data = {"focus_on": self.passwordEntry}
        self.passwordEntry.data = {"focus_on": self.submitButton}

        layout = ft.Container()
        self.controls_list = [
            self.clubLogo,
            self.usernameEntry,
            self.passwordEntry,
            ft.Row(),
            ft.Row(controls=[self.submitButton], alignment=MainAxisAlignment.CENTER),
            ft.Row(controls=[self.secondaryOption], alignment=MainAxisAlignment.END),
        ]

        vertical_layout = ft.Column(
            controls=self.controls_list,
            expand=2,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        layout.content = ft.Row(
            controls=[ft.Container(expand=1), vertical_layout, ft.Container(expand=1)]
        )

        self.controls = [layout]

    async def change_focus(self, e):
        await e.control.data["focus_on"].focus_async()

    async def clear_entries(self, e=None):
        for i in self.controls_list:
            if isinstance(i, ft.TextField):
                i.value = ""
        await self.page.update_async()

    async def open_dialog(self, dialog):
        self.page.dialog = dialog
        self.page.dialog.open = True
        await self.page.update_async()

    async def close_dialog(self, e):
        self.page.dialog.open = False
        await self.page.update_async()
        self.page.dialog = None

    async def go_to(self, e: ft.ControlEvent | str):
        if isinstance(e, ft.ControlEvent):
            await self.page.go_async(route=e.control.data)
        else:
            await self.page.go_async(route=e)

    async def show_info(self, title, content=None):
        dialog = ft.AlertDialog(
            title=ft.Text(value=title),
            content=ft.Text(value=content) if content else None,
            actions=[ft.ElevatedButton(text="Okay!", on_click=self.close_dialog)],
        )
        await self.open_dialog(dialog)

    def is_valid_username(self, username):
        valid_chars = ascii_lowercase + ascii_uppercase + digits

        def is_valid_size(username):
            MIN_SIZE = 4
            MAX_SIZE = 16
            password_size = len(username)

            return MIN_SIZE <= password_size <= MAX_SIZE

        def all_valid_chars(username):
            for i in username:
                if i not in valid_chars:
                    return False
            return True

        try:
            if not username:
                return False

            temp_username = username.strip()[::-1]

            if not all_valid_chars(temp_username):
                return "INAVLID_CHAR"
            if not is_valid_size(temp_username):
                return "INVALID_SIZE"
            return True
        except Exception:
            return False

    def is_valid_password(self, password):
        valid_punc = "_@"
        valid_chars = ascii_lowercase + ascii_uppercase + digits + valid_punc

        def contains_character(password, sack):
            has_char = False

            for char in password:
                if char in sack:
                    has_char = True
                    break

            return has_char

        def is_valid_size(password):
            MIN_SIZE = 6
            MAX_SIZE = 20
            password_size = len(password)

            return MIN_SIZE <= password_size <= MAX_SIZE

        def get_valid_punc():
            return "".join(valid_punc)

        def all_valid_chars(username):
            for i in username:
                if i not in valid_chars:
                    return False
            return True

        try:
            if not password:
                return False

            temp_password = password.strip()[::-1]

            if not all_valid_chars(temp_password):
                return "INAVLID_CHAR"
            if not is_valid_size(temp_password):
                return "INVALID_SIZE"
            if not contains_character(temp_password, ascii_lowercase):
                return "NEEDS_LOWER"
            if not contains_character(temp_password, ascii_uppercase):
                return "NEEDS_UPPER"
            if not contains_character(temp_password, get_valid_punc()):
                return "NO_VALID_PUNC"
            if not contains_character(temp_password, digits):
                return "NEEDS_DIGIT"
            return True
        except Exception:
            return False


class LoginView(Form):
    def __init__(self, log_in_control):
        super().__init__()
        self.log_in_control = log_in_control

        self.submitButton.text = "Log In"
        self.submitButton.data = {
            "username": self.usernameEntry,
            "password": self.passwordEntry,
        }
        self.submitButton.on_click = self.log_in
        self.secondaryOption.text = "Create an account?"
        self.secondaryOption.data = "/create-account"

    async def log_in(self, e):
        if isinstance(e, ft.ControlEvent):
            e = e.control
        username = e.data["username"]
        password = e.data["password"]
        username_validity = self.is_valid_username(username.value)
        password_validity = self.is_valid_password(password.value)

        # Check if both username and password has valid characters
        if (
            (not (password_validity and username_validity))
            or isinstance(username_validity, str)
            or isinstance(password_validity, str)
        ):
            await self.show_info(title="Invalid Entry!")
        else:
            if not await self.page.client_storage.contains_key_async(
                f"RebelCTF.{username.value}.password"
            ):
                await self.show_info("Account Does Not Exist!")
            else:
                try:
                    password = password.value
                    encrypted = await self.page.client_storage.get_async(
                        f"RebelCTF.{username.value}.password"
                    )
                    encrypted = urlsafe_b64decode(encrypted)
                    decrypted = Crypto.decrypt(encrypted)
                    if len(password) == len(decrypted):
                        if compare_digest(password, decrypted):
                            self.log_in_control.logged_in = True
                            await self.go_to("/hint")
                        return
                    await self.show_info("Invalid Password!")

                except Exception as e:
                    e.with_traceback()
                    await self.show_info("Unforseen error!", content=e)
                    await self.clear_entries()

    def __str__(self):
        return super().__str__() + " LOG IN FORM"


class CreateAccountView(Form):
    def __init__(self):
        super().__init__()
        self.confirmEntry = ft.TextField(
            label="Re-Enter Password",
            password=True,
            can_reveal_password=True,
            on_submit=self.change_focus,
        )
        self.controls_list.insert(3, self.confirmEntry)

        self.usernameEntry.on_change = self.validate_username
        self.passwordEntry.data = {"focus_on": self.confirmEntry}
        self.passwordEntry.on_change = self.validate_password
        self.confirmEntry.data = {
            "focus_on": self.submitButton,
            "match_with": self.passwordEntry,
        }
        self.confirmEntry.on_change = self.confirm_password

        self.submitButton.text = "Create Account"
        self.submitButton.data = {
            "username": self.usernameEntry,
            "password": self.passwordEntry,
            "confirm_password": self.confirmEntry,
        }
        self.submitButton.on_click = self.create_account
        self.secondaryOption.text = "Already have an account?"
        self.secondaryOption.data = "/"

    async def create_account(self, e):
        if isinstance(e, ft.ControlEvent):
            e = e.control

        username = e.data["username"]
        password = e.data["password"]
        confirm_password = e.data["confirm_password"]

        if not (
            username.helper_text
            == password.helper_text
            == confirm_password.helper_text
            == ""
        ):
            await self.show_info("Please Fill in Accordingly!")
            await self.clear_entries()
        else:
            if await self.page.client_storage.contains_key_async(
                f"RebelCTF.{username.value}.password"
            ):
                await self.show_info("Account Already Exits!")
                await self.clear_entries()
            else:
                try:
                    Crypto(os.getenv("FLAG_INTERMEDIATE"))
                    await self.page.client_storage.set_async(
                        f"RebelCTF.{username.value}.password",
                        urlsafe_b64encode(Crypto.encrypt(password.value)).decode(),
                    )
                    await self.page.client_storage.set_async(
                        f"RebelCTF.{username.value}.secret",
                        urlsafe_b64encode(Crypto.encrypt(os.getenv("FLAG"))).decode(),
                    )
                    await self.show_info("Account Created!")
                    await self.clear_entries()
                except Exception as e:
                    print(e.with_traceback())
                    await self.show_info("Unforseen error!", content=e)

    async def validate_username(self, e):
        if isinstance(e, ft.ControlEvent):
            e = e.control
        match self.is_valid_username(e.value):
            case "INAVLID_CHAR":
                e.helper_text = "Invalid character!"
            case "INVALID_SIZE":
                e.helper_text = "Needs atleast 4 and atmost 16 characters"
            case True:
                e.helper_text = ""
            case _:
                e.helper_text = "Invalid Username!"
        await self.page.update_async()

    async def validate_password(self, e):
        if isinstance(e, ft.ControlEvent):
            e = e.control
        match self.is_valid_password(e.value):
            case "INAVLID_CHAR":
                e.helper_text = "Invalid character!"
            case "INVALID_SIZE":
                e.helper_text = "Needs atleast 6 and atmost 20 characters"
            case "NEEDS_LOWER":
                e.helper_text = "Needs atleast 1 lowercase alphabet"
            case "NEEDS_UPPER":
                e.helper_text = "Needs atmost 1 uppercase alphabet"
            case "NO_VALID_PUNC":
                e.helper_text = (
                    "Should have atleast one of the following characters: _, @"
                )
            case "NEEDS_DIGIT":
                e.helper_text = "Needs atleast 1 digit"

            case True:
                e.helper_text = ""
            case _:
                e.helper_text = "Invalid Password!"
        await self.confirm_password(self.confirmEntry)
        await self.page.update_async()

    async def confirm_password(self, e):
        if isinstance(e, ft.ControlEvent):
            e = e.control
        if e.value != e.data["match_with"].value:
            e.helper_text = "Passwords don't match!"
        else:
            e.helper_text = ""
        await self.page.update_async()

    def __str__(self):
        return super().__str__() + "LOG IN FORM"


class HintView(ft.View):
    def __init__(self):
        super().__init__(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER,
        )

        self.md = """# Welcome to the Nebula Phoenix's Hyperdrive Control! 
The Nebula Phoenix's Hyperdrive is a one of its kind with variable speed class adjustment system ranging from 1 (fast!) to 4 (slow!).
This is where you will be able to control the hyperdrive's settings to suit your needs.  
Few of the key features of the current suite are:
- State of the art encryption using the state of the art successor to `Lucifer`
- Storage of verification keys locally to prevent integrity loss through interception"""

        self.hyperdrivePresets = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("VELOCITY", style=ft.TextThemeStyle.DISPLAY_LARGE),
                    ft.Divider(),
                    ft.Slider(
                        min=1, max=4, divisions=30, label="Class {value}", round=2
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            expand=9,
            padding=10,
            alignment=alignment.center,
            bgcolor=ft.colors.PRIMARY_CONTAINER,
        )
        self.devIntro = ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[ft.Markdown(self.md)],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            expand=3,
            padding=10,
            alignment=alignment.center,
            bgcolor=ft.colors.TERTIARY_CONTAINER,
        )

        self.grid = ft.Row(controls=[self.hyperdrivePresets, self.devIntro])
        self.controls = [self.grid]


class App:
    logged_in = False

    async def root_main(self, page: ft.Page):
        page.title = "Insecure Design"
        page.auto_scroll = True
        page.theme = ft.Theme(
            color_scheme_seed="deeppurple",
            page_transitions=ft.PageTransitionsTheme(
                *((ft.PageTransitionTheme.FADE_UPWARDS,) * 5)
            ),
        )
        page.theme_mode = ft.ThemeMode.LIGHT
        page.vertical_alignment = MainAxisAlignment.CENTER
        page.horizontal_alignment = CrossAxisAlignment.CENTER

        await page.client_storage.clear_async()

        landing = LoginView(App)
        account_creation = CreateAccountView()
        hint = HintView()

        async def route_change(route):
            page.views.clear()
            page.views.append(landing)
            if page.route == "/create-account":
                page.views.append(account_creation)
            elif page.route == "/hint":
                if App.logged_in:  # Change this!
                    page.views.append(hint)
                else:
                    await page.go_async("/")

            await page.update_async()

        async def view_pop(view):
            top_view = page.views[-1]
            await page.go_async(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop

        await page.go_async(page.route)


app = flet_fastapi.app(App().root_main, assets_dir=Path("./assets/").absolute())
