"""students and parents table


Revision ID: ff266731b0bb
Revises: e76475d1b6de
Create Date: 2018-05-13 23:51:36.298688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff266731b0bb'
down_revision = 'e76475d1b6de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('other_names', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=32), nullable=True),
    sa.Column('email_address', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_parents',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'person_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_parents')
    op.drop_table('student')
    op.drop_table('person')
    # ### end Alembic commands ###
