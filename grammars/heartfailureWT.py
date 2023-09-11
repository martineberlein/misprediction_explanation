import string
from fuzzingbook.Grammars import srange, Grammar

#Heartfailure Grammar without time (after normalization and multiplication to remove negative and float values)
HEARTFAILUREWT: Grammar = {
	"<start>": ["<age> <anaemia> <creatinine_phosphokinase> <diabetes> <ejection_fraction> <high_blood_pressure> <platelets> <serum_creatinine> <serum_sodium> <sex> <smoking>"],
	"<age>": ["0", "<onenine><maybe_digits>"],
	"<anaemia>": ["0", "<onenine><maybe_digits>"],
	"<creatinine_phosphokinase>": ["0", "<onenine><maybe_digits>"],
	"<diabetes>": ["0", "<onenine><maybe_digits>"],
	"<ejection_fraction>": ["0", "<onenine><maybe_digits>"],
	"<high_blood_pressure>": ["0", "<onenine><maybe_digits>"],
	"<platelets>": ["0", "<onenine><maybe_digits>"],
	"<serum_creatinine>": ["0", "<onenine><maybe_digits>"],
	"<serum_sodium>": ["0", "<onenine><maybe_digits>"],
	"<sex>": ["0", "<onenine><maybe_digits>"],
	"<smoking>": ["0", "<onenine><maybe_digits>"],
	"<onenine>": srange("123456789"),
	"<maybe_digits>": ["", "<digits>"],
	"<digits>": ["<digit>", "<digit><digits>"],
	"<digit>": list(string.digits)
}
