from typing import List, Union
from abc import ABC, abstractmethod

from ghostos.abcd import Operator, Ghost
from ghostos.libraries.multighosts.abcd import MultiGhosts
from ghostos.libraries.multighosts.data import MultiGhostData, Topic


class AbsMultiGhosts(MultiGhosts, ABC):

    @property
    @abstractmethod
    def _data(self) -> MultiGhostData:
        pass

    @abstractmethod
    def _save_data(self):
        pass

    def save_ghosts(self, *ghosts: Ghost) -> None:
        self._data.ghosts.add_ghosts(*ghosts)

    def get_ghosts(self, *names: str) -> List[Ghost]:
        ghosts = []
        for name in names:
            ghost = self._data.ghosts.get_ghost(name)
            ghosts.append(ghost)
        return ghosts

    def create_topic(self, name: str, description: str, ghosts: List[Union[Ghost, str]]) -> None:
        ghosts_instances = []
        for ghost in ghosts:
            if isinstance(ghost, Ghost):
                ghosts_instances.append(ghost)
            elif isinstance(ghost, str):
                instance = self.get_ghosts(ghost)
                ghosts_instances.append(instance)
            else:
                raise AttributeError(f"Invalid ghost type: {type(ghost)}")

        topic = Topic(name=name, description=description)
        topic.add_ghosts(*ghosts_instances)
        self._data.topics[name] = topic
        self._save_data()

    def public_chat(self, topic: str, message: str, *names: str) -> Operator:
        pass

    def private_chat(self, topic: str, message: str, names: List[str]) -> Operator:
        pass

    def parallel_chat(self, topic: str, message: str, *names: str) -> Operator:
        pass

    def async_chat(self, topic: str, message: str, *names: str) -> Operator:
        pass

    def clear_topic(self, topic: str) -> None:
        if topic in self._data.topics:
            del self._data.topics[topic]
        self._save_data()
