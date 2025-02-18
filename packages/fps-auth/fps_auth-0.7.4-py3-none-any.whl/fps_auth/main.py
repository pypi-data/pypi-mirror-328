import structlog
from fastapi_users.exceptions import UserAlreadyExists
from fps import Module

from jupyverse_api.app import App
from jupyverse_api.auth import Auth, AuthConfig
from jupyverse_api.frontend import FrontendConfig
from jupyverse_api.main import QueryParams

from .config import _AuthConfig
from .routes import auth_factory

log = structlog.get_logger()


class AuthModule(Module):
    def __init__(self, name: str, **kwargs):
        super().__init__(name)
        self.auth_config = _AuthConfig(**kwargs)

    async def prepare(self) -> None:
        self.put(self.auth_config, AuthConfig)

        app = await self.get(App)
        frontend_config = await self.get(FrontendConfig)

        auth = auth_factory(app, self.auth_config, frontend_config)
        self.put(auth, Auth)

        await auth.db.create_db_and_tables()

        if self.auth_config.test:
            try:
                await auth.create_user(
                    username="admin@jupyter.com",
                    email="admin@jupyter.com",
                    password="jupyverse",
                    permissions={"admin": ["read", "write"]},
                )
            except UserAlreadyExists:
                pass

        try:
            await auth.create_user(
                username=self.auth_config.token,
                email=self.auth_config.global_email,
                password="",
                permissions={},
            )
        except UserAlreadyExists:
            global_user = await auth.get_user_by_email(self.auth_config.global_email)
            await auth._update_user(
                global_user,
                username=self.auth_config.token,
                permissions={},
            )

        if self.auth_config.mode == "token":
            query_params = await self.get(QueryParams)
            query_params.d["token"] = self.auth_config.token
