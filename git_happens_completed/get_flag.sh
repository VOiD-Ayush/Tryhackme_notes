#!/bin/bash

git show 395e087334d613d5e423cdf8f7be27196a360459 | grep "password ===" | cut -d '"' -f 2