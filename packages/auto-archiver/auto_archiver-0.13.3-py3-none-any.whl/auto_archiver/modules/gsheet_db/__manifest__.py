{
    "name": "Google Sheets Database",
    "type": ["database"],
    "entry_point": "gsheet_db::GsheetsDb",
    "requires_setup": True,
    "dependencies": {
        "python": ["loguru", "gspread", "slugify"],
    },
    "configs": {
        "allow_worksheets": {
            "default": set(),
            "help": "(CSV) only worksheets whose name is included in allow are included (overrides worksheet_block), leave empty so all are allowed",
        },
        "block_worksheets": {
            "default": set(),
            "help": "(CSV) explicitly block some worksheets from being processed",
        },
        "use_sheet_names_in_stored_paths": {
            "default": True,
            "type": "bool",
            "help": "if True the stored files path will include 'workbook_name/worksheet_name/...'",
        }
    },
    "description": """
    GsheetsDatabase:
    Handles integration with Google Sheets for tracking archival tasks.

### Features
- Updates a Google Sheet with the status of the archived URLs, including in progress, success or failure, and method used.
- Saves metadata such as title, text, timestamp, hashes, screenshots, and media URLs to designated columns.
- Formats media-specific metadata, such as thumbnails and PDQ hashes for the sheet.
- Skips redundant updates for empty or invalid data fields.

### Notes
- Currently works only with metadata provided by GsheetFeeder. 
- Requires configuration of a linked Google Sheet and appropriate API credentials.
    """
}
