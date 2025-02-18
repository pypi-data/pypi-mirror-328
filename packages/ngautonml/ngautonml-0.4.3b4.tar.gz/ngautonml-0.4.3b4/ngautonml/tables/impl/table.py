'''A table of data, supporting multiple formats.'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.
import abc
from collections import defaultdict
from typing import Any, Callable, Dict, List, Type, Union


class Error(BaseException):
    '''Base class for all table-related errors.'''
    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        comma_newline = ',\n'
        return f'{self.__class__.__name__}({comma_newline.join(self.args)})'


class CanNotInstantiate(Error):
    '''The implementaiton does not understand how to use the type of value.'''


class TableValueError(Error, ValueError):
    '''Raised when a table has the correct keys but invalid values.'''


class Table(metaclass=abc.ABCMeta):
    '''The interface for Table for one variety of Table.'''
    name: str
    tags: Dict[str, List[str]]
    my_type: Type  # This is the type of the value we are wrapping.
    _value: Any  # Has type my_type.

    # All subclasses must implement this __init__ signature.
    # When we get something from a catalog we don't otherwise know what
    # arguments it needs.
    def __init__(self, value: Any):
        if not isinstance(value, self.my_type):
            raise CanNotInstantiate()
        self._value = value

    def value(self):
        '''Get the native representation of the table.

        This is special because the return object is generally mutable.
        '''
        return self._value

    def __eq__(self, other: Any) -> bool:
        '''Test two objects for equality.'''
        if not isinstance(other, self.__class__):
            return False
        return False if self.my_type != other.my_type else self._value == other._value

    def __getitem__(self, key: Any) -> Any:
        '''Select a subitem of the table by key.'''
        return self._value[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        '''Set a subitem of the table by key.'''
        self._value[key] = value

    def __len__(self) -> int:
        '''Return the length of this table.'''
        return len(self._value)

    def __str__(self) -> str:
        '''Return a string representation of the table.'''
        return f'Table({self._value})'

    def __repr__(self) -> str:
        '''Return a source representation of the table.'''
        return f'Table({self._value!r})'

    def copy(self) -> 'Table':
        '''Make a copy of the table.'''
        return self.__class__(self._value.copy())

    @property
    def shape(self) -> tuple:
        '''Get the shape of the table.'''
        return self._value.shape

    @property
    @abc.abstractmethod
    def columns(self) -> List[Union[int, str]]:
        '''Return the column names of the table.

        The can be passed to drop().
        '''

    @columns.setter
    @abc.abstractmethod
    def columns(self, value: List[Union[int, str]]) -> None:
        '''Set the column names of the table.'''

    @property
    @abc.abstractmethod
    def empty(self) -> bool:
        '''Return True if the table is empty.'''

    @abc.abstractmethod
    def to_csv(self, *args, **kwargs) -> str:
        '''Output the table as a CSV string.'''

    @abc.abstractmethod
    def as_dict(self, *args, **kwargs) -> Dict[Union[str, int], Any]:
        '''Convert table to a dictionary.'''


class TableFactory(Table, metaclass=abc.ABCMeta):
    '''A table of data, supporting multiple formats.

    We only convert the data when a specific format is requested.
    '''
    _exporters: Dict[type, Dict[type, Callable[['Table'], Any]]] = defaultdict(dict)
    _constructors: Dict[type, Callable[[Any], 'Table']] = {}
    # Ordered by issubclass() order, most general to most specific.
    _ordered_types: List[type] = []

    def __new__(cls, value: Any):
        '''Create a new table from a value.'''
        retval = None
        if type(value) in cls._constructors:
            retval = cls._constructors[type(value)](value)
        else:
            for my_type in cls._ordered_types:
                if isinstance(value, my_type):
                    retval = cls._constructors[my_type](value)
                    break
        if retval is None:
            raise CanNotInstantiate(
                f'Can not instantiate a Table from this {type(value)} value: {str(value)[:255]}')
        # Copy the as_() method from the class to the instance.
        # A better solution would be to make inheritance work properly, but I can't figure that out.
        setattr(retval, 'as_', cls.as_.__get__(retval))  # pylint: disable=no-value-for-parameter
        setattr(retval, '_cls', cls)
        return retval

    def as_(self, to_type: type) -> Any:
        '''Return the table as the requested type.'''
        try:
            return self._cls._exporters[self.my_type][to_type](self)  # type: ignore[attr-defined] # pylint: disable=no-member,protected-access
        except KeyError:
            raise TableValueError(f'Can not export {self.my_type} table to a {to_type}')  # pylint: disable=line-too-long,raise-missing-from

    @classmethod
    def register_constructor(
            cls, my_type: type, constructor: Callable[[Any], Table]) -> None:
        '''Register a new table type.

        Enables tables to be created with syntax like (e.g. using ``pd.DataFrame``
        and ``DataFrameTable``):

        .. code-block:: python

            my_df = pd.DataFrame()
            foo = Table(my_df)  # type: ignore[abstract]

        And the type of ``foo`` will be ``DataFrameTable``.

        '''
        cls._constructors[my_type] = constructor
        cls._ordered_types.append(my_type)

    @classmethod
    def register_exporter(
            cls,
            from_type: type, to_type: type,
            exporter: Callable[['Table'], Any]) -> None:
        '''Register a new exporter pair.

        Enables the as_() function:

        .. code-block: python

            foo = my_table.as_(pd.DataFrame).iloc[0, 2]

            my_np = my_table.as_(np.ndarray)
        '''
        cls._exporters[from_type][to_type] = exporter
