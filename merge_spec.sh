#!/usr/bin/bash

# Run this file to update the spec directory. All changes are overwritten!

remote_name="nulecule-spec"
remote_branch="master"
remote_url="https://github.com/projectatomic/nulecule"

if ! git remote | grep -q $remote_name; then
    git remote add -f -t $remote_branch --no-tags $remote_name $remote_url
fi

git merge -s ours --no-commit $remote_name/$remote_branch
git rm -rf spec/ 2> /dev/null
git read-tree --prefix=spec/ -u $remote_name/$remote_branch:spec/
git commit -m 'Merged latest spec'

