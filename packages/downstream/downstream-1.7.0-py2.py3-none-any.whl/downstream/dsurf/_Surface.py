import types
import typing


class Surface:
    "Container orchestrating downstream curation over a fixed-size buffer."

    __slots__ = ("_storage", "algo", "T")

    algo: types.ModuleType
    _storage: typing.MutableSequence  # storage sites
    T: int  # current logical time

    def __init__(
        self: "Surface",
        algo: types.ModuleType,
        storage: typing.Union[typing.MutableSequence[object], int],
    ) -> None:
        """Initialize a downstream Surface object, which stores hereditary 
        stratigraphic annotations using a provided algorithm.

        Parameters
        ----------
        algo: module
            The algorithm used by the surface to determine the placements  
            of data items. Should be one of the modules in `downstream.dstream`.
        storage: int or MutableSequence
            The object used to hold any ingested data. If an integer is 
            passed in, a list of length `storage` is used. Otherwise, the 
            `storage` is used directly. Random access and `__len__` must be 
            supported. For example, for efficient storage, a user may pass 
            in a NumPy array.
        """
        self.T = 0
        if isinstance(storage, int):
            self._storage = [None] * storage
        else:
            self._storage = storage
        self.algo = algo

    def __iter__(self: "Surface") -> typing.Iterator[object]:
        return iter(self._storage)

    def __getitem__(self: "Surface", site: int) -> object:
        return self._storage[site]

    @property
    def S(self: "Surface") -> int:
        return len(self._storage)

    def enumerate(
        self: "Surface",
    ) -> typing.Iterable[typing.Tuple[int, object]]:
        """Iterate over ingest times and values of retained data items."""
        return zip(self.lookup(), self._storage)

    def ingest(self: "Surface", item: object) -> typing.Optional[int]:
        """Ingest data item.

        Returns the storage site of the data item, or None if the data item is
        not retained.
        """
        assert self.algo.has_ingest_capacity(self.S, self.T)

        site = self.algo.assign_storage_site(self.S, self.T)
        if site is not None:
            self._storage[site] = item
        self.T += 1
        return site

    def lookup(self: "Surface") -> typing.Iterable[int]:
        """Iterate over ingest times of retained data items."""
        assert len(self._storage) == self.S
        return self.algo.lookup_ingest_times(self.S, self.T)
