"""empty message

Revision ID: 1665159d0695
Revises: 
Create Date: 2023-11-02 15:11:08.613869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1665159d0695'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ac',
    sa.Column('ac_no', sa.Integer(), nullable=False),
    sa.Column('cust_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ac_no')
    )
    op.create_table('admin',
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('emp_id')
    )
    op.create_table('user',
    sa.Column('cust_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('initial_dep', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('cust_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('admin')
    op.drop_table('ac')
    # ### end Alembic commands ###
