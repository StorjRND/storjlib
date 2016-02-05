CONTRACT_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {
            "enum": [
                ("56ce3e837f575827cb5a94e2b609756"
                 "a48fa4a3882f5e762b262af31f432878d")
            ]
        },
        "renter_id": {
            "type": ["string", "null"],
            "pattern": "^[13][a-km-zA-HJ-NP-Z0-9]{26,33}$"
        },
        "renter_address": {
            "type": ["string", "null"],
            "format": "ipv4"
        },
        "renter_port": {
            "type": ["integer", "null"],
            "minimum": 1,
            "maximum": 65535
        },
        "renter_signature": {
            "type": ["string", "null"]
        },
        "farmer_id": {
            "type": ["string", "null"],
            "pattern": "^[13][a-km-zA-HJ-NP-Z0-9]{26,33}$"
        },
        "farmer_address": {
            "type": ["string", "null"],
            "format": "ipv4"
        },
        "farmer_port": {
            "type": ["integer", "null"],
            "minimum": 1,
            "maximum": 65535
        },
        "farmer_signature": {
            "type": ["string", "null"]
        },
        "data_size": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "data_hash": {
            "type": ["string", "null"],
            "pattern": "^[0-9a-f]{64,64}$"
        },
        "store_begin": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "store_duration": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "store_end": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "audit_algorithm": {
            "type": ["string", "null"]
        },
        "audit_count": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "heartbeat_algorithm": {
            "type": ["string", "null"]
        },
        "heartbeat_count": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "heartbeat_coverage": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "payment_currency": {
            "type": ["string", "null"]
        },
        "payment_amount": {
            "type": ["integer", "null"]
        },
        "payment_download_price": {
            "type": ["integer", "null"]
        },
        "payment_destination": {
            "type": ["string", "null"]
        },
        "payment_source": {
            "type": ["string", "null"]
        },
        "payment_begin": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "payment_settlements": {
            "type": ["integer", "null"],
            "minimum": 0
        },
        "payment_interval": {
            "type": ["integer", "null"],
            "minimum": 0
        }
    },
    "additionalProperties": False,
    "required": [
        "type",
        "renter_id",
        "renter_address",
        "renter_port",
        "renter_signature",
        "farmer_id",
        "farmer_address",
        "farmer_port",
        "farmer_signature",
        "data_size",
        "data_hash",
        "store_begin",
        "store_duration",
        "store_end",
        "audit_algorithm",
        "audit_count",
        "heartbeat_algorithm",
        "heartbeat_count",
        "heartbeat_coverage",
        "payment_currency",
        "payment_amount",
        "payment_download_price",
        "payment_destination",
        "payment_source",
        "payment_begin",
        "payment_settlements",
        "payment_interval"
    ]
}