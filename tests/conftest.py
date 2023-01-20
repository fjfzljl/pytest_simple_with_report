#!/usr/bin/python3
import sys
sys.path.append('.')
sys.path.append('tests')

import logging
import pytest



logger = logging.getLogger("unit test")

@pytest.fixture(scope="module")
def suite_dashwebsetupteardown():
    logger.info("suite_dashwebsetupteardown fixture start...")

    yield

    logger.info("suite_dashwebsetupteardown fixture end...")

@pytest.fixture
def eachtest_umbcld_setupteardown(request):
    logger.info("eachtest_umbcld_setupteardown fixture start...")
    
    arg_1 = request.param[0]
    logger.info(f'setup arg : {arg_1}')

    yield

    logger.info("eachtest_umbcld_setupteardown fixture end...")
