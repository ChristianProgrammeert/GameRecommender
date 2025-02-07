INSERT INTO genres (id, name, rage_inducing, action_packed, multiplayer, description) VALUES
(1, 'Action', False, True, False, 'Fast-paced games with combat and movement challenges.'),
(2, 'RPG', False, False, False, 'Role-playing games with character progression and story-driven gameplay.'),
(3, 'Platformer', False, True, False, 'Games focused on jumping, running, and precise movement.'),
(4, 'FPS', False, True, True, 'First-person shooters emphasizing gunplay and reflexes.'),
(5, 'Horror', True, False, False, 'Games designed to create fear and tension.'),
(6, 'MOBA', True, True, True, 'Multiplayer Online Battle Arena with strategy-based team fights.'),
(7, 'Puzzle', False, False, False, 'Games that require problem-solving skills.'),
(8, 'Sandbox', False, False, True, 'Open-ended games with creative freedom.'),
(9, 'Simulation', False, False, False, 'Games that simulate real-world or fantasy activities.');

INSERT INTO games (id, name, mature_themes, open_world, skill_based, length_in_hours, description) VALUES
(1, 'Dark Souls', True, False, True, 50, 'A punishing action RPG known for its difficulty, deep lore, and rewarding combat.'),
(2, 'The Witcher 3', True, True, False, 100, 'An open-world RPG with rich storytelling, deep choices, and immersive combat.'),
(3, 'Celeste', False, False, True, 10, 'A challenging platformer about climbing a mountain, featuring tight controls and a touching story.'),
(4, 'Doom Eternal', True, False, True, 20, 'A fast-paced FPS focused on brutal combat, mobility, and intense action.'),
(5, 'Valorant', False, False, True, NULL, 'A tactical FPS where teams compete in strategic gunfights with unique agent abilities.'),
(6, 'Resident Evil 2', True, False, False, 15, 'A survival horror remake with tense atmosphere, puzzles, and limited resources.'),
(7, 'Tetris', False, False, True, NULL, 'A timeless puzzle game where players arrange falling blocks to clear lines.'),
(8, 'Minecraft', False, True, False, NULL, 'A sandbox game where players explore, build, and survive in an infinite blocky world.'),
(9, 'Stardew Valley', False, True, False, 50, 'A relaxing farming simulator with RPG elements, crafting, and community building.'),
(10, 'Baldur’s Gate 3', True, True, False, 100, 'A deep RPG with turn-based combat, rich storytelling, and vast player choices.');

INSERT INTO games_genres (game_id, genre_id) VALUES
(1, 1), (1, 2),   -- Dark Souls: Action, RPG
(2, 1), (2, 2),   -- The Witcher 3: Action, RPG
(3, 3),                             -- Celeste: Platformer
(4, 1), (4, 4),   -- Doom Eternal: Action, FPS
(5, 1), (5, 4),   -- Valorant: FPS, Action
(6, 5), (6, 1),   -- Resident Evil 2: Horror, Action
(7, 7),                             -- Tetris: Puzzle
(8, 8), (8, 9),   -- Minecraft: Sandbox, Simulation
(9, 9), (9, 2),   -- Stardew Valley: Simulation, RPG
(10, 2), (10, 1);  --Baldur's Gate 3: RPG, Action & Open Worl
