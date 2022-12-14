"""songs table

Revision ID: e92f12d37515
Revises: 
Create Date: 2022-08-30 20:44:16.719073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92f12d37515'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('song_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('artist', sa.VARCHAR(length=50), nullable=True),
    sa.Column('genre', sa.VARCHAR(length=50), nullable=True),
    sa.Column('song_vibe', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('song_id')
    )
    op.create_table('weather',
    sa.Column('weather_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('song_vibe', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('weather_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    op.drop_table('songs')
    # ### end Alembic commands ###
