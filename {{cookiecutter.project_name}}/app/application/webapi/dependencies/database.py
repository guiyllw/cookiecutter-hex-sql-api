from infrastructure.common.database import DBSession  # Base


def resolve_db_session():
    # Base.metadata.create_all()
    return DBSession()
