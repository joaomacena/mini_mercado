"""test update

Revision ID: 5c1bb442af53
Revises: 21195dc788a2
Create Date: 2021-12-16 12:06:24.739467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c1bb442af53'
down_revision = '21195dc788a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('technical_details', sa.String(length=255), nullable=True))
    op.drop_column('products', 'technnical_details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('technnical_details', sa.VARCHAR(length=255), nullable=True))
    op.drop_column('products', 'technical_details')
    # ### end Alembic commands ###
