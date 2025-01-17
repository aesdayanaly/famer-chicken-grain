from collections import deque

initial_state = {"farmer": "left", "fox": "left", "chicken": "left", "grain": "left"}
goal_state = {"farmer": "right", "fox": "right", "chicken": "right", "grain": "right"}

def is_valid(state):
    if (state["fox"] == "right" and state["chicken"] == "right" and state["farmer"] == "left") or \
       (state["chicken"] == "right" and state["grain"] == "right" and state["farmer"] == "left") or \
       (state["chicken"] == "left" and state["grain"] == "left" and state["farmer"] == "right") or \
       (state["chicken"] == "left" and state["fox"] == "left" and state["farmer"] == "right"):
        return False
    return True

def generate_next_states(state):
    next_states = []
    for item in state:
        if state[item] == state["farmer"]: 
            next_state = state.copy()
            next_state["farmer"] = "right" if state["farmer"] == "left" else "left" 
            next_state[item] = "right" if state[item] == "left" else "left" 
            if is_valid(next_state):
                if (next_state["chicken"] == next_state["grain"] and next_state["farmer"] != next_state["chicken"]) or \
                   (next_state["chicken"] == next_state["fox"] and next_state["farmer"] != next_state["chicken"]):
                    continue
                if item == "farmer":
                    next_states.append((next_state, f"{item} moves to the {next_state[item]}"))
                else:
                    next_states.append((next_state, f"farmer and {item} moves to the {next_state[item]}"))
    return next_states


queue = deque([(initial_state, [])])
visited = set()

while queue:
    current_state, path = queue.popleft()
    if current_state == goal_state:
        print("\nSOLUTION FOUND! \n")
        print("Path:")
        for i, step in enumerate(path):
            print("           ──────────── ⋆⋅☆⋅⋆ ────────────")
            print(f"        Step {i + 1}: {step} \n")

        print("         The farmer, chicken, grain, and fox arrive safely on the right side. \n")
        break
    if tuple(current_state.items()) in visited:
        continue
    visited.add(tuple(current_state.items()))
    next_states = generate_next_states(current_state)
    for next_state, move in next_states:
        queue.append((next_state, path + [move]))
