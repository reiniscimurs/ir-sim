import irsim


# without behavior
world_file="circle_world.yaml"
env = irsim.make(
            world_file, disable_all_plot=False, display=True
        )

for _ in range(100):
    env.step()
    env.render()

env.done()


# without behavior but make step
world_file="circle_world.yaml"
env = irsim.make(
            world_file, disable_all_plot=False, display=True
        )
num_robots = len(env.robot_list)
for _ in range(100):
    act = [[0, 0.1] for _ in range(num_robots)]
    env.step(action_id=[i for i in range(num_robots)], action=act)
    env.render()

env.done()


# with behavior
world_file="circle_world_beh.yaml"
env = irsim.make(
            world_file, disable_all_plot=False, display=True
        )
for _ in range(100):
    env.step()
    env.render()

env.done()