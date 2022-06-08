from experiments.fullExperiment import *


import environments.RegisterEnvironments as bW
import learners.discreteMDPs.UCRL3 as le
import learners.discreteMDPs.PSRL as psrl
import learners.discreteMDPs.IRL as IRL
import learners.Generic.Qlearning as ql
import learners.Generic.Random as random

# To get the list of registered environments:
#print("List of registered environments: ")
#[print(k) for k in bW.registerWorlds.keys()]




# env = bW.makeWorld(bW.registerWorld('ergo-river-swim-6'))
env = bW.makeWorld(bW.registerWorld('river-swim-6'))
# env = bW.makeWorld(bW.registerWorld('grid-2-room'))
# env = bW.makeWorld(bW.registerWorld('grid-4-room'))
# env = bW.makeWorld(bW.registerWorld('river-swim-25'))
# env = bW.makeWorld(bW.registerWorld('ergo-river-swim-25'))
# env = bW.makeWorld(bW.registerWorld('grid-random-88'))
# env = bW.makeWorld(bW.registerWorld('grid-random-1212'))
# env = bW.makeWorld(bW.registerWorld('grid-random-1616'))
# env = bW.makeWorld(bW.registerWorld('random-rich'))
# env = bW.makeWorld(bW.registerWorld('ergodic-random-rich'))
# env = bW.makeWorld(bW.registerWorld('nasty'))

agents = []
nS = env.observation_space.n
nA = env.action_space.n
delta=0.05
agents.append(([IRL.IRL, {"nbr_states":nS, "nbr_actions":nA}]))
agents.append( [psrl.PSRL, {"nS":nS, "nA":nA, "delta":delta}])
# agents.append( [random.Random, {"env": env.env}])

agents.append( [le.UCRL3_lazy, {"nS":nS, "nA":nA, "delta":delta}])
agents.append( [ql.Qlearning, {"nS":nS, "nA":nA}])

#######################
# Run a full experiment
#######################
runLargeMulticoreExperiment(env, agents, timeHorizon=5000, nbReplicates=256)

#######################
# Plotting Regret directly from dump files of past runs:
#######################
#files =plR.search_dump_cumRegretfiles("RiverSwim-6-v0")
#plR.plot_results_from_dump(files, 500)

