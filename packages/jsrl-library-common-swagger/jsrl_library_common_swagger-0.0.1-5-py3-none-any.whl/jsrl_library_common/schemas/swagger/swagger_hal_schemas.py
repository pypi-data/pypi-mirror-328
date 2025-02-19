HAL_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/schemas/HALFORMAT",
    "type": "object",
    "properties": {
        "_embedded": {
            "type": "object"
        },
        "_links": {
            "type": "object",
            "properties": {
                "self": {
                    "type": "string"
                }
            },
            "required": [
                "self"
            ]
        }
    },
    "required": [
        "_embedded",
        "_links"
    ],
    "additionalProperties": False
}


HAL_SCHEMA_WITH_SINCE_PAGINATION = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/schemas/HALSCHEMAWITHSINCEPAGINATION",
    "properties": {
        "_embedded": {
            "type": "object"
        },
        "_links": {
            "properties": {
                "next": {
                    "type": "string"
                }
            }
        },
        "_totalCount": {
            "type": "integer"
        }
    },
    "required": [
        "_embedded",
        "_links",
        "_totalCount"
    ],
    "additionalProperties": False
}


HAL_SCHEMA_ERROR_MESSAGE = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/schemas/HALFORMATERRORMESSAGE",
    "allOf": [
        {
            "$ref": "/schemas/HALFORMAT"
        }
    ],
    "properties": {
        "_embedded": {
            "properties": {
                "message": {
                    "type": "string"
                }
            },
            "required": [
                "message"
            ]
        }
    }
}


HAL_SCHEMA_WITH_PAGE_PAGINATION = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/schemas/HALSCHEMAWITHPAGEPAGINATION",
    "properties": {
        "_embedded": {
            "type": "object"
        },
        "_links": {
            "properties": {
                "self": {
                    "type": "string"
                },
                "next": {
                    "type": "string"
                },
                "prev": {
                    "type": "string"
                },
                "first": {
                    "type": "string"
                },
                "last": {
                    "type": "string"
                }
            },
            "required": [
                "first",
                "last"
            ],
            "additionalProperties": False
        },
        "_totalCount": {
            "type": "integer"
        },
        "_totalPages": {
            "type": "integer"
        },
        "_page": {
            "type": "integer"
        },
        "_pageSize": {
            "type": "integer"
        }
    },
    "required": [
        "_embedded",
        "_links",
        "_totalCount",
        "_totalPages",
        "_page",
        "_pageSize"
    ],
    "additionalProperties": False
}