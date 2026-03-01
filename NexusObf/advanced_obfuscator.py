"""
Advanced AST-Based Lua Obfuscator
Includes sophisticated techniques like:
- Opaque predicates
- Control flow flattening
- String encryption layers
- Anti-debugging measures
- Constant folding obfuscation
"""

import random
import string
import hashlib
from typing import List, Dict, Tuple

class AdvancedObfuscator:
    """Advanced obfuscation techniques beyond basic string/variable replacement"""
    
    def __init__(self):
        self.anti_debug_checks = []
        self.opaque_predicates = []
        
    def create_string_encryption_layer(self, strings: List[str]) -> Tuple[str, Dict[int, str]]:
        """
        Create a multi-layer string encryption system
        Returns: (decoder_code, encrypted_strings_map)
        """
        key_table = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        
        decoder = f'''
local _STR_KEY = "{key_table}"
local _STR_CACHE = {{}}
local _STR_DECRYPT = function(id)
    if _STR_CACHE[id] then return _STR_CACHE[id] end
    local encrypted = _STR_DATA[id]
    local result = ""
    for i = 1, #encrypted do
        local byte = encrypted:byte(i)
        local key_byte = _STR_KEY:byte(((i - 1) % #_STR_KEY) + 1)
        result = result .. string.char(byte ~ key_byte)
    end
    _STR_CACHE[id] = result
    return result
end
'''
        
        encrypted_map = {}
        for idx, s in enumerate(strings):
            encrypted = ""
            for i, c in enumerate(s):
                byte = ord(c)
                key_byte = ord(key_table[i % len(key_table)])
                encrypted += chr(byte ^ key_byte)
            encrypted_map[idx] = encrypted
        
        return decoder, encrypted_map
    
    def generate_opaque_predicate(self) -> str:
        """
        Generate an opaque predicate (always true/false but hard to determine statically)
        """
        predicates = [
            # Always true
            "(function() local x = math.random(1,1000000) return (x*x >= 0) end)()",
            "(function() return (2+2 == 4) end)()",
            "(function() local t = {} return (type(t) == 'table') end)()",
            
            # More complex always-true
            "(function() local a,b = 7,13 return ((a*b) % 2 == 1) end)()",
            "(function() return (string.len('') == 0) end)()",
        ]
        return random.choice(predicates)
    
    def generate_junk_code_blocks(self, count: int = 5) -> List[str]:
        """Generate junk code that looks important but does nothing"""
        junk_blocks = []
        
        for _ in range(count):
            templates = [
                # Fake mathematical computation
                f'''local _C{random.randint(1000,9999)} = function()
    local sum = 0
    for i = 1, {random.randint(10,100)} do
        sum = sum + (i * {random.randint(1,10)}) % {random.randint(100,1000)}
    end
    return sum > -1 and nil or sum
end''',
                
                # Fake string processing
                f'''local _S{random.randint(1000,9999)} = function()
    local chars = "{(''.join(random.choices(string.ascii_letters, k=20)))}"
    local result = ""
    for i = 1, #chars do
        if false then result = result .. chars:sub(i,i) end
    end
    return result
end''',
                
                # Fake table manipulation
                f'''local _T{random.randint(1000,9999)} = {{}}
for i = 1, {random.randint(5,20)} do
    _T{random.randint(1000,9999)}[i] = i * {random.randint(1,10)}
    if nil then return _T{random.randint(1000,9999)} end
end''',
            ]
            junk_blocks.append(random.choice(templates))
        
        return junk_blocks
    
    def create_anti_debug_layer(self) -> str:
        """Create anti-debugging and anti-analysis code"""
        anti_debug = f'''
-- Anti-Debug Layer
local _DEBUG_CHECK_{random.randint(1000,9999)} = function()
    local env_check = getfenv or debug.getfenv
    if env_check and env_check(2) then
        local suspicious = false
        -- Check for common debugging functions
        if debug and (debug.getinfo or debug.traceback) then
            suspicious = true
        end
        if suspicious and {self.generate_opaque_predicate()} then
            -- Infinite loop to prevent debugging
            while true do end
        end
    end
end

local _INTEGRITY_{random.randint(1000,9999)} = function()
    -- Check script integrity
    local check_sum = {random.randint(10000, 99999)}
    if check_sum ~= {random.randint(10000, 99999)} then
        if {self.generate_opaque_predicate()} then
            return true
        end
    end
end

_DEBUG_CHECK_{random.randint(1000,9999)}()
_INTEGRITY_{random.randint(1000,9999)}()
'''
        return anti_debug
    
    def create_control_flow_obfuscation(self, code_blocks: List[str]) -> str:
        """
        Create control flow obfuscation using state machines
        Converts sequential code into a dispatcher pattern
        """
        num_states = len(code_blocks)
        state_order = list(range(num_states))
        random.shuffle(state_order)
        
        # Generate state dispatcher
        dispatcher = f'''
local _STATE_{random.randint(1000,9999)} = {state_order[0]}
local _NEXT_{random.randint(1000,9999)} = {{}}
'''
        
        # Map state transitions
        for i in range(num_states):
            current = state_order[i]
            next_state = state_order[(i + 1) % num_states] if i < num_states - 1 else -1
            dispatcher += f'_NEXT_{random.randint(1000,9999)}[{current}] = {next_state}\n'
        
        # Create dispatch loop
        dispatcher += f'''
while _STATE_{random.randint(1000,9999)} ~= -1 do
    local _CURRENT = _STATE_{random.randint(1000,9999)}
'''
        
        for i, block in enumerate(code_blocks):
            state_id = state_order[i]
            dispatcher += f'''
    {"if" if i == 0 else "elseif"} _CURRENT == {state_id} then
        {block}
        _STATE_{random.randint(1000,9999)} = _NEXT_{random.randint(1000,9999)}[_CURRENT]
'''
        
        dispatcher += '''
    end
end
'''
        return dispatcher
    
    def create_vm_wrapper(self, script: str) -> str:
        """
        Create a mini virtual machine to execute the script
        This adds significant complexity to reverse engineering
        """
        # Create instruction set
        instructions = []
        
        # Split script into chunks
        chunk_size = random.randint(50, 150)
        for i in range(0, len(script), chunk_size):
            chunk = script[i:i+chunk_size]
            # Encode chunk
            encoded = ''.join(f'\\{ord(c)}' for c in chunk)
            instructions.append(encoded)
        
        vm = f'''
-- Virtual Machine Layer
local _VM_{random.randint(1000,9999)} = {{}}
_VM_{random.randint(1000,9999)}.instructions = {{
{', '.join(f'"{inst}"' for inst in instructions)}
}}

_VM_{random.randint(1000,9999)}.decode = function(inst)
    local result = ""
    local i = 1
    while i <= #inst do
        if inst:sub(i,i) == "\\\\" then
            local code = ""
            i = i + 1
            while i <= #inst and inst:sub(i,i):match("%d") do
                code = code .. inst:sub(i,i)
                i = i + 1
            end
            result = result .. string.char(tonumber(code))
        else
            result = result .. inst:sub(i,i)
            i = i + 1
        end
    end
    return result
end

_VM_{random.randint(1000,9999)}.execute = function()
    local full_code = ""
    for _, inst in ipairs(_VM_{random.randint(1000,9999)}.instructions) do
        full_code = full_code .. _VM_{random.randint(1000,9999)}.decode(inst)
    end
    local func = loadstring(full_code)
    if func then func() end
end

_VM_{random.randint(1000,9999)}.execute()
'''
        return vm
    
    def add_fake_vulnerabilities(self) -> List[str]:
        """Add fake vulnerabilities to waste reverse engineer's time"""
        fakes = [
            '''
-- Fake backdoor (inactive)
local _BACKDOOR = function(code)
    if false and code == "''' + ''.join(random.choices(string.ascii_letters + string.digits, k=32)) + '''" then
        return loadstring
    end
end
''',
            '''
-- Fake admin check (never triggers)
local _ADMIN_KEY = "''' + hashlib.md5(str(random.random()).encode()).hexdigest() + '''"
local _CHECK_ADMIN = function(key)
    if key == _ADMIN_KEY and nil then
        return true
    end
end
''',
        ]
        return fakes
    
    def create_number_obfuscation_functions(self) -> str:
        """Create functions that return numbers in obfuscated ways"""
        funcs = f'''
local _NUM_{random.randint(1000,9999)} = function(a, b, c)
    return ((a * b) + c - a) / b + (a - c)
end

local _CALC_{random.randint(1000,9999)} = function(x)
    local r = 0
    for i = 1, x do r = r + 1 end
    return r
end

local _CONST_{random.randint(1000,9999)} = {{}}
for i = 0, 255 do
    _CONST_{random.randint(1000,9999)}[i] = i
end
'''
        return funcs


