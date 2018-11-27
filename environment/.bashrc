export PS1="___________________________________________________________________________________________________\n| \[\e[32m\]\u \[\e[0m\]on \h in \[\e[33m\]\w \[\e[0m\]- \[\e[31m\]\@ \[\e[0m\] \n| => "
export PS2="| => "

export EDITOR=code


f [ -d ~/.bash_functions ]; then
    for file in ~/.bash_functions/*; do
        . "$file"
    done
fi