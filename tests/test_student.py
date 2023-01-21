import student

import pytest
import os
import logging

logger = logging.getLogger("unit test")


@pytest.mark.TEST00001
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, name, score, check_string, expected_result",
    [
        ("TEST00001 : test get_name() return correct name", ["debug"], "bob", 80, "bob", True),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_get_name(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    name,
    score,
    check_string,
    expected_result,
):
    test_get_name.__doc__ = dstring
    logger.info(f"processing arg name : {name}")
    logger.info(f"processing arg score : {score}")
    logger.info(f"processing arg check_string : {check_string}")
    sd = student.Student(name, score)
    assert (check_string == sd.get_name()) == expected_result

@pytest.mark.TEST00002
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, name, score, check_number, expected_result",
    [
        ("TEST00002 : test get_score() return correct score", ["debug"], "bob", 80, 80, True),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_get_score(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    name,
    score,
    check_number,
    expected_result,
):
    test_get_score.__doc__ = dstring
    logger.info(f"processing arg name : {name}")
    logger.info(f"processing arg score : {score}")
    logger.info(f"processing arg check_number : {check_number}")
    sd = student.Student(name, score)
    assert (check_number == sd.get_score()) == expected_result

@pytest.mark.TEST00003
@pytest.mark.TEST00004
@pytest.mark.TEST00005
@pytest.mark.TEST00006
@pytest.mark.TEST00007
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, name, score, check_level, expected_result",
    [
        ("TEST00003 : test get_score_level() level A", ["debug"], "bob", 81, 'A', True),
        ("TEST00004 : test get_score_level() level B", ["debug"], "bob", 80, 'B', True),
        ("TEST00005 : test get_score_level() level C", ["debug"], "bob", 41, 'C', True),
        ("TEST00006 : test get_score_level() level D", ["debug"], "bob", 40, 'D', True),
        ("TEST00007 : test get_score_level() error score ", ["debug"], "bob", 101, 90, False),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_get_score_level(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    name,
    score,
    check_level,
    expected_result,
):
    test_get_score_level.__doc__ = dstring
    logger.info(f"processing arg name : {name}")
    logger.info(f"processing arg score : {score}")
    logger.info(f"processing arg check_level : {check_level}")
    sd = student.Student(name, score)
    assert (check_level == sd.get_score_level()) == expected_result
