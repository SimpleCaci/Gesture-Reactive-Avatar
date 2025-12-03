ExpressionRules = {

    # ===== WINKS (highest priority) =====
    "catLeftWink.jpg": {
        "all": ["left_wink"],
        "any": [],
        "none": []
    },

    "catRightWink.jpg": {
        "all": ["right_wink"],
        "any": [],
        "none": []
    },

    # ===== BLINK (covers both eyes) =====
    "mmCry.jpg": {
        "all": ["blink"],
        "any": ["frown", "eyebrow_lowered"],
        "none": []
    },

    # ===== LAUGH / TALK / SCREAM =====
    "catLaugh.jpg": {
        "all": ["mouth_open"],
        "any": ["smile", "surprised"],
        "none": ["blink", "left_wink", "right_wink"]
    },

    # ===== SMUG / SMIRK =====
    "catSmirk.jpg": {
        "all": ["smile"],
        "any": ["eyebrow_lowered"],
        "none": ["mouth_open"]
    },

    # ===== SAD =====
    "catSad.jpg": {
        "all": ["frown"],
        "any": [],
        "none": ["mouth_open", "smile"]
    },

    # ===== CUTE STARING / CURIOUS =====
    "catStareCute.jpg": {
        "all": ["eyebrow_raised"],
        "any": [],
        "none": ["mouth_open"]
    },

    # ===== NEUTRAL (fallback) =====
    "catStare.jpg": {
        "all": [],
        "any": [],
        "none": []
    }
}
