#!/bin/bash

function parse_worker_max() {
    uwsgi_config=api/uwsgi.ini
    worker_max=$(cat "$uwsgi_config" | grep "processes" | cut -d= -f2 | tr -d '[:space:]')
    echo "$worker_max"
}

function get_worker() {
    worker=$(docker-compose exec api sh -c "ps -eF | grep 'uwsgi \-\-ini' | wc -l")
    [[ ! ( -z "$worker" || "$worker" == "" ) ]] && worker=${worker::-1} || worker=0
    echo "$worker"
}

worker_max=$(parse_worker_max)
worker=$(get_worker)

until [[ "$worker" -eq "$worker_max" ]]
do
    worker=$(get_worker)
    echo "Waiting for api container"
done
