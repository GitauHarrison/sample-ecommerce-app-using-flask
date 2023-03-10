"""more columns

Revision ID: 9081f63cf7e1
Revises: 3e71761ddb8d
Create Date: 2023-01-24 17:07:57.879688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9081f63cf7e1'
down_revision = '3e71761ddb8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products_for_sale', schema=None) as batch_op:
        batch_op.add_column(sa.Column('added_at', sa.DateTime(), nullable=False))

    with op.batch_alter_table('purchased_products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('purchased_at', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchased_products', schema=None) as batch_op:
        batch_op.drop_column('purchased_at')
        batch_op.drop_column('price')

    with op.batch_alter_table('products_for_sale', schema=None) as batch_op:
        batch_op.drop_column('added_at')

    # ### end Alembic commands ###
