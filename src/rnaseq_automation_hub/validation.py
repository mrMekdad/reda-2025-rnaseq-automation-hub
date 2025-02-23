def required_fields(record, fields):
    return [field for field in fields if not record.get(field)]
