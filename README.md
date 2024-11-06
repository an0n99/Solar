**THIS IS A PURELY EDUCATIONAL RESEARCH PAPER INTO THE EFFECTIVENESS OF ANTI-CHEATS AND HOW AI MODELS ARE DISRUPTING THIS**

# Solar
Solar Demonstration Model is built upon the [Flare](https://github.com/zeyad-mansour/lunar) object detection model. 

## How Does Aimbot Work?

Aimbots are software programs or modifications used to give players an unfair advantage in competitive video games by automating the aiming process. Typically, aimbots aim automatically at opponents, often with pixel-perfect precision, making it easier for players to score headshots or eliminate enemies without relying on their own aiming skills. To understand how aimbots work, it's essential to explore the different techniques and technologies they use.

# Memory Access and Manipulation:
One of the most common methods aimbots use is memory manipulation. Video games store key data like player positions, health, and other important in-game variables in the computer’s memory (RAM). Aimbots can gain access to this memory to retrieve critical information about enemy locations and game states. Here's how it typically works:

Memory Scanning: Aimbots scan the game's memory for relevant data structures, such as coordinates of enemy players, weapon stats, or aiming mechanics.
Memory Editing: Once the aimbot locates this data, it can modify or read it in real-time to adjust the player's aim toward enemies, even if the player isn't looking in their direction.
By manipulating memory, aimbots can programmatically move the player's crosshair towards opponents with high accuracy, even beyond what a normal player could achieve with manual aiming.

# Game Memory Injection and DLL Injection:
DLL (Dynamic Link Library) injection is another method aimbots use to hook into a game. This involves the aimbot inserting a custom DLL file into the game's memory space, which allows the aimbot to execute code within the game's process. The injected DLL is typically responsible for:

Reading Game Data: As with memory manipulation, it can read data from the game's memory, including enemy positions and other player-related data.
Modifying Aiming or Movement: The DLL can also modify the player's in-game actions, such as altering the mouse input, changing the view angle, or moving the player's crosshair automatically to target enemies.
DLL injection is more sophisticated than memory manipulation alone because it allows the aimbot to interact directly with the game code, making it harder for basic anti-cheat systems to detect.

## How Do Anti-Cheats Detect Aimbot?
# Memory Scanning: 
One of the primary methods anti-cheat systems use to detect memory manipulation is by scanning the game’s memory during runtime. These scans focus on identifying unusual patterns or modifications in the game's memory space, which could indicate that a cheat is active.

Memory Integrity Checks: Anti-cheat systems periodically scan the memory of running games for anomalies, such as unfamiliar code or data structures that do not match the expected values. This helps detect unauthorized memory injections or changes to in-game variables that would be manipulated by an aimbot.

Behavioral Analysis: Anti-cheats may also monitor the behavior of the game in memory. For example, if player data such as enemy positions or player coordinates are being altered or read by processes outside of the standard game flow, it can trigger an alert. This is especially effective for detecting cheats that access and modify game memory in real-time.

Signature Matching: Anti-cheat systems can compare memory data to a database of known cheat signatures. These signatures are patterns that have been identified from known cheats (e.g., aimbots or wallhacks). If the memory access pattern matches an entry in the cheat database, the system flags the activity as suspicious.

# DLL Injection Detection:
DLL injection is one of the most common techniques used by aimbots to manipulate a game’s behavior. Anti-cheat systems have several methods to detect DLL injections:

Monitoring Processes and Modules: Anti-cheats constantly monitor the game's processes for unexpected DLLs. If a game process loads a DLL that is not part of the game's standard files, the anti-cheat system can identify and flag it. This includes third-party DLLs injected into the game’s memory by cheats.

Checking for Unusual Function Calls: When a DLL is injected into a game, it may alter or hook into game functions (such as rendering or input functions). Anti-cheat systems can monitor for unusual function calls or memory hooks that are not part of the original game code. If the system detects a hook or function modification that is not part of the legitimate game engine, it can flag it as a cheat.

# File Hashing and Integrity Checks:
File integrity checking is one of the most common and effective methods used to detect file manipulation, which is often employed by cheats to modify or replace game assets (e.g., to inject cheat code or alter game files).

File Hashing: Anti-cheat systems use cryptographic hash functions (such as MD5, SHA-1, or SHA-256) to compute a hash for each critical game file (e.g., executables, DLLs, assets, and configuration files). When the game is launched, the anti-cheat system compares the hash of each file with a stored reference value. If a file’s hash does not match the expected value, it is flagged for potential modification.

File Integrity Enforcement: Anti-cheat systems may implement runtime checks to enforce file integrity. For example, if a player has altered or replaced a game’s executable or assets with a modified version (such as aimbot code or other cheats), the anti-cheat system will detect discrepancies during these integrity checks and can prevent the game from running, force a file repair, or issue a warning to the player.

Binary Signatures of Known Programs: Anti-cheat systems use a method known as binary signature matching to detect known cheat programs. These systems analyze the binary code of game files and compare it against a database of known cheat signatures. If a cheat program or its components are detected through matching these signatures, the anti-cheat can flag the player as a cheater.

# Opcode Signatures:
Opcode (operation code) signatures are another powerful tool used by anti-cheat systems to detect the presence of cheat programs. An opcode is a part of a machine instruction in the game's code that tells the processor what operation to perform. Cheating software often hooks into or alters these opcodes to manipulate the game’s behavior.

Opcode Signature Matching: Anti-cheat systems can monitor specific opcodes that are associated with known cheat functions (like aimbot functions, wallhacks, or other exploits). When a player runs a cheat that manipulates the game’s operations through altered opcodes, the system can detect the abnormal opcode and flag it as suspicious.

## What is "AI Aimbot?"
AI aimbot is a newer type of aimbot, that takes screen captures of the game and then uses a machine learning model to identify characters in the game. The algorirthm then calculates the X, Y and Z co-ordinates of the player, and moves the mouse to the cooridnates. AI Aimbots are harder to detect because they do not read or write to memory, however, they can still be detected through behavourial analysis due to the unnatural snapping of the crosshair and binary signature analysis. To demonstrate that even this is not sufficient to prevent AI Aimbots, we have built the Solar program with the state of the art Flare model. Flare has been trained on 9,488 natural images of Fortnite gameplay and 26,567 synthetic images, providing it with a 97% precision rate in identifying Fortnite characters in random pictures. The Solar software also incorporates unique features, as seen below. 

## Key Features
# Avoiding Memory Manipulation
One of the key features of tSolar is that it does not read from or write to game memory. Instead, it captures the screen in real-time and processes the image data using an AI model (Flare) to detect players and calculate their relative positions. This approach makes it much harder for memory-based anti-cheat systems, which typically monitor game memory for suspicious activity (such as accessing enemy positions or modifying game variables), to flag the cheat.

By avoiding memory manipulation, this aimbot sidesteps detection methods that focus on:

- Memory scanning for unusual memory access patterns.
- Signature matching for known cheats that modify game data.


# Preventing Static Binary Signatures
To further evade detection, Solar incorporates a randomization mechanism in the code. Each time Solar is opened, a random 25-character string is generated and embedded in a comment in the code. This random string changes every time the program is loaded, which makes it much harder for anti-cheat systems to generate a reliable binary signature for the program.

Static vs. Dynamic Signatures: Traditional aimbots can be detected by anti-cheats that rely on binary signatures (hashes) of known cheat files. By inserting a random string, the aimbot’s binary signature changes every time, preventing it from being flagged as a known cheat.

Comment Injection: The random string is inserted into the comment section of the code, ensuring it doesn’t affect the functionality of Solar. Since comments don’t execute and are ignored by the program, they don’t alter the behavior of the aimbot, but they alter its "fingerprint."
This approach makes the program's binary dynamic and non-static, meaning it can continuously evolve and evade traditional signature-based detection methods used by anti-cheat systems.

# Quadratic Movement for Human-Like Aiming
Solar moves the crosshair towards the target in a non-linear, human-like fashion. Instead of simply moving the crosshair directly in a straight line (which would be robotic and easily detectable), it uses a quadratic function to simulate more organic movement, mimicking the way a human would aim at a target. This makes it harder for anti-cheat systems to distinguish the movement from legitimate player actions.

---
The mathematical formula for the **ease-in, ease-out quadratic function** is as follows:

```math
ease\_in\_out\_quad(t) = 
\begin{cases}
2t^2 & \text{if } t < 0.5 \\
-1 + (4t) - (2t^2) & \text{if } t \geq 0.5
\end{cases}
```

Where:
- \( t \) is a normalized time variable (ranging from 0 to 1), representing the progress of the movement.
- For \( t < 0.5 \), the movement accelerates (ease-in).
- For \( t \geq 0.5 \), the movement decelerates (ease-out).
---

Why it’s human-like: This type of easing curve is typical in human motion, where players may initially aim more slowly, then speed up as they approach the target, and finally slow down as they get closer to the target. This gradual movement simulates a more natural, organic aiming behavior.

The quadratic easing function reduces the mechanical, robotic feel of simple linear aiming, which would otherwise be detectable by anti-cheat systems that analyze mouse movement patterns for unnatural or superhuman speeds.

# Code Implementation for Mouse Movement
To simulate the mouse movement, the aimbot uses ctypes to create a custom input structure that is sent to the system to move the mouse. Here's a brief breakdown of how the movement is simulated:

Mouse Input: The MouseInput structure in the code is used to define the mouse movement parameters, including the dx (change in x) and dy (change in y), which are calculated based on the target position.

Simulated Input: The input is sent to the system using ctypes.windll.user32.SendInput(), which simulates actual user input for mouse movement, making it harder to detect through traditional input monitoring methods.

Smoothness and Randomization: The movement is not only eased with the quadratic function but also randomized using a small delay between movements, making it harder to distinguish from human input.
The combination of quadratic movement, input simulation, and random delays gives the aimbot a smooth, human-like feel that makes it less likely to be flagged by anti-cheat systems that analyze input patterns for unnatural behavior.

</div>


## Installation

1. Install [Python 3.10.5](https://www.python.org/downloads/release/python-3105/)

2. Navigate to the root directory. Run the install_requirements.bat file

3. Run the start.bat file

## Usage
If the console is closing immediately, you can run this command to see the errors:
```           
python lunar.py
```
To update sensitivity settings:
```           
python lunar.py setup
```

## Future Developments

We wish to continue to develop the research model to keep in pace with future developments in anti cheats and continue to test their effectiveness. To do this, we wish to train the Flare model, the backbone of Solar, on 26,000 natural images of gameplay and 53,000 synthetic images of gameplay. 
