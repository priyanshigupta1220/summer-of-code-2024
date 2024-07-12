"""empty message

Revision ID: 1dcca1718256
Revises: 120c21432e91
Create Date: 2024-07-12 19:15:26.043826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dcca1718256'
down_revision = '120c21432e91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.add_column(sa.Column('s_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('s_isadmin', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('s_isapproved', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('s_isdeleted', sa.Boolean(), nullable=False))
        batch_op.drop_column('s_isAdmin')
        batch_op.drop_column('s_ID')
        batch_op.drop_column('s_isApproved')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.add_column(sa.Column('s_isApproved', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('s_ID', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('s_isAdmin', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('s_isdeleted')
        batch_op.drop_column('s_isapproved')
        batch_op.drop_column('s_isadmin')
        batch_op.drop_column('s_id')

    # ### end Alembic commands ###