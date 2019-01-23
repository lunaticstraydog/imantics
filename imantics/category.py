from .basic import Semantic
from .color import Color


class Category(Semantic):

    @classmethod
    def from_coco(cls, coco):
        data = {
            'name': coco.get('name'),
            'metadata': coco.get('metadata', {}),
            'id': coco.get('id', 0),
            'parent': coco.get('supercategory')
        }
        return cls(**data)

    def __init__(self, name, parent=None, metadata={}, id=0, color=None):
        self.id = id
        self.name = name
        self.parent = None
        self.color = Color.create(color)

        super().__init__(id, metadata)

    def _coco(self, include=True):

        category = {
            'id': self.id,
            'name': self.name,
            'supercategory': self.parent.name if self.parent else None,
            'metadata': self.metadata
        }

        if include:
            return {
                'categories': [category]
            }

        return category


__all__ = ["Category"]