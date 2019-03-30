"""remove key-value store (stop using simplekv... we will do our own thing)

Revision ID: a5915c5a78eb
Revises: 78514b173380
Create Date: 2019-03-02 15:02:04.315615

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a5915c5a78eb'
down_revision = '78514b173380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kv_store')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kv_store',
    sa.Column('key', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('value', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('key', name='kv_store_pkey')
    )
    # ### end Alembic commands ###