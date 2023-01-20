#!/usr/bin/python3
import sys

sys.path.append(".")
sys.path.append("tests")

import logging
import pytest
from py.xml import html



logger = logging.getLogger("unit test")


def pytest_configure(config):
    config._metadata['test software version'] = '0.1'

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop()

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except AttributeError as error:
        logger.info("AttributeError trying to pytest_html_results_table_row - start")
        logger.error(error)
        logger.info("AttributeError trying to pytest_html_results_table_row - end")
    except Exception as e:
        logger.error(f"Unknown Exception trying to pytest_html_results_table_row : {e}")
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

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
