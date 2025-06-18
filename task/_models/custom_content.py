from dataclasses import dataclass


@dataclass
class Attachment:
    title: str | None = None
    data: str | None = None
    type: str | None = None
    url: str | None = None

    def to_dict(self) -> dict[str, str | None]:
        return {
            "title": self.title,
            "data": self.data,
            "type": self.type,
            "url": self.url
        }


@dataclass
class CustomContent:
    attachments: list[Attachment]

    def to_dict(self) -> dict[str, list[dict]]:
        return {
            "attachments": [attachment.to_dict() for attachment in self.attachments]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CustomContent":
        attachments = []
        if attachment_data := data.get("attachments"):
            if isinstance(attachment_data, list):
                attachments = [
                    Attachment(**{k: v for k, v in attachment.items()
                                  if k in ["title", "data", "type", "url"]})
                    for attachment in attachment_data
                ]
        return cls(attachments=attachments)
