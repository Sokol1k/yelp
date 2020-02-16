"""create business table

Revision ID: 6e0c31f56346
Revises: 
Create Date: 2019-12-18 14:32:01.093584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e0c31f56346'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'business',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('category', sa.String(255)),
        sa.Column('address', sa.String(150)),
        sa.Column('phone', sa.String(30)),
        sa.Column('reviews', sa.String(10)),
        sa.Column('rating', sa.String(5)),
        sa.Column('image', sa.String(255)),
        sa.Column('site', sa.String(150)),
        sa.Column('workdays', sa.JSON),
    )
    op.create_unique_constraint('name', 'business', ['name'])



def downgrade():
    op.drop_table('business')
