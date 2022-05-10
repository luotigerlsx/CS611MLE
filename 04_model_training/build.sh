        'docker', 'build',
        '--tag', f'{destination}:{tag}',
        '--tag', f'{destination}:{commit_hash}',
        '-f', dockerfile,
        '.',

docker build \
  -f dockerfile . \
  --tag yourusername/containerizeml


docker run yourusername/containerizeml \
  --model_file='model.h5' \
  --bucket='gs://helloworld'