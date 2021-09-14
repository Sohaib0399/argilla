from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.text2_text_query import Text2TextQuery
from ..types import UNSET, Unset

T = TypeVar("T", bound="Text2TextSearchRequest")


@attr.s(auto_attribs=True)
class Text2TextSearchRequest:
    """API SearchRequest request

    Attributes:
    -----------

    query: Text2TextQuery
        The search query configuration"""

    query: Union[Text2TextQuery, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query: Union[Text2TextQuery, Unset] = UNSET
        _query = d.pop("query", UNSET)
        if not isinstance(_query, Unset):
            query = Text2TextQuery.from_dict(_query)

        text2_text_search_request = cls(
            query=query,
        )

        text2_text_search_request.additional_properties = d
        return text2_text_search_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties