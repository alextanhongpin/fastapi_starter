from alembic.config import Config
from alembic import command, autogenerate
from alembic.script import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext


def run_migrations(engine):
    metadata = None
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "migrations")

    alembic_script = ScriptDirectory.from_config(alembic_cfg)
    alembic_env = EnvironmentContext(alembic_cfg, alembic_script)

    conn = engine.connect()
    alembic_env.configure(connection=conn, target_metadata=metadata)

    def do_upgrade(revision, context):
        return alembic_script._upgrade_revs(alembic_script.get_heads(), revision)

    alembic_env.configure(connection=conn, target_metadata=metadata, fn=do_upgrade)

    with alembic_env.begin_transaction():
        alembic_env.run_migrations()
