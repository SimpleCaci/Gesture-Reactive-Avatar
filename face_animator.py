import os
import time

class ExpressionSmoother:
    def __init__(self, hold_time=0.08):
        self.hold_time = hold_time
        self.last_state = None
        self.last_time = time.time()

    def smooth(self, current_state):
        now = time.time()

        if current_state != self.last_state:
            # state changed — only commit if stable long enough
            if now - self.last_time > self.hold_time:
                self.last_state = current_state
            else:
                # ignore flicker, return old state
                return self.last_state
        else:
            # stable state
            self.last_time = now

        return self.last_state


class FaceAnimator:
    def __init__(self, image_folder, rules):
        self.image_folder = image_folder
        self.rules = rules

    def matches(self, state, rule):

        # ALL conditions must be True
        for key in rule.get("all", []):
            if not state.get(key, False):
                return False

        # ANY conditions (if present, at least one must be True)
        any_list = rule.get("any", [])
        if any_list:
            if not any(state.get(k, False) for k in any_list):
                return False

        # NONE conditions must be False
        for key in rule.get("none", []):
            if state.get(key, False):
                return False

        return True

    def select_image(self, state):
        for image_name, rule in self.rules.items():
            if self.matches(state, rule):
                return os.path.join(self.image_folder, image_name)
        return None
