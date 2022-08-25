#!/bin/bash

source "$PYTHONPATH/activate" && {
    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then
        # collectstatic
        python manage.py collectstatic --noinput;

    else
        echo "this intance is not the leader";
    fi
}