import string
from fuzzingbook.Grammars import srange, Grammar

#water Grammar(after normalization and multiplication to remove negative and float values)
WATER: Grammar = {
    "<start>": ["<ph> <Hardness> <Solids> <Chloramines> <Sulfate> <Conductivity> <Organic_carbon> <Trihalomethanes> <Turbidity>"],
    "<ph>": ["0", "<onenine><maybe_digits>"],
    "<Hardness>": ["0", "<onenine><maybe_digits>"],
    "<Solids>": ["0", "<onenine><maybe_digits>"],
    "<Chloramines>": ["0", "<onenine><maybe_digits>"],
    "<Sulfate>": ["0", "<onenine><maybe_digits>"],
    "<Conductivity>": ["0", "<onenine><maybe_digits>"],
    "<Organic_carbon>": ["0", "<onenine><maybe_digits>"],
    "<Trihalomethanes>": ["0", "<onenine><maybe_digits>"],
    "<Turbidity>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
