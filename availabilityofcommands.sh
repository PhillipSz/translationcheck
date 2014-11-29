#!/bin/bash

checkcommands (){
# check availability of commands on the system

my_needed_commands="grep wget tail head egrep" 

missing_counter=0
for needed_command in $my_needed_commands; do
  if ! hash "$needed_command" >/dev/null 2>&1; then
    printf "Command not found in PATH: %s\n" "$needed_command" >&2
    ((missing_counter++))
  fi
done

if ((missing_counter > 0)); then
  printf "Minimum %d commands are missing in PATH, aborting\n" "$missing_counter" >&2
  exit 1
fi
}

checkcommands
