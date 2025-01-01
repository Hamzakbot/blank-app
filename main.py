from highrise import *
from highrise.models import *

class Mybot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        pass
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        await self.highrise.chat(f"Welcome {user.username}!")
