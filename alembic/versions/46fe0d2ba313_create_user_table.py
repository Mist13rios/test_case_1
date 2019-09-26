"""create user table

Revision ID: 46fe0d2ba313
Revises: 
Create Date: 2019-09-26 13:35:45.269164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46fe0d2ba313'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(30)),
        sa.Column('last_name', sa.String(30)),
        sa.Column('nickname', sa.String(30)),
        sa.Column('email', sa.String(40)),
    )


def downgrade():
    op.drop_table('users')
