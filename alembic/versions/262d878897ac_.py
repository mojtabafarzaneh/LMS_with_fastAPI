"""empty message

Revision ID: 262d878897ac
Revises: bc9f932ac890
Create Date: 2024-06-15 21:11:44.003934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '262d878897ac'
down_revision: Union[str, None] = 'bc9f932ac890'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
