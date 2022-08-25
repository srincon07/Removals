#!/bin/bash

source "$PYTHONPATH/activate" && {
    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then
        # createsu
        python manage.py createsu;

    else
        echo "this intance is not the leader";
    fi
}