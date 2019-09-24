"""empty message

Revision ID: 3e8df3b6b947
Revises: 84fb16a1886a
Create Date: 2019-09-20 14:05:08.780483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8df3b6b947'
down_revision = '84fb16a1886a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_message_read_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_message_read_time')
    # ### end Alembic commands ###