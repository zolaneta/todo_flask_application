"""empty message

Revision ID: 1708b480ca90
Revises: None
Create Date: 2016-02-09 13:32:07.857948

"""

# revision identifiers, used by Alembic.
revision = '1708b480ca90'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('priority',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('priority_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.Column('creation_date', sa.Date(), nullable=True),
    sa.Column('is_done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['priority_id'], ['priority.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    op.drop_table('priority')
    op.drop_table('category')
    ### end Alembic commands ###
