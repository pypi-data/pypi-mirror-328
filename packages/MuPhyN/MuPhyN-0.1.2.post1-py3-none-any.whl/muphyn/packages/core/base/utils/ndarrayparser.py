import numpy as np
import re
from ast import literal_eval
from typing import List, Union

from .regexes import Regex

def formatMatlab(array: Union[List, np.ndarray]):
    # First sub
    arrayStr = np.array2string(array)

    # Execute first match
    matches = re.findall(r"\b\s*\]+\s*\[+", arrayStr)
    
    while len(matches) > 0:

        # Get match string
        matchedString = matches[0]

        # Count brackets
        openBracketsCount = matchedString.count("[")
        closeBracketsCount = matchedString.count("]")
        if openBracketsCount == closeBracketsCount:
            arrayStr = arrayStr.replace(matchedString, f" {';' * closeBracketsCount} ", 1)
        else:
            raise(ValueError(f"An error occured while parsing string array:\n{np.array2string(array)}\n\n{arrayStr}"))

        # Update list
        matches = re.findall(r"\b\s*\]+\s*\[+", arrayStr)

    return re.sub(r"\]+", "]", re.sub(r"\[+", "[", arrayStr))

def formatPython(array: Union[List, np.ndarray]):
    return np.array2string(array, separator=',', floatmode="maxprec")

def formatArray(array: Union[List, np.ndarray], target = "python"):
    if target == "python":
        return formatPython(array)
    elif target == "matlab":
        return formatMatlab(array)
    else:
        raise(ValueError(f"Unsupported target: \"{target}\" instead of \"matlab\" or \"python\""))
        
def detectOrigin(arrayStr: str):

    if Regex.isMatlabArray(arrayStr):
        origin = "matlab"
    elif Regex.isPythonArray(arrayStr):
        origin = "python"
    else:
        raise(ValueError("No matlab or python matrix detected"))
    
    return origin

def convertMatlabMatrix2Python(arrayStr: str) -> str:
   
    # Replace all space separator
    for vectorMatch in re.findall(Regex.MatlabVector, arrayStr):
        # Build python string
        pythonVector = re.sub(r"\s+", ", ", vectorMatch)

        # Replace space separator
        arrayStr = re.sub(
            vectorMatch, 
            pythonVector, 
            arrayStr
        )

    # Replace all semicolon 
    maxLevel = -1

    for semicolonGroupMatch in re.findall(r"\s*\;+\s*", arrayStr):
        # Update level
        level = semicolonGroupMatch.count(';')
        maxLevel = max(maxLevel, level)

        #
        arrayStr = re.sub(semicolonGroupMatch, "] " * level + "," + " [" * level, arrayStr)

    return "[ " * (maxLevel - 1) + arrayStr + " ]" * (maxLevel - 1)

def decodeMatlab(arrayStr: str) -> np.ndarray:
    # Convert to python matrix
    pythonMatrix = convertMatlabMatrix2Python(arrayStr)

    return decodePython(pythonMatrix)

def decodePython(arrayStr: str):
    return np.array(literal_eval(arrayStr))

def decodeArray(arrayStr: str, origin = None) -> np.ndarray:
    # Auto detect ND-array string origin
    if origin is None:
        origin = detectOrigin(arrayStr)
        
    # Decode array
    if origin == "matlab":
        return decodeMatlab(arrayStr)
    elif origin == "python":
        return decodePython(arrayStr)
    else:
        raise(ValueError(f"Unsupported origin value: {origin}"))

if __name__ == "__main__":
    # Init array
    shape = np.random.randint(2, 4, 4)
    array = np.random.rand(*shape) * 20 - 10

    for target in [
            "matlab", 
            "python"
        ]:
        print("="*25, target, "=" * 25)

        # Build string array
        arrayStr = formatArray(array, target=target)

        # Decode array
        newArray = decodeArray(arrayStr)

        print(newArray.mean() - array.mean())

        print("="*23, f"END {target}", "=" * 23)