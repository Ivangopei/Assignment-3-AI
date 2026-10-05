#!/usr/bin/env python
"""
Tournament Agent: Scilur
Student: Ivan Gopei
Generated: 2026-10-04 21:08:04

Evolution Details:
- Generations: 100
- Final Fitness: N/A
- Trained against: Random (0.7), Tit-for-Tat, Always Invest, Hard Majority, Prober...

Strategy: No mercy, no fear
"""

from agents import Agent, INVEST, UNDERCUT
import random


class IvanGopeiAgent(Agent):
    """
    Scilur

    No mercy, no fear

    Evolved Genes: [0.8014849888207329, 1.0, 0.9785192339640734, 0.4728080550680513, 0.47832914147859534, 0.8743497161749513]
    """

    def __init__(self):
        # These genes were evolved through 100 generations
        self.genes = [0.8014849888207329, 1.0, 0.9785192339640734, 0.4728080550680513, 0.47832914147859534, 0.8743497161749513]

        # Required for tournament compatibility
        self.student_name = "Ivan Gopei"

        super().__init__(
            name="Scilur",
            description="No mercy, no fear"
        )

    def choose_action(self) -> bool:
        if self.round_num == 0 or len(self.history) == 0:
            return INVEST if self.genes[0] > 0.5 else UNDERCUT

        memory_length = max(1, int(self.genes[4] * 10) + 1)
        recent_history = self.history[-memory_length:]
        cooperation_rate = sum(recent_history) / len(recent_history)

        if len(self.history) >= 5 and cooperation_rate < self.genes[5] * 0.5:
            return UNDERCUT

        opp_last = self.history[-1]

        if opp_last == INVEST:
            loyalty = 0.85 + 0.15 * self.genes[1]
            return INVEST if random.random() < loyalty else UNDERCUT

        defected_twice = len(self.history) >= 2 and self.history[-2] == UNDERCUT

        if defected_twice or random.random() < self.genes[2]:
            if random.random() < self.genes[3] * 0.3:
                return INVEST
            return UNDERCUT

        return INVEST



# Convenience function for tournament loading
def get_agent():
    """Return an instance of this agent for tournament use"""
    return IvanGopeiAgent()


if __name__ == "__main__":
    # Test that the agent can be instantiated
    agent = get_agent()
    print(f"✅ Agent loaded successfully: {agent.name}")
    print(f"   Genes: {agent.genes}")
    print(f"   Description: {agent.description}")
