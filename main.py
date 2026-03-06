import os
import random

primaries = [
    {
        "name": "AR-23 Liberator",
        "tags": ["assault_rifle", "default"]
    },
    {
        "name": "AR-23P Liberator Penetrator",
        "tags": ["assault_rifle", "helldivers_mobilize"]
    },
    {
        "name": "AR-23C Liberator Concussive",
        "tags": ["assault_rifle", "steeled_veterans"]
    },
    {
        "name": "StA-52 Assault Rifle",
        "tags": ["assault_rifle", "righteous_revenants"]
    },
    {
        "name": "AR-32 Pacifier",
        "tags": ["assault_rifle", "force_of_law"]
    },
    {
        "name": "AR-2 Coyote",
        "tags": ["assault_rifle", "dust_devils"]
    },
    {
        "name": "MA5C Assault Rifle",
        "tags": ["assault_rifle", "obedient_democracy_support_troopers"]
    },
    {
        "name": "AR-23A Liberator Carbine",
        "tags": ["assault_rifle", "viper_commandos"]
    },
    {
        "name": "AR-61 Tenderizer",
        "tags": ["assault_rifle", "polar_patriots"]
    },
    {
        "name": "BR-14 Adjudicator",
        "tags": ["assault_rifle", "democratic_detonation"]
    },
    {
        "name": "AR/GL-21 One-Two",
        "tags": ["assault_rifle", "python_commandos"]
    },
    {
        "name": "AR-59 Suppressor",
        "tags": ["assault_rifle", "redacted_regiment"]
    },
    {
        "name": "R-2 Amendment",
        "tags": ["marksman_rifle", "masters_of_ceremony"]
    },
    {
        "name": "R-2124 Constitution",
        "tags": ["marksman_rifle", "liberty_day"]
    },
    {
        "name": "R-6 Deadeye",
        "tags": ["marksman_rifle", "borderline_justice"]
    },
    {
        "name": "R-63 Diligence",
        "tags": ["marksman_rifle", "helldivers_mobilize"]
    },
    {
        "name": "R-63CS Diligence Counter Sniper",
        "tags": ["marksman_rifle", "helldivers_mobilize"]
    },
    {
        "name": "R-72 Censor",
        "tags": ["marksman_rifle", "redacted_regiment"]
    },
    {
        "name": "MP-98 Knight",
        "tags": ["submachine_gun", "super_citizen_edition"]
    },
    {
        "name": "StA-11 SMG",
        "tags": ["submachine_gun", "righteous_revenants"]
    },
    {
        "name": "M7S SMG",
        "tags": ["submachine_gun", "obedient_democracy_support_troopers"]
    },
    {
        "name": "SMG-32 Reprimand",
        "tags": ["submachine_gun", "truth_enforcers"]
    },
    {
        "name": "SMG-37 Defender",
        "tags": ["submachine_gun", "helldivers_mobilize"]
    },
    {
        "name": "SMG-72 Pummeler",
        "tags": ["submachine_gun", "polar_patriots"]
    },
    {
        "name": "SG-8 Punisher",
        "tags": ["shotgun", "helldivers_mobilize"]
    },
    {
        "name": "SG-8S Slugger",
        "tags": ["shotgun", "helldivers_mobilize"]
    },
    {
        "name": "SG-20 Halt",
        "tags": ["shotgun", "truth_enforcers"]
    },
    {
        "name": "SG-451 Cookout",
        "tags": ["shotgun", "freedom's flame"]
    },
    {
        "name": "DBS-2 Double Freedom",
        "tags": ["shotgun", "superstore"]
    },
    {
        "name": "M90A Shotgun",
        "tags": ["shotgun", "obedient_democracy_support_troopers"]
    },
    {
        "name": "SG-225 Breaker",
        "tags": ["shotgun", "helldivers_mobilize"]
    },
    {
        "name": "SG-22SP Breaker Spray&Pray",
        "tags": ["shotgun", "helldivers_mobilize"]
    },
    {
        "name": "SG-225IE Breaker Incendiary",
        "tags": ["shotgun", "steeled_veterans"]
    },
    {
        "name": "CB-9 Exploding Crossbow",
        "tags": ["explosive", "democratic_detonation"]
    },
    {
        "name": "R-36 Eruptor",
        "tags": ["explosive", "democratic_detonation"]
    },
    {
        "name": "SG-8P Punisher Plasma",
        "tags": ["energy_based", "cutting_edge"]
    },
    {
        "name": "PLAS-39 Accelerator Rifle",
        "tags": ["energy_based", "righteous_revenants"]
    },
    {
        "name": "ARC-12 Blitzer",
        "tags": ["energy_based", "cutting_edge"]
    },
    {
        "name": "LAS-5 Scythe",
        "tags": ["energy_based", "helldivers_mobilize"]
    },
    {
        "name": "LAS-16 Sickle",
        "tags": ["energy_based", "cutting_edge"]
    },
    {
        "name": "Las-17 Double-Edge Sickle",
        "tags": ["energy_based", "servants_of_freedom"]
    },
    {
        "name": "PLAS-1 Scorcher",
        "tags": ["energy_based", "helldivers_mobilize"]
    },
    {
        "name": "PLAS-101 Purifier",
        "tags": ["energy_based", "polar_patriots"]
    },
    {
        "name": "LAS-13 Trident",
        "tags": ["energy_based", "siege_breakers"]
    },
    {
        "name": "VG-70 Variable",
        "tags": ["special", "control_group"]
    },
    {
        "name": "FLAM-66 Torcher",
        "tags": ["special", "freedom's flame"]
    },
    {
        "name": "JAR-5 Dominator",
        "tags": ["special", "steeled_veterans"]
    }
]

def get_random(items, selected_tags):
    pool = [item for item in items if all(tag in item["tags"] for tag in selected_tags)]
    if not pool:
        return None
    return random.choice(pool)

if __name__ == "__main__":
    #example of syntax needed for randomly pulling from large datastructure with tags
    #selected_tags = ["helldivers_mobilize"]
    #items = primaries
    #print (get_random(items, selected_tags)["name"])