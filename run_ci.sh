js_test=$(docker ps -a -f exited=1 -q | wc -l | tr -d ' ')
docker-compose exec -T api sh -c 'python manage.py test; (exit $?)'
py_test=$?
echo $js_test
echo $py_test

docker-compose down

if [[ $js_test == 0 && $py_test == 0 ]]; then
    exit 0
fi
exit 1
