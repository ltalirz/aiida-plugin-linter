#!/bin/bash
pylint --load-plugins=pylint_aiida --disable=all \
   --enable=custom_raw,aiida-wf-import \
   test.py
