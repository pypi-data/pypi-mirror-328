"""initial user extension

Revision ID: 0f94089f1af1
Revises: 
Create Date: 2025-01-24 21:13:14.359200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import wuttjamaican.db.util


# revision identifiers, used by Alembic.
revision: str = '0f94089f1af1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = ('wutta_corepos',)
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # corepos_user
    op.create_table('corepos_user',
                    sa.Column('uuid', wuttjamaican.db.util.UUID(), nullable=False),
                    sa.Column('corepos_employee_number', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['uuid'], ['user.uuid'], name=op.f('fk_corepos_user_uuid_user')),
                    sa.PrimaryKeyConstraint('uuid', name=op.f('pk_corepos_user')),
                    sa.UniqueConstraint('corepos_employee_number', name=op.f('uq_corepos_user_corepos_employee_number'))
                    )


def downgrade() -> None:

    # corepos_user
    op.drop_table('corepos_user')
