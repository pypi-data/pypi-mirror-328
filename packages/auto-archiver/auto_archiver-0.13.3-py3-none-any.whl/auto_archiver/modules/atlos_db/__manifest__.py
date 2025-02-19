{
    "name": "Atlos Database",
    "type": ["database"],
    "entry_point": "atlos_db::AtlosDb",
    "requires_setup": True,
    "dependencies":
        {"python": ["loguru",
                    ""],
         "bin": [""]},
    "configs": {
        "api_token": {
            "default": None,
            "help": "An Atlos API token. For more information, see https://docs.atlos.org/technical/api/",
            "required": True,
            "type": "str",
        },
        "atlos_url": {
            "default": "https://platform.atlos.org",
            "help": "The URL of your Atlos instance (e.g., https://platform.atlos.org), without a trailing slash.",
            "type": "str"
        },
    },
    "description": """
Handles integration with the Atlos platform for managing archival results.

### Features
- Outputs archival results to the Atlos API for storage and tracking.
- Updates failure status with error details when archiving fails.
- Processes and formats metadata, including ISO formatting for datetime fields.
- Skips processing for items without an Atlos ID.

### Setup
Required configs:
- atlos_url: Base URL for the Atlos API.
- api_token: Authentication token for API access.
"""
,
}
