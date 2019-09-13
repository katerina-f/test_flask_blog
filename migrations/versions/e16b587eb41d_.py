"""empty message

Revision ID: e16b587eb41d
Revises: 545f084f0181
Create Date: 2019-09-09 12:17:51.352993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e16b587eb41d'
down_revision = '545f084f0181'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('post_author_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.drop_column('post', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_author_fkey', 'post', 'user', ['author'], ['id'])
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###
