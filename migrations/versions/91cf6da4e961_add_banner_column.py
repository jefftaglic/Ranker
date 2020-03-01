"""Add banner column

Revision ID: 91cf6da4e961
Revises: 858da16ce17a
Create Date: 2020-02-01 17:09:02.529495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91cf6da4e961'
down_revision = '858da16ce17a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('seasons', sa.Column('banner', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('seasons', 'banner')
    # ### end Alembic commands ###