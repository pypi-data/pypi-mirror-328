import asyncio

from pantheon.agent import Agent
from pantheon.repl.meeting import Repl
from pantheon.meeting import UserCentricMeeting


biologist = Agent(
    name="biologist",
    instructions="You will consider the user's question through the lens of a biologist.",
    model="gpt-4o-mini",
)

computer_scientist = Agent(
    name="computer_scientist",
    instructions="You will consider the user's question through the lens of a computer scientist.",
    model="gpt-4o-mini",
)


meeting = UserCentricMeeting([biologist, computer_scientist])
repl = Repl(meeting)

asyncio.run(repl.run())
