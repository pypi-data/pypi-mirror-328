import logging
from shutil import rmtree
from typing import TYPE_CHECKING, Optional

from nio.responses import LoginError
from slidge import BaseGateway, FormField, global_config
from slixmpp import JID

from . import config
from .matrix import AuthenticationClient
from .util import Credentials

if TYPE_CHECKING:
    from .session import Session


class Gateway(BaseGateway):
    REGISTRATION_FIELDS = [
        FormField(var="homeserver", label="Home Server", required=True),
        FormField(var="username", label="User name", required=True),
        FormField(var="password", label="Password", required=True, private=True),
        FormField(
            var="device",
            label="Device name",
            value=f"matridge on {getattr(global_config, 'JID', 'dev')}",
            required=True,
        ),
    ]
    REGISTRATION_INSTRUCTIONS: str = "Enter your credentials"

    COMPONENT_NAME = "Matrix (slidge)"
    COMPONENT_TYPE = "matrix"

    COMPONENT_AVATAR = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Matrix_icon.svg/209px-Matrix_icon.svg.png"

    ROSTER_GROUP: str = "matrix"

    MARK_ALL_MESSAGES = False

    PROPER_RECEIPTS = True

    GROUPS = True

    def __init__(self):
        super().__init__()
        if not config.NIO_VERBOSE:
            logging.getLogger("peewee").setLevel(logging.WARNING)
            logging.getLogger("nio.responses").setLevel(logging.WARNING)
            logging.getLogger("nio.rooms").setLevel(logging.WARNING)

    async def validate(
        self, user_jid: JID, registration_form: dict[str, Optional[str]]
    ) -> Credentials:
        client = AuthenticationClient(
            registration_form["homeserver"],  # type:ignore
            registration_form["username"],  # type:ignore
            user_jid,
        )
        await client.fix_homeserver()
        resp = await client.login(
            registration_form["password"],  # type:ignore
            registration_form["device"],  # type:ignore
        )
        if isinstance(resp, LoginError):
            log.debug("Failed login: %r", resp)
            raise PermissionError(resp)
        return client.get_credentials(resp)

    async def unregister(self, user):
        session: "Session" = self.get_session_from_user(user)  # type: ignore
        session.matrix.stop_listen()
        await session.matrix.logout()
        rmtree(session.matrix.store_path)


log = logging.getLogger(__name__)
