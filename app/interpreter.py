import re
from typing import Dict

def check_if_hebrew(match: Dict[str, str]) -> bool:
    alef_ad_taf = range(ord('א'), ord('ת') + 1)
    if ord(match['command'][0]) in alef_ad_taf:
        return True
    return False


def hebrew_time_fixer(match: Dict[str, str]) -> Dict[str, str]:
    copy = match.copy()
    start = match['start']
    end = match['end']
    copy['start'] = end
    copy['end'] = start
    return copy

def get_groups(message: str) -> Dict[str, str]:
    regex = regex = r"(?P<command>.{3,4}) (?P<day>\d{1,2})\/(?P<month>\d{1,2})\/?(?P<year>\d{4}|\d{2})? ?(?P<start>\d{1,2}\:\d{2})?-?(?P<end>\d{1,2}\:\d{2})? (?P<content>.+)"
    m = re.match(regex, message, re.MULTILINE)
    return m.groupdict()


def interapt_message(message: str) -> Dict[str, str]:
    gd = get_groups(message)
    return gd