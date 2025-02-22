import json
import os

from grutopia.core.datahub import DataHub
from grutopia.core.gym_env import Env
from grutopia.core.runtime import SimulatorRuntime
from grutopia_extension import import_extensions
from grutopia_extension.agents.util.agent import create_agent

# Run with social navigation agent
file_path = './GRUtopia/demo/configs/h1_social_navigation.yaml'

sim_runtime = SimulatorRuntime(config_path=file_path, headless=True, webrtc=False, native=True)

import_extensions()
# import custom extensions here.

env = Env(sim_runtime)
obs, info = env.reset()
print(f'========INIT OBS{obs}=============')

# init agent
agent = create_agent(sim_runtime=sim_runtime, reset_info=info)
print('========INIT AGENTS=============')
print(f'agent robot_name: {agent.robot_name}')

# init param
i = 0
task_finished = False
metrics_save_path = './results/'
metrics_results = {}
task_name = list(env.active_runtimes.values())[0]

while env.simulation_app.is_running() and not env.finished():
    i += 1
    env_actions = {}
    _actions = DataHub.get_actions_by_task_name(task_name)
    _actions = (
        {_actions['robot']: {a['controller']: a['data'] for a in _actions['controllers']}} if len(_actions) > 0 else {}
    )
    for _robot, _action in _actions.items():
        env_actions = _action

    obs, _, _, _, _ = env.step(action=env_actions)

    # Send obs
    DataHub.set_obs_data(obs)

    # Agent step
    agent.step(obs)
    obs = DataHub.get_obs_data()

    for task in env.runner.current_tasks.values():
        for metric in task.metrics.values():
            metric.update({env._robot_name: obs})
        if task.is_done():
            metrics_results = task.calculate_metrics()
            init_finished = True
            # TODELETE
            metrics_results['normally_end'] = True
            with open(
                os.path.join(
                    metrics_save_path,
                    task.runtime.scene_asset_path.split('/')[-2]
                    + '_'
                    + '_'.join(task.runtime.extra['target'].split('/'))
                    + str(task.runtime.extra['episode_idx'])
                    + '.json',
                ),
                'w',
            ) as f:
                f.write(json.dumps(metrics_results))

    if task_finished:
        env.close()

    if i % 1000 == 0:
        print(i)

env.close()
