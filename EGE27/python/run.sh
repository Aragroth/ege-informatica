#!/bin/bash
name=$(basename $1 .rs)
rustc $@ && ./$name && rm $name
