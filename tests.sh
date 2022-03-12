#!/bin/bash

usage(){
   echo "Usage: $0 [-h] [run_all] [run_seq_gen_tests] [run_db_tests]"
    echo "  -h  Help. Display this message and quit."
    echo "  run_all - Run all tests"
    echo "  run_seq_gen_tests - Run tests of random number sequence generator"
    echo "  run_db_tests - Run tests of database"
    exit
}

run_all(){
  python3 -m unittest -v tests/test_*.py
}

run_seq_gen_tests(){
  python3 -m unittest -v tests/test_rand*.py
}

run_db_tests(){
  python3 -m unittest -v tests/test_db*.py
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
            run_all
            exit 0
            ;;
        run_seq_gen_tests)
            run_seq_gen_tests
            exit 0
            ;;
        run_db_tests)
            run_db_tests
            exit 0
            ;;
    esac
done