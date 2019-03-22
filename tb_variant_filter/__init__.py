from dataclasses import dataclass
from functools import wraps


@dataclass
class Location(object):
    locus: str
    start: int
    end: int
    strand: int

    @classmethod
    def from_dict(cls, d):
        """load from a dict - used to turn a json-loaded dict into a Location"""
        self = Location(
            locus=d["locus"],
            start=int(d["start"]),
            end=int(d["end"]),
            strand=int(d["strand"]),
        )
        return self

    def to_dict(self):
        return dict(
            locus=self.locus,
            start=self.start,
            end=self.end,
            strand=self.strand,
        )

    def __eq__(self, other):
        if isinstance(other, Location):
            return (
                self.locus == other.locus
                and self.start == other.start
                and self.end == other.end
                and self.strand == other.strand
            )
        return False


class DocInherit(object):
    """
    Docstring inheriting method descriptor

    The class itself is also used as a decorator
    """

    def __init__(self, mthd):
        self.mthd = mthd
        self.name = mthd.__name__

    def __get__(self, obj, cls):
        if obj:
            return self.get_with_inst(obj, cls)
        else:
            return self.get_no_inst(cls)

    def get_with_inst(self, obj, cls):

        overridden = getattr(super(cls, obj), self.name, None)

        @wraps(self.mthd, assigned=("__name__", "__module__"))
        def f(*args, **kwargs):
            return self.mthd(obj, *args, **kwargs)

        return self.use_parent_doc(f, overridden)

    def get_no_inst(self, cls):

        for parent in cls.__mro__[1:]:
            overridden = getattr(parent, self.name, None)
            if overridden:
                break

        @wraps(self.mthd, assigned=("__name__", "__module__"))
        def f(*args, **kwargs):
            return self.mthd(*args, **kwargs)

        return self.use_parent_doc(f, overridden)  # noqa

    def use_parent_doc(self, func, source):
        if source is None:
            raise NameError("Can't find '%s' in parents" % self.name)
        func.__doc__ = source.__doc__
        return func


doc_inherit = DocInherit