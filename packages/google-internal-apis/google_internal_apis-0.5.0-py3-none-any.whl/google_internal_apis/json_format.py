import warnings
from datetime import date, datetime
from pprint import pformat

from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import StringValue
from google.type.date_pb2 import Date

__all__ = ["from_datetime", "dump", "parse"]


def from_datetime(dt: datetime) -> Timestamp:
    """
    Convert a datetime object to a protobuf Timestamp object
    """
    m = Timestamp()
    m.FromDatetime(dt)
    return m


def dump_repeated(message, field):
    if field.type == field.TYPE_MESSAGE:
        return [dump(item) for item in getattr(message, field.name)]
    return getattr(message, field.name)


def dump(message):
    """
    Convert a protobuf message to a recursive list of values
    """
    if isinstance(message, Timestamp):
        return str(message.ToMilliseconds())
    if isinstance(message, StringValue):
        return message.value if message.value else None
    if isinstance(message, Date):
        return date(year=message.year, month=message.month, day=message.day).isoformat()
    fields = message.DESCRIPTOR.fields
    arrays = []
    for field in fields:
        match field.label:
            case field.LABEL_REPEATED:
                arrays.append(dump_repeated(message, field))
            case field.LABEL_REQUIRED:
                if field.type == field.TYPE_MESSAGE:
                    arrays.append(dump(getattr(message, field.name)))
                else:
                    arrays.append(getattr(message, field.name))
            case field.LABEL_OPTIONAL:
                if field.type == field.TYPE_MESSAGE:
                    arrays.append(dump(getattr(message, field.name)))
                else:
                    arrays.append(getattr(message, field.name))
            case _:
                raise ValueError("Unknown label")
    return arrays


def repeated(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        for array in value:
            parse(array, getattr(message, field.name).add())
    else:
        getattr(message, field.name).extend(value)


def required(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        parse(value, getattr(message, field.name))
    else:
        setattr(message, field.name, value)


def optional(message, field, value):
    if field.type == field.TYPE_MESSAGE:
        parse(value, getattr(message, field.name))
    else:
        setattr(message, field.name, value)


def parse(arrays, message):
    """
    Convert a recursive list of values to a protobuf message
    """
    fields = message.DESCRIPTOR.fields
    if isinstance(message, Timestamp):
        message.FromMilliseconds(int(arrays))
        return message
    if isinstance(message, StringValue):
        if arrays:
            message.value = arrays
        return message
    if isinstance(message, Date):
        dt = date.fromisoformat(arrays)
        message.year = dt.year
        message.month = dt.month
        message.day = dt.day
        return message

    for field in fields:
        parse_field(message, field, arrays)
    remaining = arrays[fields[-1].number :]
    if remaining:
        warnings.warn("Extra fields: " + pformat(remaining))
    return message


def parse_field(message, field, arrays):
    match field.label:
        case field.LABEL_REPEATED:
            value = arrays[field.number - 1]
            repeated(message, field, value)
        case field.LABEL_REQUIRED:
            value = arrays[field.number - 1]
            required(message, field, value)
        case field.LABEL_OPTIONAL:
            if len(arrays) >= field.number:
                value = arrays[field.number - 1]
                optional(message, field, value)
        case _:
            raise ValueError("Unknown label")
