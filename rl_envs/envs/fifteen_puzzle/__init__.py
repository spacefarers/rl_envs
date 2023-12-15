from gymnasium.envs.registration import register

register(
     id="FifteenPuzzle-v0",
     entry_point="envs:GridWorldEnv",
     max_episode_steps=300,
)