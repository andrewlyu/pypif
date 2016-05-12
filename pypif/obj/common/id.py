import numbers
from pypif.obj.common.pio import Pio


class Id(Pio):
    """
    Information about a generic identifier.
    """

    def __init__(self, name=None, value=None, **kwargs):
        """
        Constructor.

        :param name: String with the name of the identifier.
        :param value: String or number with the value of the identifier.
        :param kwargs: Dictionary of fields that are not supported.
        """
        super(Id, self).__init__(**kwargs)
        self._name = None
        self.name = name
        self._value = None
        self.value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._validate_type('name', name, basestring)
        self._name = name

    @name.deleter
    def name(self):
        self._name = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._validate_list_type('value', value, basestring, numbers.Number)
        self._value = value

    @value.deleter
    def value(self):
        self._value = None