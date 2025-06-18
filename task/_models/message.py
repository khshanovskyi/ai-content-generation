from dataclasses import dataclass
from typing import Any

from task._models.custom_content import CustomContent
from task._models.role import Role


@dataclass
class Message:
    role: Role
    content: str
    custom_content: CustomContent | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert Message to dictionary representation."""
        result: dict[str, Any] = {
            "role": self.role.value,
            "content": self.content
        }

        if self.custom_content:
            result["custom_content"] = self.custom_content.to_dict()

        return result

    @classmethod
    def from_dict(cls, data: dict) -> "Message":
        return cls(
            role=Role(data["role"]),
            content=data.get("content", ""),
            custom_content=CustomContent.from_dict(data["custom_content"])
            if data.get("custom_content") else None
        )