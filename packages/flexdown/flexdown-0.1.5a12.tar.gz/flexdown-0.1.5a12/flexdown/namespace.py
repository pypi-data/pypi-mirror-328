"""Module allowing for the creation of a namespace for Flexdown from a folder"""

from dataclasses import dataclass, field
import os
from pathlib import Path
from types import SimpleNamespace
from .utils import get_flexdown_files

from reflex.utils import format, console
from flexdown import parse_file
from flexdown.document import Document


@dataclass
class FxPage:
    route: str
    title: str
    doc: Document


class FxNamespace(SimpleNamespace):
    """A namespace for Flexdown from a folder"""

    _pages: list[FxPage]
    _prefix: str | None = None

    def __init__(self, root_folder=""):
        self._pages = []
        if root_folder:
            self._folder = root_folder
            self._prefix = "".join(root_folder.rpartition("/")[:2])
            console.info(f"Init FxNamespace with {self._folder=} {self._prefix=}")
            self._load_namespace()

    def _load_namespace(self):
        """Load the namespace from the folder"""
        _files: list[str] = get_flexdown_files(self._folder)
        for _file in _files:
            _f: Path = Path(_file)
            _path: list[str] = list(_f.parts[0:-1])
            _path_no_ext: str = str(_f.with_suffix(''))
            _snakecase_path = _path_no_ext.replace(self._prefix, '') if self._prefix else _path_no_ext
            
            name = format.to_snake_case(_f.stem)
            route = format.to_kebab_case(f"/{_snakecase_path}")
            doc = parse_file(_file)

            if route.endswith("/index"):
                route = route[:-6]
                folder_dir = _f.parts[-2]
                title = folder_dir + " • " + name
            else:
                title = name

            page = FxPage(
                route,
                doc.metadata.get("title", format.to_title_case(title)),
                doc,
            )

            self._build_nested_namespace(_path, name, page)
            self._pages.append(page)

    def _build_nested_namespace(self, path, name, leaf, top_level=True):
        """Build a nested namespace"""
        namespace = format.to_snake_case(path[0])

        if getattr(self, namespace, None) is None and not top_level:
            setattr(self, namespace, FxNamespace())

        nested_namespace = self if top_level else getattr(self, namespace)

        if len(path) == 1:
            setattr(nested_namespace, name, leaf)
        else:
            nested_namespace._build_nested_namespace(path[1:], name, leaf, False)
        return nested_namespace

    def _clear_namespace(self):
        """Clear the namespace"""
        _to_del = []
        for _attr in self.__dict__:
            if _attr in ["_folder", "_prefix", "_pages"]:
                continue
            _to_del.append(_attr)

        for _attr in _to_del:
            delattr(self, _attr)

    def reload(self) -> None:
        """Reload the namespace"""
        self._pages.clear()
        self._clear_namespace()
        self._load_namespace()

    def all_pages(self) -> list[FxPage]:
        """Return the pages in the namespace.

        Returns:
            The pages.
        """
        return self._pages

    def by_tags(self, tag):
        """Return the pages by tags.

        Returns:
            The pages by tags.
        """
        _tagged_pages = []
        index = None
        for _page in self._pages:
            if _page.title.endswith("• Index"):
                index = _page
                continue
            if tag in _page.doc.metadata["tags"]:
                _tagged_pages.append(_page)
        return _tagged_pages if not index else [index, *_tagged_pages]
