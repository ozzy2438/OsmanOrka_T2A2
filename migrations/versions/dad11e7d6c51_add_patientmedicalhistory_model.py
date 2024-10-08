"""Add PatientMedicalHistory model

Revision ID: dad11e7d6c51
Revises: 26a591fc2058
Create Date: 2024-09-25 15:43:47.629556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dad11e7d6c51'
down_revision = '26a591fc2058'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient_medical_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('record_date', sa.Date(), nullable=False),
    sa.Column('diagnosis', sa.String(length=200), nullable=False),
    sa.Column('treatment', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient_medical_history')
    # ### end Alembic commands ###