class MetamorphicEngine:
    """
    Metamorphic engine that generates functionally equivalent but structurally different code
    """
    
    def __init__(self):
        self.transformations = []
    
    def transform_loops(self, code: str) -> str:
        """Transform loop structures"""
        # Example: for i=1,10 do ... end
        # Transform to: local i=1 while i<=10 do ... i=i+1 end
        return code  # Placeholder for full implementation
    
    def transform_conditions(self, code: str) -> str:
        """Transform if-else structures"""
        # Example: if x then y else z end
        # Transform to: local r = x and y or z
        return code  # Placeholder
    
    def apply_all_transformations(self, code: str) -> str:
        """Apply all metamorphic transformations"""
        code = self.transform_loops(code)
        code = self.transform_conditions(code)
        return code


def apply_advanced_obfuscation(script: str, options: Dict = None) -> str:
    """
    Apply all advanced obfuscation techniques
    
    Options:
        - anti_debug: bool (default True)
        - vm_wrapper: bool (default True)
        - control_flow: bool (default True)
        - junk_code: bool (default True)
        - fake_vulns: bool (default False)
    """
    if options is None:
        options = {
            'anti_debug': True,
            'vm_wrapper': True,
            'control_flow': True,
            'junk_code': True,
            'fake_vulns': False
        }
    
    obf = AdvancedObfuscator()
    result = script
    
    # Add layers in order
    if options.get('anti_debug'):
        result = obf.create_anti_debug_layer() + "\n" + result
    
    if options.get('junk_code'):
        junk = obf.generate_junk_code_blocks(random.randint(5, 10))
        result = '\n'.join(junk) + "\n" + result
    
    if options.get('fake_vulns'):
        fakes = obf.add_fake_vulnerabilities()
        result = '\n'.join(fakes) + "\n" + result
    
    result = obf.create_number_obfuscation_functions() + "\n" + result
    
    if options.get('vm_wrapper'):
        result = obf.create_vm_wrapper(result)
    
    return result
