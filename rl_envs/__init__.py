from gymnasium.envs.registration import register

register(
    id="rl_envs/GridWorld-v0",
    entry_point="rl_envs.envs:GridWorldEnv",
    max_episode_steps=300,
)

register(
    id="rl_envs/FifteenPuzzle-v0",
    entry_point="rl_envs.envs:FifteenPuzzleEnv",
    max_episode_steps=300,
)
