#!/usr/bin/python3
import sys

sys.path.append(".")
sys.path.append("tests")

import logging
import pytest


logger = logging.getLogger("unit test")


@pytest.fixture(scope="module")
def suite_setupteardown():
    logger.info("suite_setupteardown fixture start...")

    logger.info("software install ...")

    yield

    logger.info("software uninstall...")

    logger.info("suite_setupteardown fixture end...")


@pytest.fixture
def eachtest_setupteardown(request):
    logger.info("eachtest_setupteardown fixture start...")


    arg_1 = request.param[0]
    logger.info(f"type : {arg_1}")

    logger.info("change system configuration...")

    yield

    logger.info("recover system configuration...")

    logger.info("eachtest_setupteardown fixture end...")
