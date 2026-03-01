-- Sample Roblox Script for Testing the Obfuscator
-- This script demonstrates various Lua features that will be obfuscated

-- Variables
local player = game.Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")

-- Constants
local MAX_HEALTH = 100
local SPEED_MULTIPLIER = 1.5
local GAME_VERSION = "1.0.0"

-- Strings to be obfuscated
local welcomeMessage = "Welcome to the game!"
local secretKey = "MySecretAPIKey12345"

-- Tables
local playerData = {
    coins = 0,
    level = 1,
    inventory = {},
    settings = {
        music = true,
        sound = true
    }
}

-- Function declarations
local function addCoins(amount)
    playerData.coins = playerData.coins + amount
    print("Coins added: " .. amount)
    print("Total coins: " .. playerData.coins)
end

local function levelUp()
    playerData.level = playerData.level + 1
    print("Level up! New level: " .. playerData.level)
    
    -- Heal player on level up
    if humanoid then
        humanoid.Health = MAX_HEALTH
    end
end

local function checkInventory(itemName)
    for _, item in ipairs(playerData.inventory) do
        if item == itemName then
            return true
        end
    end
    return false
end

-- Conditional logic
if player then
    print(welcomeMessage)
    print("Player name: " .. player.Name)
    
    if playerData.level >= 10 then
        print("You are a veteran player!")
    elseif playerData.level >= 5 then
        print("You are an experienced player!")
    else
        print("You are a new player!")
    end
end

-- Loops
for i = 1, 5 do
    print("Iteration: " .. i)
end

local count = 0
while count < 3 do
    count = count + 1
    print("Count: " .. count)
end

-- Game services
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local TweenService = game:GetService("TweenService")

-- Remote Events (common in Roblox)
local remoteEvent = ReplicatedStorage:FindFirstChild("GameEvent")
if remoteEvent then
    remoteEvent.OnClientEvent:Connect(function(eventType, data)
        if eventType == "COIN_REWARD" then
            addCoins(data.amount)
        elseif eventType == "LEVEL_UP" then
            levelUp()
        elseif eventType == "INVENTORY_ADD" then
            table.insert(playerData.inventory, data.item)
            print("Item added: " .. data.item)
        end
    end)
end

-- Character setup
character.DescendantAdded:Connect(function(descendant)
    if descendant:IsA("BasePart") then
        descendant.Transparency = 0
    end
end)

-- Humanoid events
humanoid.Died:Connect(function()
    print(player.Name .. " has died!")
    playerData.coins = math.floor(playerData.coins * 0.5)
    print("Coins lost. Remaining: " .. playerData.coins)
end)

-- Mathematical operations
local function calculateDamage(baseDamage, multiplier)
    local finalDamage = baseDamage * multiplier
    
    -- Critical hit chance
    if math.random() < 0.1 then
        finalDamage = finalDamage * 2
        print("Critical hit!")
    end
    
    return finalDamage
end

-- String manipulation
local function formatPlayerName(name)
    return "[VIP] " .. name:upper()
end

-- Advanced function with multiple returns
local function getPlayerStats()
    return playerData.coins, playerData.level, #playerData.inventory
end

-- Error handling
local function safeLoadData(dataKey)
    local success, result = pcall(function()
        -- Simulated data loading
        return playerData[dataKey]
    end)
    
    if success then
        return result
    else
        warn("Failed to load data: " .. dataKey)
        return nil
    end
end

-- Metatables (advanced Lua feature)
local gameConfig = {
    maxPlayers = 50,
    roundTime = 300,
    mapRotation = {"Map1", "Map2", "Map3"}
}

setmetatable(gameConfig, {
    __index = function(table, key)
        warn("Accessing undefined config: " .. key)
        return nil
    end
})

-- Coroutines
local function countdownTimer(seconds)
    for i = seconds, 1, -1 do
        print("Time remaining: " .. i)
        wait(1)
    end
    print("Time's up!")
end

-- Start some processes
spawn(function()
    while true do
        wait(5)
        -- Periodic health check
        if humanoid and humanoid.Health < MAX_HEALTH then
            humanoid.Health = humanoid.Health + 5
        end
    end
end)

-- Initialize
print("Script initialized successfully!")
print("Version: " .. GAME_VERSION)
addCoins(100)

-- This script contains:
-- ✓ Variables and constants
-- ✓ Strings (including sensitive data)
-- ✓ Functions with various complexity
-- ✓ Conditional statements
-- ✓ Loops (for, while)
-- ✓ Tables and nested tables
-- ✓ Remote events
-- ✓ Game services
-- ✓ Event connections
-- ✓ Mathematical operations
-- ✓ String manipulation
-- ✓ Error handling (pcall)
-- ✓ Metatables
-- ✓ Coroutines
-- ✓ Comments (will be preserved or removed based on settings)

-- Perfect for testing the obfuscator's capabilities!
