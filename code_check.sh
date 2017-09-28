#!/bin/bash
pylintrc_file=.pylintrc
pylint_disable_file=.pylint_disable

function create_pylint_ignore_string {
    file=$1
    pylint_ignore_string=""

    while IFS= read -r ignore_entry
    do
        clean_entry=$(echo "$ignore_entry" | cut -d '#' -f1 | tr -d '[:space:]')
        [ "$clean_entry" == "" ] && continue

        [ "$pylint_ignore_string" != "" ] && pylint_ignore_string="$pylint_ignore_string,"
        pylint_ignore_string="$pylint_ignore_string$clean_entry"
    done < "$file"
    echo "$pylint_ignore_string"
}

which pylint
RC=$?

[ "$RC" != "0" ] && echo "Please install pylint" && exit 1

disable_list=$(create_pylint_ignore_string $pylint_disable_file)
echo Disabled: $disable_list
find . -name "*.py" -print0 | xargs -0 pylint --rcfile=.pylintrc --disable="$disable_list"
