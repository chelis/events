"""empty message

Revision "id": f9e5bcd219de
Revises: 58d120d2ea30
Create Date: 2016-05-09 17:49:40.060992

"""

# revision identifiers, used by Alembic.
revision = 'f9e5bcd219de'
down_revision = '58d120d2ea30'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    event_types =  [{"name": "Visita"}, {"name": "Llamado"}, { "name": "Mail"}, {"name": "Otro"}]
    my_table = table('event_type', column('name', sa.String))
    op.bulk_insert(my_table, event_types)

def downgrade():
    pass
