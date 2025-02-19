import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NewsItemResponse")


@_attrs_define
class NewsItemResponse:
    """
    Attributes:
        id (int):
        title (str):
        description (str):
        category (str):
        content (str):
        image_url (str):
        published_date (datetime.datetime):
    """

    id: int
    title: str
    description: str
    category: str
    content: str
    image_url: str
    published_date: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        category = self.category

        content = self.content

        image_url = self.image_url

        published_date = self.published_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "category": category,
                "content": content,
                "image_url": image_url,
                "published_date": published_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description")

        category = d.pop("category")

        content = d.pop("content")

        image_url = d.pop("image_url")

        published_date = isoparse(d.pop("published_date"))

        news_item_response = cls(
            id=id,
            title=title,
            description=description,
            category=category,
            content=content,
            image_url=image_url,
            published_date=published_date,
        )

        news_item_response.additional_properties = d
        return news_item_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
