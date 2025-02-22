# -*- coding: utf-8; -*-
################################################################################
#
#  Wutta-COREPOS -- Wutta Framework integration for CORE-POS
#  Copyright © 2025 Lance Edgar
#
#  This file is part of Wutta Framework.
#
#  Wutta Framework is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option) any
#  later version.
#
#  Wutta Framework is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  Wutta Framework.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Data models for CORE-POS integration
"""

import sqlalchemy as sa
from sqlalchemy import orm

from wuttjamaican.db import model


class CoreUser(model.Base):
    """
    CORE-POS extension for
    :class:`~wuttjamaican:wuttjamaican.db.model.auth.User`.
    """

    __tablename__ = 'corepos_user'

    uuid = model.uuid_column(sa.ForeignKey('user.uuid'), default=None)
    user = orm.relationship(
        model.User,
        cascade_backrefs=False,
        doc="""
        Reference to the
        :class:`~wuttjamaican:wuttjamaican.db.model.auth.User` which
        this record extends.
        """,
        backref=orm.backref(
            '_corepos',
            uselist=False,
            cascade='all, delete-orphan',
            cascade_backrefs=False,
            doc="""
            Reference to the CORE-POS extension record for the user.
            """)
    )

    corepos_employee_number = sa.Column(sa.Integer(), nullable=False, unique=True, doc="""
    ``employees.emp_no`` value for the user within CORE-POS.
    """)

    def __str__(self):
        return str(self.user)

CoreUser.make_proxy(model.User, '_corepos', 'corepos_employee_number')
