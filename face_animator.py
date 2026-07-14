import os
import time


class ExpressionSmoother:
    def __init__(self, hold_time=0.08):
        self.hold_time = hold_time
        self.reset()

    def reset(self):
        self.last_state = None
        self.pending_state = None
        self.pending_since = time.time()

    def smooth(self, current_state):
        if self.last_state is None:
            self.last_state = current_state
            return current_state

        now = time.time()
        if current_state != self.pending_state:
            self.pending_state = current_state
            self.pending_since = now

        if current_state != self.last_state and now - self.pending_since >= self.hold_time:
            self.last_state = current_state

        return self.last_state


class FaceAnimator:
    def __init__(self, image_folder, rules):
        self.image_folder = image_folder
        self.rules = rules

    def matches(self, state, rule):
        state = state or {}

        for key in rule.get("all", []):
            if not state.get(key, False):
                return False

        any_list = rule.get("any", [])
        if any_list and not any(state.get(key, False) for key in any_list):
            return False

        for key in rule.get("none", []):
            if state.get(key, False):
                return False

        return True

    def select_image(self, state):
        for image_name, rule in self.rules.items():
            if self.matches(state, rule):
                return os.path.join(self.image_folder, image_name)
        return None
