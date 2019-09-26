#!/bin/bash

set -e

chown -R $SYSTEM_USER:$SYSTEM_GROUP /var/www/logs

if [[ "$1" = 'gunicorn' || "$3" == 'runserver' ]]; then
    gosu $SYSTEM_USER bash -c "\
        source /var/www/env/bin/activate &&"
#        touch /var/www/logs/{gunicorn.access.log, gunicorn.error.log, debug.log, order_processing.log}"
#        python app.py migrate && \
fi

#tail -n 0 -f /var/www/logs/*.log &

case "$1" in
    gunicorn|python)
        set -- gosu $SYSTEM_USER bash -c "source /var/www/env/bin/activate && $*"
    ;;
esac

exec "$@"
