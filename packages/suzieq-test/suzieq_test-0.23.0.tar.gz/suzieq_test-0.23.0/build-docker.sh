#!/usr/bin/env bash

VERSION=$(python -c "exec(open('suzieq/version.py').read())")
echo "Building image ddutt/suzieq:$VERSION"
if [ $# -eq 0 ]; then
    docker build --build-arg SUZIEQ_VERSION=$VERSION -t ddutt/suzieq:$VERSION -t ddutt/suzieq:latest -t netenglabs/suzieq:$VERSION -t netenglabs/suzieq:latest .
else
    docker build --build-arg SUZIEQ_VERSION=$VERSION -t ddutt/suzieq:$VERSION -t netenglabs/suzieq:$VERSION .
fi
