from typing import Union

from .db import WikidataClaim
from .labels import lookup_label


def get_label(eid):
    label = lookup_label(eid)
    if label == eid:
        return label
    else:
        return f"{eid}:{label}"


class TreeResult:
    def __init__(self, root_id: str):
        self.root_id = root_id
        self.children: list['TreeResult'] = []

    def to_dict(self, fetch_label=True) -> dict:
        item = {
            "root_id": self.root_id,
            "children": [child.to_dict() for child in self.children]
        }

        if fetch_label:
            item["label"] = get_label(self.root_id)

        return item

    def __repr__(self) -> str:
        """
        Returns a string representation of the tree using indentation.
        """
        return self._repr_helper()

    def _repr_helper(self, level: int = 0, is_last: bool = True, fetch_label=False) -> str:
        label = get_label(self.root_id) if fetch_label else self.root_id

        prefix = "    " * (level - 1) + ("└── " if is_last and level > 0 else "├── " if level > 0 else "")
        result = f"{prefix}{label}\n"

        for idx, child in enumerate(self.children):
            is_last_child = idx == len(self.children) - 1
            result += child._repr_helper(level + 1, is_last_child, fetch_label)

        return result

    def show(self):
        return print(self._repr_helper(fetch_label=True))

    def flatten(self) -> list[str]:
        """
        Flattens the tree into a list of root_ids using preorder traversal.
        :return: List of all node root_ids.
        """
        flat_list = []

        def _flatten(node: 'TreeResult'):
            flat_list.append(node.root_id)
            for child in node.children:
                _flatten(child)

        _flatten(self)
        return flat_list


def get_tree(root: str, prop_id: str, direction='forward') -> TreeResult:
    """
    Entry point for building the tree. Initializes visited set.
    """
    if direction not in ['forward', 'backward']:
        raise ValueError('direction must be either "forward" or "backward"')
    visited = set()
    if isinstance(prop_id, str):
        prop_id = [prop_id]
    return _build_tree(root, prop_id, visited, direction)


def _build_tree(root: str, prop_id: list[str], visited: set[str], direction) -> TreeResult:
    """
    Auxiliary recursive function to build the tree.
    """
    if root in visited:
        # Prevent infinite loops in case of cyclic references
        return TreeResult(root)

    visited.add(root)
    tree = TreeResult(root)

    # Get immediate children
    children = list_neighbors(root, prop_id, direction)

    # Recursively process each child
    for child_id in children:
        child_tree = _build_tree(child_id, prop_id, visited, direction)
        tree.children.append(child_tree)

    return tree


def list_neighbors(root: str, prop_id: Union[list[str], str], direction) -> list[str]:
    if isinstance(prop_id, str):
        prop_id = [prop_id]

    if direction == 'forward':
        query = WikidataClaim.select().where(
            WikidataClaim.source_entity == root,
            WikidataClaim.property_id.in_(prop_id),
        )
        return [
            item.target_entity for item in query
        ]

    elif direction == 'backward':
        query = WikidataClaim.select().where(
            (WikidataClaim.target_entity == root) &
            (WikidataClaim.property_id.in_(prop_id))
        )
        return [
            item.source_entity for item in query
        ]

    else:
        return []


def list_instances_of(clz):
    query = WikidataClaim.select().where(
        WikidataClaim.property_id == 'P31',
        (WikidataClaim.target_entity == clz),
    )
    for claim in query:
        yield claim
