"""empty message

Revision ID: 618614d64d1c
Revises: 6cc7f073b358
Create Date: 2021-05-24 19:44:26.161445

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618614d64d1c'
down_revision = '6cc7f073b358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hibpdataclass',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hibpdataclass_description'), 'hibpdataclass', ['description'], unique=True)
    op.create_table('hibp_hibpdataclass',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('hibp_id', sa.Integer(), nullable=True),
    sa.Column('hibp_dataclass_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hibp_dataclass_id'], ['hibpdataclass.id'], ),
    sa.ForeignKeyConstraint(['hibp_id'], ['hibp.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hibp_id', 'hibp_dataclass_id', name='uq_hibp_hibpdataclass')
    )
    op.add_column('hibp', sa.Column('date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))
    op.add_column('hibp', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hibp', 'description')
    op.drop_column('hibp', 'date')
    op.drop_table('hibp_hibpdataclass')
    op.drop_index(op.f('ix_hibpdataclass_description'), table_name='hibpdataclass')
    op.drop_table('hibpdataclass')
    # ### end Alembic commands ###
