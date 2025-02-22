# nilvec.pyi
from typing import List, Optional, Tuple, Any

class PyHNSW:
    def __init__(
        self,
        dim: int,
        m: Optional[int] = None,
        ef_construction: Optional[int] = None,
        ef_search: Optional[int] = None,
        metric: Optional[str] = None,
        schema: Optional[List[str]] = None,
    ) -> None: ...
    def insert(
        self,
        vector: List[float],
        metadata: Optional[List[Tuple[str, Any]]] = None,
    ) -> None: ...
    def search(
        self,
        query: List[float],
        k: Optional[int] = None,
        filter: Optional[Tuple[str, Any]] = None,
    ) -> List[Tuple[float, List[float]]]: ...
    def create(
        self,
        vectors: List[List[float]],
        metadata: Optional[List[List[Tuple[str, Any]]]] = None,
    ) -> None: ...

class PyFlat:
    def __init__(
        self, dim: int, metric: Optional[str] = None, schema: Optional[List[str]] = None
    ) -> None: ...
    def insert(
        self, vector: List[float], metadata: Optional[List[Tuple[str, Any]]] = None
    ) -> None: ...
    def search(
        self,
        query: List[float],
        k: Optional[int] = None,
        filter: Optional[Tuple[str, Any]] = None,
    ) -> List[Tuple[float, List[float]]]: ...
    # def create(
    #     self,
    #     vectors: List[List[float]],
    #     metadata: Optional[List[List[Tuple[str, Any]]]] = None,
    # ) -> None: ...
