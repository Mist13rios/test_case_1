#!/bin/bash

set -e

chown -R $SYSTEM_USER:$SYSTEM_GROUP /var/www/logs

gosu $SYSTEM_USER bash -c " source /var/www/env/bin/activate && alembic upgrade head"

case "$1" in
    gunicorn|python)
        set -- gosu $SYSTEM_USER bash -c "source /var/www/env/bin/activate && $*"
    ;;
esac

exec "$@"
