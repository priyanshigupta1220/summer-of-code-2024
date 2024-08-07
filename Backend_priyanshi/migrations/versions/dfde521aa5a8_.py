"""empty message

Revision ID: dfde521aa5a8
Revises: 1dcca1718256
Create Date: 2024-07-12 21:43:24.539140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfde521aa5a8'
down_revision = '1dcca1718256'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventoryitem', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_sku', sa.Integer(), nullable=False))
        batch_op.drop_column('item_SKU')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inventoryitem', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_SKU', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('item_sku')

    # ### end Alembic commands ###
