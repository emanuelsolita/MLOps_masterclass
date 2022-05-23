# ml_pipelines/local_deployment.py
# Might be a nice place to use Environment Variables
from azureml.core import Workspace, Model
from azureml.core.model import InferenceConfig
from utils import EnvironmentVariables


env_vars = EnvironmentVariables()
print(env_vars.environment_file)
'''model = Model(workspace, name=env_vars.model_name)
experiment = Experiment(workspace, name=env_vars.experiment_name)

conda_file = 'environment_setup/ci_dependencies.yml'
environment_name = 'my-environment'

try:
    env = Environment.get(ws, name=environment_name)
except Exception:
    assert env_vars.environment_file is not None
    env = Environment.from_conda_specification(
        name=environment_name, file_path=conda_file
    ) '''