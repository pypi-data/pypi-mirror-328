#!/bin/zsh

source ~/.zshrc

for ver in 3.9 3.10 3.11 3.12 3.13 ; do
  conda create -n pytest_$ver hatch pytest python=$ver -y
  conda activate pytest_$ver
  /bin/rm -f dist/*
  hatch clean
  hatch build
  pip install dist/simplemseed*.whl
  if pytest ; then
    echo python $ver ok
  else
    echo Fail!
    exit 1
  fi

  conda deactivate
  conda env remove -n pytest_$ver -y
done;
