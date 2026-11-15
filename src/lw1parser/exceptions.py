class LW1ParserError(Exception):
    """Base exception for errors"""

class TacticalSaveError(LW1ParserError):
    """A tactical save was selected"""

class Xcom2jsonMissingError(LW1ParserError):
    """xcom2json.exe could not be found"""

class Xcom2jsonUnknownError(LW1ParserError):
    """xcom2json.exe failed for another reason, please report"""