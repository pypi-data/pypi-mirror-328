# -*- coding: utf-8; -*-

from wuttjamaican.testing import ConfigTestCase
from wuttjamaican.db.model import User

from wutta_corepos.db import model as mod


class TestCoreUser(ConfigTestCase):

    def test_str(self):
        user = User(username='barney')
        self.assertEqual(str(user), 'barney')

        ext = mod.CoreUser(user=user, corepos_employee_number=42)
        self.assertEqual(str(ext), 'barney')
