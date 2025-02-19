# Copyright 2023-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""### Module fp.err_handling - monadic error handling

Functional data types to use in lieu of exceptions.

#### Error handling types:

* class **MB**: Maybe (Optional) monad
* class **XOR**: Left biased Either monad

"""
from __future__ import annotations

__all__ = [ 'MB', 'XOR' ]

from collections.abc import Callable, Iterator, Sequence
from typing import cast, Final, Never, overload, TypeVar
from .singletons import Sentinel

D = TypeVar('D')
L = TypeVar('L')
R = TypeVar('R')
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

class MB[D]():
    """Maybe monad - class wrapping a potentially missing value.

    * where `MB(value)` contains a possible value of type `~D`
    * `MB()` semantically represent a non-existent or missing value of type `~D`
    * `MB` objects are self flattening, therefore a `MB` cannot contain a MB
      * `MB(MB(d)) == MB(d)`
      * `MB(MB()) == MB()`
    * immutable semantics, map & bind return new instances
      * warning: hashed values invalidated if contained value is mutated
      * warning: hashed values invalidated if put or pop methods are called
    * unsafe method `get` and `pop`
      * will raise `ValueError` if MB is empty
    * stateful methods `put` and `pop`
      * useful to treat a `MB` as a stateful object
      * basically a container that can contain 1 or 0 objects

    """
    __slots__ = '_value',
    __match_args__ = '_value',

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, value: MB[D]) -> None: ...
    @overload
    def __init__(self, value: D) -> None: ...

    def __init__(self, value: D|MB[D]|Sentinel=Sentinel('MB')) -> None:
        self._value: D|Sentinel
        _sentinel: Final[Sentinel] = Sentinel('MB')
        match value:
            case MB(d) if d is not _sentinel:
                self._value = d
            case MB(s):
                self._value = _sentinel
            case d:
                self._value = d

    def __bool__(self) -> bool:
        return self._value is not Sentinel('MB')

    def __iter__(self) -> Iterator[D]:
        if self:
            yield cast(D, self._value)

    def __repr__(self) -> str:
        if self:
            return 'MB(' + repr(self._value) + ')'
        else:
            return 'MB()'

    def __len__(self) -> int:
        return (1 if self else 0)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self._value is other._value:
            return True
        elif self._value == other._value:
            return True
        else:
            return False

    @overload
    def get(self) -> D|Never: ...
    @overload
    def get(self, alt: D) -> D: ...
    @overload
    def get(self, alt: Sentinel) -> D|Never: ...

    def get(self, alt: D|Sentinel=Sentinel('MB')) -> D|Never:
        """Return the contained value if it exists, otherwise an alternate value.

        * alternate value must be of type `~D`
        * raises `ValueError` if an alternate value is not provided but needed

        """
        _sentinel: Final[Sentinel] = Sentinel('MB')
        if self._value is not _sentinel:
            return cast(D, self._value)
        else:
            if alt is _sentinel:
                msg = 'MB: an alternate return type not provided'
                raise ValueError(msg)
            else:
                return cast(D, alt)

    def put(self, value: D) -> None:
        """Put a value in the MB if empty, if not empty do nothing."""
        if self._value is Sentinel('MB'):
            self._value = value

    def pop(self) -> D|Never:
        """Pop the value if the MB is not empty, otherwise fail."""
        _sentinel: Final[Sentinel] = Sentinel('MB')
        if self._value is _sentinel:
            msg = 'MB: Popping from an empty MB'
            raise ValueError(msg)
        else:
            popped = cast(D, self._value)
            self._value = _sentinel
            return popped

    def map[U](self, f: Callable[[D], U]) -> MB[U]:
        """Map function `f` over the 0 or 1 elements of this data structure.

        * if `f` should fail, return a MB()

        """
        if self._value is Sentinel('MB'):
            return cast(MB[U], self)
        else:
            try:
                return MB(f(cast(D, self._value)))
            except Exception:
                return MB()

    def bind[U](self, f: Callable[[D], MB[U]]) -> MB[U]:
        """Map `MB` with function `f` and flatten."""
        try:
            return (f(cast(D, self._value)) if self else MB())
        except Exception:
            return MB()

    @staticmethod
    def call[U, V](f: Callable[[U], V], u: U) -> MB[V]:
        """Return an function call wrapped in a MB"""
        try:
            return MB(f(u))
        except Exception:
            return MB()

    @staticmethod
    def lz_call[U, V](f: Callable[[U], V], u: U) -> Callable[[], MB[V]]:
        def ret() -> MB[V]:
            return MB.call(f, u)
        return ret

    @staticmethod
    def idx[V](v: Sequence[V], ii: int) -> MB[V]:
        """Return an indexed value wrapped in a MB"""
        try:
            return MB(v[ii])
        except IndexError:
            return MB()

    @staticmethod
    def lz_idx[V](v: Sequence[V], ii: int) -> Callable[[], MB[V]]:
        def ret() -> MB[V]:
            return MB.idx(v, ii)
        return ret

    @staticmethod
    def sequence[T](seq_mb_d: Sequence[MB[T]]) -> MB[Sequence[T]]:
        """Sequence an indexable container of `MB[~D]`

        * if all the contained `MB` values in the container are not empty,
          * return a `MB` of a container containing the values contained
          * otherwise return an empty `MB`

        """
        l: list[T] = []

        for mb_d in seq_mb_d:
            if mb_d:
                l.append(mb_d.get())
            else:
                return MB()

        ds = cast(Sequence[T], type(seq_mb_d)(l))  # type: ignore # will be a subclass at runtime
        return MB(ds)

class XOR[L, R]():
    """Either monad - class semantically containing either a left or a right
    value, but not both.

    * implements a left biased Either Monad
    * `XOR(left: ~L, right: ~R)` produces a left `XOR` which
      * contains a value of type `~L`
      * and a potential right value of type `~R`
    * `XOR(MB(), right)` produces a right `XOR`
    * in a Boolean context
      * `True` if a left `XOR`
      * `False` if a right `XOR`
    * two `XOR` objects compare as equal when
      * both are left values or both are right values whose values
        * are the same object
        * compare as equal
    * immutable, an `XOR` does not change after being created
      * immutable semantics, map & bind return new instances
        * warning: contained values need not be immutable
        * warning: not hashable if value or potential right value mutable

    """
    __slots__ = '_left', '_right'
    __match_args__ = ('_left', '_right')

    @overload
    def __init__(self, left: L, right: R, /) -> None: ...
    @overload
    def __init__(self, left: MB[L], right: R, /) -> None: ...

    def __init__(self, left: L|MB[L], right: R, /) -> None:
        self._left: L|MB[L]
        self._right: R
        match left:
            case MB(l) if l is not Sentinel('MB'):
                self._left, self._right = cast(L, l), right
            case MB(s):
                self._left, self._right = MB(), right
            case l:
                self._left, self._right = l, right

    def __bool__(self) -> bool:
        return MB() != self._left

    def __iter__(self) -> Iterator[L]:
        if self:
            yield cast(L, self._left)

    def __repr__(self) -> str:
        if self:
            return 'XOR(' + repr(self._left) + ', ' + repr(self._right) + ')'
        else:
            return 'XOR(MB(), ' + repr(self._right) + ')'

    def __str__(self) -> str:
        if self:
            return '< ' + str(self._left) + ' | >'
        else:
            return '< | ' + str(self._right) + ' >'

    def __len__(self) -> int:
        # Semantically, an XOR always contains just one value.
        return 1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False

        if self and other:
            if self._left is other._left:
                return True
            elif self._left == other._left:
                return True
            else:
                return False

        if not self and not other:
            if self._right is other._right:
                return True
            elif self._right == other._right:
                return True
            else:
                return False

        return False

    @overload
    def getLeft(self) -> MB[L]: ...
    @overload
    def getLeft(self, altLeft: L) -> MB[L]: ...
    @overload
    def getLeft(self, altLeft: MB[L]) -> MB[L]: ...

    def getLeft(self, altLeft: L|MB[L]=MB()) -> MB[L]:
        """Get value if a left.

        * if the `XOR` is a left, return its value
        * if a right, return an alternate value of type ~L` if it is provided
          * alternate value provided directly
          * or optionally provided with a MB
        * returns a `MB[L]` for when an altLeft value is needed but not provided

        """
        _sentinel = Sentinel('MB')
        match altLeft:
            case MB(l) if l is not _sentinel:
                if self:
                    return MB(self._left)
                else:
                    return MB(cast(L, l))
            case MB(s):
                if self:
                    return MB(self._left)
                else:
                    return MB()
            case l:
                if self:
                    return MB(self._left)
                else:
                    return MB(l)

    def getRight(self) -> R:
        """Get value of `XOR` if a right, potential right value if a left.

        * if `XOR` is a right, return its value
        * if `XOR` is a left, return the potential right value

        """
        return self._right

    def makeRight(self) -> XOR[L, R]:
        """Make a right based on the `XOR`.

        * return a right based on potential right value
        * returns itself if already a right

        """
        if self._left == MB():
            return self
        else:
            return cast(XOR[L, R], XOR(MB(), self._right))

    def newRight(self, right: R) -> XOR[L, R]:
        """Swap in a right value.

        * returns a new instance with a new right (or potential right) value.

        """
        if self._left == MB():
            return cast(XOR[L, R], XOR(MB(), right))
        else:
            return cast(XOR[L, R], XOR(self._left, right))

    def map[U](self, f: Callable[[L], U]) -> XOR[U, R]:
        """Map over if a left value.

        * if `XOR` is a left then map `f` over its value
          * if `f` successful return a left `XOR[S, R]`
          * if `f` unsuccessful return right `XOR[S, R]`
            * swallows any exceptions `f` may throw
        * if `XOR` is a right
          * return new `XOR(right=self._right): XOR[S, R]`
          * use method `mapRight` to adjust the returned value

        """
        if self._left == MB():
            return cast(XOR[U, R], self)
        try:
            applied = f(cast(L, self._left))
        except Exception:
            return cast(XOR[U, R], XOR(MB(), self._right))
        else:
            return XOR(applied, self._right)

    def mapRight(self, g: Callable[[R], R], altRight: R) -> XOR[L, R]:
        """Map over a right or potential right value."""
        try:
            applied = g(self._right)
            right = applied
        except:
            right = altRight

        if self:
            left: L|MB[L] = cast(L, self._left)
        else:
            left = MB()

        return XOR(left, right)

    def bind[U](self, f: Callable[[L], XOR[U, R]]) -> XOR[U, R]:
        """Flatmap - bind

        * map over then flatten left values
        * propagate right values

        """
        if self._left == MB():
            return cast(XOR[U, R], self)
        else:
            return f(cast(L, self._left))

    @staticmethod
    def call[U, V](f: Callable[[U], V], left: U) -> XOR[V, MB[Exception]]:
        try:
            return XOR(f(left), MB())
        except Exception as esc:
            return XOR(MB(), MB(esc))

    @staticmethod
    def lz_call[U, V](f: Callable[[U], V], left: U) -> Callable[[], XOR[V, MB[Exception]]]:
        def ret() -> XOR[V, MB[Exception]]:
            return XOR.call(f, left)
        return ret

    @staticmethod
    def idx[V](v: Sequence[V], ii: int) -> XOR[V, MB[Exception]]:
        try:
            return XOR(v[ii], MB())
        except Exception as esc:
            return XOR(MB(), MB(esc))

    @staticmethod
    def lz_idx[V](v: Sequence[V], ii: int) -> Callable[[], XOR[V, MB[Exception]]]:
        def ret() -> XOR[V, MB[Exception]]:
            return XOR.idx(v, ii)
        return ret

    @staticmethod
    def sequence(seq_xor_lr: Sequence[XOR[L, R]], potential_right: R) -> XOR[Sequence[L], R]:
        """Sequence an indexable container of `XOR[L, R]`

        * if all the `XOR` values contained in the container are lefts, then
          * return an `XOR` of the same type container of all the left values
          * setting the potential right `potential_right`
        * if at least one of the `XOR` values contained in the container is a right,
          * return a right XOR containing the right value of the first right

        """
        l: list[L] = []

        for xor_lr in seq_xor_lr:
            if xor_lr:
                l.append(xor_lr.getLeft().get())
            else:
                return XOR(MB(), xor_lr.getRight())

        ds = cast(Sequence[L], type(seq_xor_lr)(l))  # type: ignore # will be a subclass at runtime
        return XOR(ds, potential_right)

