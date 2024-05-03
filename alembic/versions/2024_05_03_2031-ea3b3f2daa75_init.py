"""init

Revision ID: ea3b3f2daa75
Revises: 
Create Date: 2024-05-03 20:31:04.991840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea3b3f2daa75'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useraccount',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('project_id', sa.UUID(), nullable=False),
    sa.Column('env', sa.String(), nullable=False),
    sa.Column('domain', sa.String(), nullable=False),
    sa.Column('locktime', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('useraccount')
    # ### end Alembic commands ###