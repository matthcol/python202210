from typing import List, Dict, Optional

# https://realpython.com/python-type-checking/

villes: List[str] = [ "Toulouse", 'Pau', "Bayonne" ]
villes.append(1)

def getDictValue(dictionnary: Dict[str,float], key: str) -> Optional[float]:
    if key in dictionnary:
        return dictionnary[key]

# progWithHints.py:11: error: Argument 1 to "getDictValue" has incompatible type "Dict[object, object]"; expected "Dict[str, float]"
# progWithHints.py:11: error: Argument 2 to "getDictValue" has incompatible type "int"; expected "str"
wrongDict = {'a': 'a', 'b': 1, 3: 1.1}
getDictValue(wrongDict, 3)

okDict = {'a': 1.2, 'b': 1, 'c': 1.1}  # ok for int/double
optRes:Optional[float] = getDictValue(okDict, 'a')
if optRes is not None:
    print(optRes**2 + 1)
