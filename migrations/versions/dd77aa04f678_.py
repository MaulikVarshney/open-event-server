"""empty message

Revision ID: dd77aa04f678
Revises: 8a3de7c8b6d5
Create Date: 2018-08-07 14:17:40.707207

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'dd77aa04f678'
down_revision = '8a3de7c8b6d5'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('is_event_online', sa.Boolean(), nullable=True))
    op.add_column('events_version', sa.Column('is_event_online', sa.Boolean(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'is_event_online')
    op.drop_column('events', 'is_event_online')
    # ### end Alembic commands ###
