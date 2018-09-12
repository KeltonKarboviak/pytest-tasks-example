# -*- coding: utf-8 -*-

from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'karboviak', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'karboviak',
        'done': True,
        'id': 21,
    }

    assert expected == t_dict


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'kelton', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'kelton', True, 10)

    assert t_expected == t_after


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'kelton')

    assert 'buy milk' == t.summary
    assert 'kelton' == t.owner
    assert (t.done, t.id) == (False, None)
