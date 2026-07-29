# buckshot-roulette
we finna do some machine learning or some sort of algo to get bots in the real game






# ROADMAP

**Phase 1 — Foundations (done / near-done)**
- [x] `Shotgun` (chambers, rack, reload)
- [x] Fix `player.py` naming conflict → single `self.inventory`
- [x] Fix `items.py` enum syntax
- [x] Fix `main.py` missing constructor arg

**Phase 2 — Items (ABC, inheritance, factory)**
- [ ] `Item` abstract base — one method: `use(user, target, game)`
- [ ] All 9 subclasses (Cigarettes, Magnifying Glass, Beer, Phone, Inverter, Saw, Adrenaline)
- [ ] `ItemBox` — dict-based factory, teaches "factory pattern" as literally just a dict + one method

**Phase 3 — Player (teach: encapsulation)**
- [ ] health/damage
- [ ] `inventory: list[Item]`, capped size
- [ ] `add_item` / `remove_item`

**Phase 4 — Game (teach: composition, "who owns what")**
- [ ] owns `players`, `shotgun`, `itembox`
- [ ] turn order + direction (needed for Remote)
- [ ] round/reload logic
- [ ] win condition check

**Phase 5 — RL-readiness (the actual point of the project)**
- [ ] fixed `Action` enum (shoot self, shoot opp, use item 1–9)
- [ ] `Game.step(action) -> (observation, reward, done, info)` — gym-shaped
- [ ] separate `Observation` (what a player can see) from ground-truth `Shotgun.chambers`

# Dependencies

- Game
    - Shotgun
    - Player
        - Holds Items
    - Itembox
        - Creates Items
    - Items
        - use method
            - user
            - target
            - game

