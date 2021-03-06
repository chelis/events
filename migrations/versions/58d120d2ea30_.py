"""empty message

Revision ID: 58d120d2ea30
Revises: None
Create Date: 2016-05-09 12:25:31.525035

"""

# revision identifiers, used by Alembic.
revision = '58d120d2ea30'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_type')
    op.drop_table('event')
    ### end Alembic commands ###
