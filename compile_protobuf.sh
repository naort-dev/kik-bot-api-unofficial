#!/bin/bash
set -e
files=$(find protobuf_source -name '*.proto')
protoc -I protobuf_source $files --python_out=kik_unofficial/protobuf
generated_files=$(find kik_unofficial/protobuf -name '*_pb2.py')
echo $generated_files
sed -i 's/^import \([^ ]*\)_pb2 as \([^ ]*\)$/import kik_unofficial.protobuf.\1_pb2 as \2/'  $generated_files
sed -i 's/^from \([^ ]*\) import \([^ ]*\)_pb2 as \([^ ]*\)$/from kik_unofficial.protobuf.\1 import \2_pb2 as \3/' $generated_files
echo Done.
