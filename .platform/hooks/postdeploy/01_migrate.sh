#!/bin/bash

source "$PYTHONPATH/activate" && {
    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then
        # log which migrations have already been applied
        python manage.py showmigrations;

        # migrate
        python manage.py migrate --noinput;

        # createsu
        python manage.py createsu;

        # collectstatic
        python manage.py collectstatic --noinput;

    else
        echo "this intance is not the leader";
    fi
}