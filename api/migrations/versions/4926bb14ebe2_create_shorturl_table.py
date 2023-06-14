"""Create ShortURL table

Revision ID: 4926bb14ebe2
Revises: 
Create Date: 2023-06-13 17:27:45.045210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4926bb14ebe2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shorturls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Text(), nullable=False),
    sa.Column('short_url', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shorturls')
    # ### end Alembic commands ###