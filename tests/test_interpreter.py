from app.interpreter import check_if_hebrew, get_groups, hebrew_time_fixer


def test_get_groups():
    message_dict = get_groups('הוסף 27/10 פגישה עם שגיא')
    print(message_dict)
    assert message_dict['command'] == 'הוסף'
    assert message_dict['day'] == '27'
    assert message_dict['month'] == '10'
    assert message_dict['content'] == 'פגישה עם שגיא'


def test_get_groups_with_start_time():
    message_dict = get_groups('הוסף 27/10 19:00 פגישה עם שגיא')
    assert message_dict['command'] == 'הוסף'
    assert message_dict['day'] == '27'
    assert message_dict['month'] == '10'
    assert message_dict['content'] == 'פגישה עם שגיא'
    assert message_dict['start'] == '19:00'


def test_check_if_hebrew():
    message_dict = get_groups('הוסף 27/10 19:00 פגישה עם שגיא')
    assert check_if_hebrew(message_dict)
    message_dict = get_groups('add 27/10 meeting with sagi')
    assert not check_if_hebrew(message_dict)


def test_hebrew_time_fixer():
    message_dict = get_groups('add 27/10 12:00-19:00 meeting with sagi')
    assert message_dict['start'] == '12:00'
    message_dict = get_groups('הוסף 27/10 19:00-12:00 פגישה עם שגיא')
    assert message_dict['start'] == '19:00'
    message_dict = hebrew_time_fixer(message_dict)
    assert message_dict['start'] == '12:00'
