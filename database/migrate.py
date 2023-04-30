from alembic.config import Config
from alembic.runtime.environment import EnvironmentContext
from alembic.script import ScriptDirectory


def run_migrations(engine):
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "migrations")

    alembic_script = ScriptDirectory.from_config(alembic_cfg)
    alembic_env = EnvironmentContext(alembic_cfg, alembic_script)

    conn = engine.connect()
    alembic_env.configure(connection=conn, target_metadata=None)

    def do_upgrade(revision, context):
        heads = alembic_script.get_heads()
        return alembic_script._upgrade_revs(heads, revision)

    alembic_env.configure(connection=conn, target_metadata=None, fn=do_upgrade)

    with alembic_env.begin_transaction():
        alembic_env.run_migrations()
