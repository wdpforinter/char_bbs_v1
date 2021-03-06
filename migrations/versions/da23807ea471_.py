"""empty message

Revision ID: da23807ea471
Revises: 5c2789c2bbf5
Create Date: 2017-04-14 21:32:54.133000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da23807ea471'
down_revision = '5c2789c2bbf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sign_in',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['front_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('signin_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signin_table',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'front_user.id'], name=u'signin_table_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('sign_in')
    # ### end Alembic commands ###
