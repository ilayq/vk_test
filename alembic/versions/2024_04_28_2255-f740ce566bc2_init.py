"""init

Revision ID: f740ce566bc2
Revises: 
Create Date: 2024-04-28 22:55:21.960513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f740ce566bc2'
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
    sa.Column('env', postgresql.ENUM('PROD', 'PREPROD', 'STAGE', name='env_enum'), nullable=False),
    sa.Column('domain', postgresql.ENUM('CANARY', 'REGULAR', name='domain_enum'), nullable=False),
    sa.Column('locktime', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('useraccount')
    # ### end Alembic commands ###