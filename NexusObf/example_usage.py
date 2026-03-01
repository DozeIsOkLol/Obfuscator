"""
Example Usage Script
Demonstrates various features of the Lua Obfuscator
"""

from lua_obfuscator import LuaObfuscator, ObfuscatorCLI
from advanced_obfuscator import apply_advanced_obfuscation

# Example 1: Basic obfuscation
print("=" * 60)
print("EXAMPLE 1: Basic Obfuscation")
print("=" * 60)

example_script_1 = """
local player = game.Players.LocalPlayer
local character = player.Character

function greetPlayer()
    print("Hello, " .. player.Name)
end

greetPlayer()
"""

print("\n[Original Script]")
print(example_script_1)

obfuscator = LuaObfuscator(example_script_1)
obfuscated_1 = obfuscator.obfuscate(level="basic")

print("\n[Obfuscated - Basic Level]")
print(obfuscated_1[:500] + "...\n")

# Example 2: Advanced obfuscation
print("\n" + "=" * 60)
print("EXAMPLE 2: Advanced Obfuscation")
print("=" * 60)

example_script_2 = """
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RemoteEvent = ReplicatedStorage:WaitForChild("GameEvent")

local coins = 0

local function addCoins(amount)
    coins = coins + amount
    print("Coins: " .. coins)
end

RemoteEvent.OnClientEvent:Connect(function(eventType, data)
    if eventType == "COINS" then
        addCoins(data)
    end
end)
"""

print("\n[Original Script]")
print(example_script_2)

obfuscator2 = LuaObfuscator(example_script_2)
obfuscated_2 = obfuscator2.obfuscate(level="advanced")

print("\n[Obfuscated - Advanced Level]")
print(obfuscated_2[:500] + "...\n")

# Example 3: Extreme obfuscation
print("\n" + "=" * 60)
print("EXAMPLE 3: Extreme Obfuscation")
print("=" * 60)

example_script_3 = """
local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")

local API_KEY = "secret_key_12345"
local API_URL = "https://api.example.com/data"

local function fetchData(userId)
    local success, result = pcall(function()
        return HttpService:GetAsync(API_URL .. "?user=" .. userId .. "&key=" .. API_KEY)
    end)
    
    if success then
        local data = HttpService:JSONDecode(result)
        return data
    else
        warn("Failed to fetch data")
        return nil
    end
end

Players.PlayerAdded:Connect(function(player)
    local data = fetchData(player.UserId)
    if data then
        print("Loaded data for " .. player.Name)
    end
end)
"""

print("\n[Original Script]")
print(example_script_3)

obfuscator3 = LuaObfuscator(example_script_3)
obfuscated_3 = obfuscator3.obfuscate(level="extreme")

print("\n[Obfuscated - Extreme Level]")
print(obfuscated_3[:800] + "...\n")

# Example 4: Paranoid level with advanced techniques
print("\n" + "=" * 60)
print("EXAMPLE 4: Paranoid + Advanced Techniques")
print("=" * 60)

example_script_4 = """
local adminList = {
    ["Player1"] = true,
    ["Player2"] = true,
}

local function isAdmin(playerName)
    return adminList[playerName] == true
end

local function executeCommand(player, command)
    if not isAdmin(player.Name) then
        return false, "Not authorized"
    end
    
    if command == "ban" then
        -- Ban logic
        return true, "User banned"
    elseif command == "kick" then
        -- Kick logic
        return true, "User kicked"
    end
    
    return false, "Unknown command"
end
"""

print("\n[Original Script]")
print(example_script_4)

obfuscator4 = LuaObfuscator(example_script_4)
obfuscated_base = obfuscator4.obfuscate(level="paranoid")

# Apply advanced techniques
advanced_options = {
    'anti_debug': True,
    'vm_wrapper': True,
    'control_flow': True,
    'junk_code': True,
    'fake_vulns': True
}

obfuscated_4 = apply_advanced_obfuscation(obfuscated_base, advanced_options)

print("\n[Obfuscated - Paranoid + All Advanced Techniques]")
print(obfuscated_4[:800] + "...\n")

# Example 5: String obfuscation comparison
print("\n" + "=" * 60)
print("EXAMPLE 5: String Obfuscation Techniques")
print("=" * 60)

string_example = """
local message = "This is a secret message"
local password = "SuperSecretPassword123"
local apiKey = "sk_live_abc123xyz789"
print(message)
"""

print("\n[Original Script with Strings]")
print(string_example)

obfuscator5 = LuaObfuscator(string_example)
obfuscated_5 = obfuscator5.obfuscate(level="extreme")

print("\n[Obfuscated Strings]")
print(obfuscated_5[:600] + "...\n")

# Example 6: Performance comparison
print("\n" + "=" * 60)
print("EXAMPLE 6: Size Comparison")
print("=" * 60)

test_scripts = [
    ("Small Script (5 lines)", example_script_1),
    ("Medium Script (15 lines)", example_script_2),
    ("Large Script (25 lines)", example_script_3)
]

for name, script in test_scripts:
    original_size = len(script)
    
    obf = LuaObfuscator(script)
    obf_basic = obf.obfuscate(level="basic")
    obf_advanced = obf.obfuscate(level="advanced")
    obf_extreme = obf.obfuscate(level="extreme")
    
    print(f"\n{name}:")
    print(f"  Original:  {original_size:,} bytes")
    print(f"  Basic:     {len(obf_basic):,} bytes ({len(obf_basic)/original_size:.2f}x)")
    print(f"  Advanced:  {len(obf_advanced):,} bytes ({len(obf_advanced)/original_size:.2f}x)")
    print(f"  Extreme:   {len(obf_extreme):,} bytes ({len(obf_extreme)/original_size:.2f}x)")

# Example 7: CLI usage demonstration
print("\n" + "=" * 60)
print("EXAMPLE 7: CLI Usage Examples")
print("=" * 60)

print("""
Command Line Interface Usage:

1. Basic obfuscation:
   python lua_obfuscator.py input.lua output.lua basic

2. Advanced obfuscation:
   python lua_obfuscator.py input.lua output.lua advanced

3. Extreme obfuscation (default):
   python lua_obfuscator.py input.lua output.lua

4. Paranoid obfuscation:
   python lua_obfuscator.py input.lua output.lua paranoid

GUI Usage:
   python obfuscator_gui.py
""")

# Example 8: Batch processing
print("\n" + "=" * 60)
print("EXAMPLE 8: Batch Processing Multiple Files")
print("=" * 60)

print("""
Batch Processing Example:

import glob
from lua_obfuscator import LuaObfuscator

# Find all Lua files in a directory
lua_files = glob.glob("scripts/*.lua")

for file in lua_files:
    with open(file, 'r') as f:
        script = f.read()
    
    obfuscator = LuaObfuscator(script)
    obfuscated = obfuscator.obfuscate(level="extreme")
    
    output_file = file.replace(".lua", "_obfuscated.lua")
    with open(output_file, 'w') as f:
        f.write(obfuscated)
    
    print(f"✓ Obfuscated: {file} -> {output_file}")
""")

print("\n" + "=" * 60)
print("All examples completed!")
print("=" * 60)
