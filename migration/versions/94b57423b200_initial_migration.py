"""Initial migration

Revision ID: 94b57423b200
Revises: 
Create Date: 2024-11-06 17:41:35.483668

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision: str = '94b57423b200'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('passenger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('last_name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.Column('patronymic', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=True),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema=settings.POSTGRES_SCHEMA
    )


def downgrade():
    op.drop_table('passenger', schema=settings.POSTGRES_SCHEMA)
