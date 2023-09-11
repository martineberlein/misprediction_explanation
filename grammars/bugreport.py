import string
from fuzzingbook.Grammars import srange, Grammar

#bugreport Grammar(after normalization and multiplication to remove negative and float values)
BUGREPORT: Grammar = {
    "<start>": ["<priority> <NCommentT> <NActor> <meanCommentSize> <ticketCleanedBodyLen> <nticketsByCreatorOpen> <nClosedticketsByCreatorOpen> <nCommentsByCreator> <NCommentByActorsT> <NticketsCreatedInProject> <NticketsCreatedInProjectT> <NticketsCreatedInProjectClosed> <NticketsCreatedInProjectClosedT> <NActivityInProject> <NActivityInProjectT> <chainLength> <longTimeHold> <lateTriageDays> <InitialActivityCount> <InitialActionCount> <recentActionCount> <recentActivityCount> <activitysequence> <projectCoverage>"],
    "<priority>": ["0", "<onenine><maybe_digits>"],
    "<NCommentT>": ["0", "<onenine><maybe_digits>"],
    "<NActor>": ["0", "<onenine><maybe_digits>"],
    "<meanCommentSize>": ["0", "<onenine><maybe_digits>"],
    "<ticketCleanedBodyLen>": ["0", "<onenine><maybe_digits>"],
    "<nticketsByCreatorOpen>": ["0", "<onenine><maybe_digits>"],
    "<nClosedticketsByCreatorOpen>": ["0", "<onenine><maybe_digits>"],
    "<nCommentsByCreator>": ["0", "<onenine><maybe_digits>"],
    "<NCommentByActorsT>": ["0", "<onenine><maybe_digits>"],
    "<NticketsCreatedInProject>": ["0", "<onenine><maybe_digits>"],
    "<NticketsCreatedInProjectT>": ["0", "<onenine><maybe_digits>"],
    "<NticketsCreatedInProjectClosed>": ["0", "<onenine><maybe_digits>"],
    "<NticketsCreatedInProjectClosedT>": ["0", "<onenine><maybe_digits>"],
    "<NActivityInProject>": ["0", "<onenine><maybe_digits>"],
    "<NActivityInProjectT>": ["0", "<onenine><maybe_digits>"],
    "<chainLength>": ["0", "<onenine><maybe_digits>"],
    "<longTimeHold>": ["0", "<onenine><maybe_digits>"],
    "<lateTriageDays>": ["0", "<onenine><maybe_digits>"],
    "<InitialActivityCount>": ["0", "<onenine><maybe_digits>"],
    "<InitialActionCount>": ["0", "<onenine><maybe_digits>"],
    "<recentActionCount>": ["0", "<onenine><maybe_digits>"],
    "<recentActivityCount>": ["0", "<onenine><maybe_digits>"],
    "<activitysequence>": ["0", "<onenine><maybe_digits>"],
    "<projectCoverage>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
