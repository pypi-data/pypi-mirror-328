from typing import Union, List, Dict

from ghostos.abcd import Operator, Session, Ghost, Shell
from ghostos.core.runtime import GoTaskStruct, EventTypes
from ghostos.core.messages import Message, Role
from ghostos.identifier import get_identifier
from ghostos.helpers import md5


class PublicChatOperator(Operator):

    def __init__(self, hostname: str, message: str, ghosts: List[Ghost]):
        self.hostname = hostname
        self.message = message
        self.ghosts = ghosts

    @staticmethod
    def get_ghost_task_id(session: Session, ghost: Ghost) -> str:
        name = get_identifier(ghost).name
        return md5(f"multi-ghosts:session:{session.task.task_id}:ghost_name:{name}")

    def run(self, session: Session) -> Union[Operator, None]:

        host_message = Role.USER.new(
            content=self.message,
            name=self.hostname,
        )
        shell = session.container.force_fetch(Shell)
        conversations = {}
        threads = {}
        for task_id, ghost in self.ghosts.items():
            conversation = shell.sync(ghost, task_id=task_id)
            conversations[task_id] = conversation
            thread = conversation.get_thread()
            # copy a thread.
            thread = thread.thread_copy()
            event = EventTypes.INPUT.new(task_id=task_id, messages=[host_message])
            thread.new_turn(event)
            threads[task_id] = thread

        for task_id, conversation in conversations.items():
            event = EventTypes.ROTATE.new(task_id=task_id, messages=[])
            conversation.respond_event()

        return session.mindflow().think()

    def destroy(self):
        del self.ghosts
