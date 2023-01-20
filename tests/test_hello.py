import hello

import pytest
import os
import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(levelname)-8s | %(name)s | %(asctime)s | %(module)s:%(lineno)-4d | %(message)s'
#     )

logger = logging.getLogger("unit test")


def process(name, check_string):
    logger.info(f"processing arg name : {name}")
    logger.info(f"processing arg check_string : {check_string}")
    return check_string in hello.hello_name(name)


@pytest.mark.TEST00001
@pytest.mark.parametrize(
    "dstring, eachtest_setupteardown, name, check_string, expected_result",
    [
        ("TEST00001 : test hello_name() match correct name", ["debug"], "bob", "bob", True),
        ("TEST00002 : test hello_name() incorrect str not in name", ["debug"], "bob", "haha", False),
    ],
    indirect=["eachtest_setupteardown"],
)
def test_hello_name(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    name,
    check_string,
    expected_result,
):
    test_hello_name.__doc__ = dstring
    assert process(name, check_string) == expected_result
