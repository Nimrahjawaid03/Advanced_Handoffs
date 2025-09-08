from agents import Agent, Runner, handoff
import asyncio
from connection import config

billing_agent = Agent(
    name="Billing Agent",
    instructions="Aap sirf billing sey related sawallon ke jawab dengey."
)

refund_agent = Agent(
    name="Refund Agent",
    instructions="Aap sirf refund process kerney mein madad karengy."
)

custom_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="custom_refund_tool",
    tool_description_override="Handle user refund requests with extra care."
)

damage_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="damage_refund_tool",
    tool_description_override="Handle refund due to damage item."
)

late_delivery_refund_handoff = handoff(
    agent=refund_agent,
    tool_name_override="late_delivery_refund_tool",
    tool_description_override="Handle refund due to late delivery."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Aap user ki request perhein or decide karein k kis agent ko ye kaam dena hai.",
    handoffs=[billing_agent, custom_refund_handoff, damage_refund_handoff, late_delivery_refund_handoff]
)

async def main():
    result = await Runner.run(triage_agent,
        "My order arrived 10 days late. I want a refund.",
        run_config=config)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())