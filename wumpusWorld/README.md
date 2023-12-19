# wumpusWorld

This project is my attempt to implement a knowledge-ased agent to traverse (and hopefully survive) the Wumpus World.

### Overview 

The WumpusWorld is a well known problem example for the world of AI. It's main topic is with knowledge-based agents. The idea behind these agents is to create some sort of "knowledge" for the agent in some way so that any agent can make inferences similar to the way humans do. This will allow any knowledge-based agents to come up with it's own "conclusions" when deciding what to do next to achieve it's goal. 

For this specific problem, the agents goal is to grab the gold in the cave without dying to the Wumpus monster. In the cave there is a Wumpus that does not move, and several pits as well. If the agent happens to enter the location where the Wumpus is, or similarly, stumble upon the location of a pit, the agent dies. The idea is that the agent can logically "realize" where all these things are (Gold, Wumpus, Pits) by exploring the cave. Certain spots will have a "breeze" indicating there must be a pit in some neighboring location, or a "smell" indicating that the Wumpus is similarly in a neighboring location. The gold simply has a "glitter" in the location it's at, no neighboring indicators or anything. 

These indicators are how the agents will eventually understand that these things are around them, by using the "breeze," "smell," and "glitter" cues. 