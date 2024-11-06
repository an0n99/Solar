**THIS IS A PURELY EDUCATIONAL RESEARCH PAPER INTO THE EFFECTIVENESS OF ANTI-CHEATS AND HOW AI MODELS ARE DISRUPTING THIS

# Solar
Solar Demonstration Model is built upon the [Flare](https://github.com/zeyad-mansour/lunar) object detection model. 

## How Does Aimbot Work?

Aimbots are software programs or modifications used to give players an unfair advantage in competitive video games by automating the aiming process. Typically, aimbots aim automatically at opponents, often with pixel-perfect precision, making it easier for players to score headshots or eliminate enemies without relying on their own aiming skills. To understand how aimbots work, it's essential to explore the different techniques and technologies they use.

1. Memory Access and Manipulation
One of the most common methods aimbots use is memory manipulation. Video games store key data like player positions, health, and other important in-game variables in the computer’s memory (RAM). Aimbots can gain access to this memory to retrieve critical information about enemy locations and game states. Here's how it typically works:

Memory Scanning: Aimbots scan the game's memory for relevant data structures, such as coordinates of enemy players, weapon stats, or aiming mechanics.
Memory Editing: Once the aimbot locates this data, it can modify or read it in real-time to adjust the player's aim toward enemies, even if the player isn't looking in their direction.
By manipulating memory, aimbots can programmatically move the player's crosshair towards opponents with high accuracy, even beyond what a normal player could achieve with manual aiming.

2. Game Memory Injection and DLL Injection
DLL (Dynamic Link Library) injection is another method aimbots use to hook into a game. This involves the aimbot inserting a custom DLL file into the game's memory space, which allows the aimbot to execute code within the game's process. The injected DLL is typically responsible for:

Reading Game Data: As with memory manipulation, it can read data from the game's memory, including enemy positions and other player-related data.
Modifying Aiming or Movement: The DLL can also modify the player's in-game actions, such as altering the mouse input, changing the view angle, or moving the player's crosshair automatically to target enemies.
DLL injection is more sophisticated than memory manipulation alone because it allows the aimbot to interact directly with the game code, making it harder for basic anti-cheat systems to detect.

## How Do Anti-Cheats Detect Aimbot?
1. Memory Scanning and Analysis
One of the primary methods anti-cheat systems use to detect memory manipulation is by scanning the game’s memory during runtime. These scans focus on identifying unusual patterns or modifications in the game's memory space, which could indicate that a cheat is active.

Memory Integrity Checks: Anti-cheat systems periodically scan the memory of running games for anomalies, such as unfamiliar code or data structures that do not match the expected values. This helps detect unauthorized memory injections or changes to in-game variables that would be manipulated by an aimbot.

Behavioral Analysis: Anti-cheats may also monitor the behavior of the game in memory. For example, if player data such as enemy positions or player coordinates are being altered or read by processes outside of the standard game flow, it can trigger an alert. This is especially effective for detecting cheats that access and modify game memory in real-time.

Signature Matching: Anti-cheat systems can compare memory data to a database of known cheat signatures. These signatures are patterns that have been identified from known cheats (e.g., aimbots or wallhacks). If the memory access pattern matches an entry in the cheat database, the system flags the activity as suspicious.

2. DLL Injection Detection
DLL injection is one of the most common techniques used by aimbots to manipulate a game’s behavior. Anti-cheat systems have several methods to detect DLL injections:

Monitoring Processes and Modules: Anti-cheats constantly monitor the game's processes for unexpected DLLs. If a game process loads a DLL that is not part of the game's standard files, the anti-cheat system can identify and flag it. This includes third-party DLLs injected into the game’s memory by cheats.

Checking for Unusual Function Calls: When a DLL is injected into a game, it may alter or hook into game functions (such as rendering or input functions). Anti-cheat systems can monitor for unusual function calls or memory hooks that are not part of the original game code. If the system detects a hook or function modification that is not part of the legitimate game engine, it can flag it as a cheat.

3. File Hashing and Integrity Checks
File integrity checking is one of the most common and effective methods used to detect file manipulation, which is often employed by cheats to modify or replace game assets (e.g., to inject cheat code or alter game files).

File Hashing: Anti-cheat systems use cryptographic hash functions (such as MD5, SHA-1, or SHA-256) to compute a hash for each critical game file (e.g., executables, DLLs, assets, and configuration files). When the game is launched, the anti-cheat system compares the hash of each file with a stored reference value. If a file’s hash does not match the expected value, it is flagged for potential modification.

File Integrity Enforcement: Anti-cheat systems may implement runtime checks to enforce file integrity. For example, if a player has altered or replaced a game’s executable or assets with a modified version (such as aimbot code or other cheats), the anti-cheat system will detect discrepancies during these integrity checks and can prevent the game from running, force a file repair, or issue a warning to the player.

Binary Signatures of Known Programs: Anti-cheat systems use a method known as binary signature matching to detect known cheat programs. These systems analyze the binary code of game files and compare it against a database of known cheat signatures. If a cheat program or its components are detected through matching these signatures, the anti-cheat can flag the player as a cheater.

4. Opcode Signatures
Opcode (operation code) signatures are another powerful tool used by anti-cheat systems to detect the presence of cheat programs. An opcode is a part of a machine instruction in the game's code that tells the processor what operation to perform. Cheating software often hooks into or alters these opcodes to manipulate the game’s behavior.

Opcode Signature Matching: Anti-cheat systems can monitor specific opcodes that are associated with known cheat functions (like aimbot functions, wallhacks, or other exploits). When a player runs a cheat that manipulates the game’s operations through altered opcodes, the system can detect the abnormal opcode and flag it as suspicious.




Lunar LITE has been upgraded to [YOLOv8](https://github.com/ultralytics/ultralytics)

![Lunar Lite banner](https://github.com/user-attachments/assets/05864acf-cdd1-484f-be79-fa4a9643e8c2)

![Thumbnail](https://github.com/user-attachments/assets/afa30dd2-8168-4c64-999e-bedb0bef4dec)

<div align="center">

  
[![discord server](https://ucarecdn.com/38366345-9cd9-47e2-b4b5-f3586975d0e6/lunar.svg)](https://discord.gg/St8xd8d9Ts)


</div>


## Installation

1. Install [Python 3.10.5](https://www.python.org/downloads/release/python-3105/)

2. Navigate to the root directory. Run the install_requirements.bat file

3. Run the start.bat file

4. TIP: To make it more undetected, obfuscate the code. 

## Usage
If the console is closing immediately, you can run this command to see the errors:
```           
python lunar.py
```
To update sensitivity settings:
```           
python lunar.py setup
```

