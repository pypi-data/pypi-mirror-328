import re
from ast import literal_eval

from typing import List

class Regex:

    # Boolean regexes
    BooleanRegex = r"\s*[tT]rue\s*|\s*[fF]alse\s*|\s*[01]{1}\s*"
    FalseRegex = r"\s*[fF]alse\s*|\s*0\s*"
    TrueRegex = r"\s*[tT]rue\s*|\s*1\s*"
    
    # Integer regex
    IntegerRegex = r"[-+]?[0-9]*"

    # Comma float regexes 
    CommaFloatRegex = r"[\+|-]?(?:(?:[0-9]+(?:\,(?:[0-9]+)?)?)|(?:(?:[0-9]+)?\,[0-9]+))(?:\s*[Ee]\s*[\+|-]?[0-9]+)?"
    CommaScientificNumberRegex = r"[\+|-]?(?:(?:[0-9]+(?:\,(?:[0-9]+)?)?)|(?:(?:[0-9]+)?\,[0-9]+))(?:\s*[Ee]\s*[\+|-]?[0-9]+)"

    # Dot float regexes
    DotFloatRegex = r"[\+|-]?(?:(?:[0-9]+(?:\.(?:[0-9]+)?)?)|(?:(?:[0-9]+)?\.[0-9]+))(?:\s*[Ee]\s*[\+|-]?[0-9]+)?"
    DotScientificNumberRegex = r"[\+|-]?(?:(?:[0-9]+(?:\.(?:[0-9]+)?)?)|(?:(?:[0-9]+)?\.[0-9]+))(?:\s*[Ee]\s*[\+|-]?[0-9]+)"

    # String literal regex
    StringLiteralRegex = r"\".*\""

    # Email
    EmailRegex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

    # Matrix & Vector
    MatlabMatrixRegex = r"\[(?:(?:(?:\s*[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)\s+)*(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)\s*)\;+\s*)*(?:(?:\s*[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)\s+)*(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)\s*)))\]"
    MatlabVector = r"(?:(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)\s+)*(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+)?)))"
    PythonMatrixRegex = r"\[\s*(?:(?:\[\s*(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+))\s*\,\s*)*(?:[\+|-]?[0-9]+(?:\.(?:[0-9]+)))\s*\])\s*\,?\s*)+\]"
    AllMatrixFormatRegex = r"(?P<matlab>{})|(?P<python>{})".format(MatlabMatrixRegex, PythonMatrixRegex)

    # Number Separators
    SpaceSeparatorRegex = r"(?<=[\d|\.])\s+(?=[\d|-])"
    CommaSeparatorRegex = r"(?<=[\d|\.])\s*\,\s*(?=[\d|-])"
    SemiColonSeparatorRegex = r"(?<=[\d|\.])\s*\;\s*(?=[\d|-])"

    # ----------
    # Functions
    # ----------

    @staticmethod
    def isArray(value: str) -> bool:
        return Regex.isMatlabArray(value) or Regex.isPythonArray(value)
    
    @staticmethod
    def isMatlabArray(value: str) -> bool:
        return re.match(Regex.MatlabMatrixRegex, value) is not None
    
    @staticmethod
    def isPythonArray(value: str) -> bool:
        try:
            return type(literal_eval(value)) == list
        except:
            return False
    
    @staticmethod
    def isBoolean(value: str) -> bool:
        return re.match(Regex.BooleanRegex, value) is not None

    @staticmethod
    def isTrueValue(value: str) -> bool:
        return re.match(Regex.TrueRegex, value) is not None

    @staticmethod
    def isFalseValue(value: str) -> bool:
        return re.match(Regex.FalseRegex, value) is not None

    @staticmethod
    def isInteger(value: str) -> bool:
        return re.match(Regex.IntegerRegex, value) is not None

    @staticmethod
    def isCommaFloat(value: str) -> bool:
        return re.match(Regex.CommaFloatRegex, value) is not None

    @staticmethod
    def isCommaScientificFloat(value: str) -> bool:
        return re.match(Regex.CommaScientificNumberRegex, value) is not None

    @staticmethod
    def isDotFloat(value: str) -> bool:
        return re.match(Regex.DotFloatRegex, value) is not None

    @staticmethod
    def isDotScientificFloat(value: str) -> bool:
        return re.match(Regex.DotScientificNumberRegex, value)

    @staticmethod
    def isFloat(value: str) -> bool:
        return re.match(Regex.DotFloatRegex, value) is not None or re.match(Regex.DotScientificNumberRegex, value) is not None

    @staticmethod
    def isStringLiteral(value: str) -> bool:
        return re.match(Regex.StringLiteralRegex, value) is not None

    @staticmethod
    def isEmailAddress(value: str):
        return re.match(Regex.EmailRegex, value) is not None
    
    @staticmethod
    def findAll(value: str, pattern: str) -> List[str]:
        return re.findall(pattern, value)
    
if __name__ == "__main__":
    # Number types
    intergerStrings = [*[str(i) for i in range(-9, 10)], "-123456789", "132456789"]
    assert all([Regex.isInteger(intergerString) for intergerString in intergerStrings]), "Error in detecting integer strings"

    dotFloatStrings = ["1", "-1", "1.", "-1.", "1.0", "-1.0", "1234.56789", 
        "-1234.56789", "0.56789", "-0.56789", "0.56789", "-0.56789", "1.0e10",
        "-1.0e10", "1.0e-10", "-1.0e-10"]

    assert all([Regex.isDotFloat(dotFloatString) for dotFloatString in dotFloatStrings]), "Error in detecting dot float strings"

    commaFloatStrings = ["1", "-1", "1,", "-1,", "1,0", "-1,0", "1234,56789", 
        "-1234,56789", "0,56789", "-0,56789", "0,56789", "-0,56789", "1,0e10",
        "-1,0e10", "1,0e-10", "-1,0e-10"]

    assert all([Regex.isCommaFloat(commaFloatString) for commaFloatString in commaFloatStrings]), "Error in detecting comma float strings"

    # Boolean type
    booleanStrings = ["False", "True", "false", "true"]

    assert all([Regex.isBoolean(booleanString) for booleanString in booleanStrings]), "Error in boolean strings"

    # String literal type
    stringLiterals = ["\"False\"", "\"True\"", "\"false\"", "\"true\""]

    assert all([Regex.isStringLiteral(stringLiteral) for stringLiteral in stringLiterals]), "Error in string literal strings"

    # Email regex
    mailAdresseStrings = [
        "development@ceref.be"
    ]

    assert all([Regex.isEmailAddress(mailAdresseString) for mailAdresseString in mailAdresseStrings]), "Error in mail address strings"

    # Matrices & vectors
    arrayStrings = [
        "[1.23456789 1.23456789 1.23456789 ; 1.23456789 1.23456789 1.23456789 ;; 1.23456789 1.23456789 1.23456789 ; 1.23456789 1.23456789 1.23456789]",
        "[[[1.23456789, 1.23456789, 1.23456789], [1.23456789, 1.23456789, 1.23456789]], [[1.23456789, 1.23456789, 1.23456789], [1.23456789, 1.23456789, 1.23456789]]]",
        "[1, 2, 3]",
        "[[]]"
    ]

    assert Regex.isMatlabArray(arrayStrings[0]), "Error in matlab array strings"
    assert Regex.isPythonArray(arrayStrings[1]), "Error in python array strings"
    assert all([Regex.isArray(arrayString) for arrayString in arrayStrings]), "Error in array strings"