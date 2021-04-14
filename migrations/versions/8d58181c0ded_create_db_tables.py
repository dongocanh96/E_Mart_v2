"""create db tables

Revision ID: 8d58181c0ded
Revises: 
Create Date: 2021-04-14 16:28:26.093764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d58181c0ded'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_email'), 'account', ['email'], unique=True)
    op.create_index(op.f('ix_account_name'), 'account', ['name'], unique=True)
    op.create_index(op.f('ix_account_phone_number'), 'account', ['phone_number'], unique=True)
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('collection', sa.String(length=255), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=False)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_table('item_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_cart_id'), 'item_cart', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_cart_id'), table_name='item_cart')
    op.drop_table('item_cart')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_account_phone_number'), table_name='account')
    op.drop_index(op.f('ix_account_name'), table_name='account')
    op.drop_index(op.f('ix_account_email'), table_name='account')
    op.drop_table('account')
    # ### end Alembic commands ###