"""init

Revision ID: 8979571d8f5e
Revises: 
Create Date: 2021-08-04 14:48:43.231492

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau



# revision identifiers, used by Alembic.
revision = '8979571d8f5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('is_admin', sa.Boolean, default=False ),
        sa.Column('user_email', sau.EmailType, nullable=False)
    )


def downgrade():
    op.drop_table('users')