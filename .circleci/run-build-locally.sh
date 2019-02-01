#!/usr/bin/env bash
curl --user ${CIRCLE_TOKEN}: \
    --request POST \
    --form revision=daca2b7c7d089d0d3c3c3ebd4bde2300c4f3dde0\
    --form config=@config.yml \
    --form notify=false \
        https://circleci.com/api/v1.1/project/github/tcbegley/dash-google-charts/tree/master
