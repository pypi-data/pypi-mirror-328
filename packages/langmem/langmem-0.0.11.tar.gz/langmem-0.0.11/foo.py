#%%
# %load_ext autoreload
# %autoreload 2
#%%
import asyncio

from langmem import create_memory_manager

async def main():
    manager = create_memory_manager("openai:o3-mini", enable_deletes=True)

    conversation = [
        {"role": "user", "content": "I prefer dark mode in all my apps"},
        {"role": "assistant", "content": "I'll remember that preference"},
    ]

    # Extract memories from conversation
    memories = await manager.ainvoke({"messages": conversation, "max_steps": 4})
    #%%
    import langsmith as ls
    new_conversation = [
        {"role": "user", "content": "Actually i like light mode in some things like dev tools."},
        {"role": "assistant", "content": "Bad choice."},
        {"role": "user", "content": "Don't speak back to me >:("},
    ]
    with ls.trace("extract"):
        memories = await manager.ainvoke({"messages": new_conversation, "max_steps": 4, "existing": memories})
    # %%
asyncio.run(main())