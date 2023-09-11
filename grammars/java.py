import string
from fuzzingbook.Grammars import srange, Grammar

#java Grammar(after normalization and multiplication to remove negative and float values)
JAVA: Grammar = {
    "<start>": ["<parallel_changed_file_num> <commit_num> <file_added> <file_removed> <file_renamed> <file_modified> <file_copied> <line_added> <line_removed> <developer_num> <duration> <commit_density> <add_frequency> <bug_frequency> <change_frequency> <delete_frequency> <document_frequency> <feature_frequency> <fix_frequency> <improve_frequency> <refactor_frequency> <remove_frequency> <update_frequency> <use_frequency> <messages_min> <messages_max> <messages_mean> <messages_median>"],
    "<parallel_changed_file_num>": ["0", "<onenine><maybe_digits>"],
    "<commit_num>": ["0", "<onenine><maybe_digits>"],
    "<file_added>": ["0", "<onenine><maybe_digits>"],
    "<file_removed>": ["0", "<onenine><maybe_digits>"],
    "<file_renamed>": ["0", "<onenine><maybe_digits>"],
    "<file_modified>": ["0", "<onenine><maybe_digits>"],
    "<file_copied>": ["0", "<onenine><maybe_digits>"],
    "<line_added>": ["0", "<onenine><maybe_digits>"],
    "<line_removed>": ["0", "<onenine><maybe_digits>"],
    "<developer_num>": ["0", "<onenine><maybe_digits>"],
    "<duration>": ["0", "<onenine><maybe_digits>"],
    "<commit_density>": ["0", "<onenine><maybe_digits>"],
    "<add_frequency>": ["0", "<onenine><maybe_digits>"],
    "<bug_frequency>": ["0", "<onenine><maybe_digits>"],
    "<change_frequency>": ["0", "<onenine><maybe_digits>"],
    "<delete_frequency>": ["0", "<onenine><maybe_digits>"],
    "<document_frequency>": ["0", "<onenine><maybe_digits>"],
    "<feature_frequency>": ["0", "<onenine><maybe_digits>"],
    "<fix_frequency>": ["0", "<onenine><maybe_digits>"],
    "<improve_frequency>": ["0", "<onenine><maybe_digits>"],
    "<refactor_frequency>": ["0", "<onenine><maybe_digits>"],
    "<remove_frequency>": ["0", "<onenine><maybe_digits>"],
    "<update_frequency>": ["0", "<onenine><maybe_digits>"],
    "<use_frequency>": ["0", "<onenine><maybe_digits>"],
    "<messages_min>": ["0", "<onenine><maybe_digits>"],
    "<messages_max>": ["0", "<onenine><maybe_digits>"],
    "<messages_mean>": ["0", "<onenine><maybe_digits>"],
    "<messages_median>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
