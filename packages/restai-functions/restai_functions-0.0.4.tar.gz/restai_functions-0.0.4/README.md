# restai-functions

Call RESTai projects like functions in Python

## Usage

### Create a RESTai Project
<div align="center">
  <img src="https://raw.githubusercontent.com/apocas/restai-functions/master/readme/assets/project.png"  alt="RESTai Project" width="50%"/>
</div>

### Install
```bash
pip install restai-functions
```

### Example
```python
from restai_functions import Restai

restai = Restai(url=os.environ.get("RESTAI_URL"), api_key=os.environ.get("RESTAI_KEY"))

print(restai.yoda_speak("Hi I'm Pedro"))

```
