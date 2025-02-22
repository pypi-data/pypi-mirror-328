> Update
```bash
...do changes...
git commit -m "Version 1.0.1"
git tag v1.0.1
git push origin v1.0.1
```


> Build
```bash
hatch build
```

This creates:
```bash
dist/
│── spida_api-1.0.1.tar.gz
│── spida_api-1.0.1-py3-none-any.whl
```

> login to AWS CodeArtifact
```bash
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain techserv \
  --domain-owner 066767799640 \
  --query authorizationToken \
  --output text --region us-east-1)
```

> Make sure twine is installed
```bash
pip install twine
```

> Push
```bash
twine upload \
  --repository-url https://techserv-066767799640.d.codeartifact.us-east-1.amazonaws.com/pypi/spida_api/ \
  -u aws \
  -p $CODEARTIFACT_AUTH_TOKEN \
  dist/*
```