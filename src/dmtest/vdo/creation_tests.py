"""VDO device creation and cleanup test.

Minimal test that verifies VDO device can be created and automatically
cleaned up without errors. Tests the basic infrastructure for VDO testing.
"""

from dmtest.fixture import Fixture
from dmtest.test_register import TestRegister
from dmtest.vdo.utils import standard_vdo


def t_create(fix: Fixture) -> None:
    with standard_vdo(fix) as vdo:
        pass

def register(tests: TestRegister) -> None:
    tests.register("/vdo/creation/create01", t_create)
