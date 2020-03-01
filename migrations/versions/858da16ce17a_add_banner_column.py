"""Add banner column

Revision ID: 858da16ce17a
Revises: 9c7eb007004d
Create Date: 2020-02-01 16:54:56.194243

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '858da16ce17a'
down_revision = '9c7eb007004d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matches')
    op.drop_table('seasons')
    op.drop_table('games')
    op.drop_table('characters')
    op.drop_table('users')
    op.drop_table('scores')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scores',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('scores_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('season_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('score', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('main_name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['main_name'], ['characters.name'], name='scores_main_name_fkey'),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], name='scores_season_id_fkey'),
    sa.ForeignKeyConstraint(['username'], ['users.username'], name='scores_username_fkey'),
    sa.PrimaryKeyConstraint('id', name='scores_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('users',
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('slack_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('twitch_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('twitter_id', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('profile_img', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('homepage', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('witness', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('username', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('characters',
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('game', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('favicon', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('img', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name', name='characters_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('games',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('games_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('img', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='games_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('seasons',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('seasons_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('game_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('end', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='seasons_game_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='seasons_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('matches',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('winner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('loser_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('season_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('winner_wins', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('loser_wins', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('winner_prev_score', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('loser_prev_score', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('witness_username', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['loser_id'], ['scores.id'], name='matches_loser_id_fkey'),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], name='matches_season_id_fkey'),
    sa.ForeignKeyConstraint(['winner_id'], ['scores.id'], name='matches_winner_id_fkey'),
    sa.ForeignKeyConstraint(['witness_username'], ['users.username'], name='matches_witness_username_fkey'),
    sa.PrimaryKeyConstraint('id', name='matches_pkey')
    )
    # ### end Alembic commands ###