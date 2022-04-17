#!/bin/bash

usage(){
   echo "Usage: $0 [-h] [run_all [seed]|NULL] [run_seq_gen_tests [seed]|NULL] [run_db_tests [seed]|NULL]"
    echo "  -h  Help. Display this message and quit."
    echo "  run_all - Run all tests"
    echo "  run_seq_gen_tests - Run tests of random number sequence generator"
    echo "  run_db_tests - Run tests of database"
    exit
}

run_all(){
  if [ "$1" ]; then
      python3 -m unittest -v tests/test_*.py "$1"
      else python3 -m unittest -v tests/test_*.py
  fi
}

run_seq_gen_tests(){
  if [ "$1" ]; then
      python3 -m python3 -m unittest -v tests/test_rand*.py "$1"
      else python3 python3 -m unittest -v tests/test_rand*.py
  fi
  ls
  rm -f ./test_db_file.db
  rm -f ./US_Cities.txt
}

run_db_tests(){
  if [ "$1" ]; then
      python3 -m unittest -v tests/test_db*.py "$1"
      else python3 -m unittest -v tests/test_db*.py
  fi
}

remove_file(){
   rm -f ./test_db_file.db
   rm -f ./US_Cities.txt
}

if (( $# == 0 ))
then
    usage
fi

while (( $# > 0 ))
do
    opt="$1"
    shift

    case $opt in
        -h)
            usage
            exit 0
            ;;
        run_all)
            run_all "$1"
            remove_file
            exit 0
            ;;
        run_seq_gen_tests)
            run_seq_gen_tests "$1"
            exit 0
            ;;
        run_db_tests)
            run_db_tests "$1"
            remove_file
            exit 0
            ;;
    esac
done