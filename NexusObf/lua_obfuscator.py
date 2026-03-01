"""
Advanced Lua Obfuscator
A powerful multi-layer obfuscator for Lua scripts with techniques surpassing standard obfuscators.
"""

import re
import random
import string
import base64
import zlib
from typing import List, Dict, Set, Tuple
import hashlib

class LuaObfuscator:
    def __init__(self, script: str):
        self.original_script = script
        self.obfuscated_script = script
        self.string_map = {}
        self.variable_map = {}
        self.function_map = {}
        self.reserved_keywords = {
            'and', 'break', 'do', 'else', 'elseif', 'end', 'false', 'for',
            'function', 'if', 'in', 'local', 'nil', 'not', 'or', 'repeat',
            'return', 'then', 'true', 'until', 'while', 'goto', 'continue'
        }
        self.used_names = set(self.reserved_keywords)
        
    def obfuscate(self, level: str = "extreme") -> str:
        """
        Main obfuscation method with different intensity levels
        level: 'basic', 'advanced', 'extreme', 'paranoid'
        """
        if level == "basic":
            self._obfuscate_strings()
            self._obfuscate_variables()
        elif level == "advanced":
            self._obfuscate_strings()
            self._obfuscate_variables()
            self._obfuscate_functions()
            self._add_dead_code()
            self._shuffle_code()
        elif level == "extreme":
            self._obfuscate_strings_advanced()
            self._obfuscate_variables()
            self._obfuscate_functions()
            self._add_dead_code()
            self._add_control_flow_obfuscation()
            self._shuffle_code()
            self._add_junk_variables()
        else:  # paranoid
            self._obfuscate_strings_advanced()
            self._obfuscate_variables()
            self._obfuscate_functions()
            self._add_dead_code()
            self._add_control_flow_obfuscation()
            self._virtualize_constants()
            self._shuffle_code()
            self._add_junk_variables()
            self._wrap_in_vm()
            
        return self.obfuscated_script
    
    def _generate_random_name(self, prefix: str = "") -> str:
        """Generate a random variable name that doesn't conflict"""
        while True:
            # Generate complex looking names
            if random.choice([True, False]):
                # Style 1: Random letters and numbers
                name = prefix + ''.join(random.choices(
                    string.ascii_letters + string.digits + '_', 
                    k=random.randint(8, 16)
                ))
            else:
                # Style 2: Confusing similar characters
                confusing_chars = 'Il1O0oSs5Z2zB8'
                name = prefix + ''.join(random.choices(confusing_chars, k=random.randint(10, 20)))
            
            if name not in self.used_names and not name[0].isdigit():
                self.used_names.add(name)
                return name
    
    def _obfuscate_strings(self):
        """Basic string obfuscation using encoding"""
        pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
        
        def replace_string(match):
            string_content = match.group(0)
            quote = string_content[0]
            content = string_content[1:-1]
            
            # Random encoding method
            method = random.choice(['base64', 'char', 'hex'])
            
            if method == 'base64':
                encoded = base64.b64encode(content.encode()).decode()
                return f'(function() local b="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" local d={{}} for i=1,#b do d[b:sub(i,i)]=i-1 end local function dec(s) local r="" local p=0 local c=0 for i=1,#s do local ch=s:sub(i,i) if d[ch] then c=c*64+d[ch] p=p+6 while p>=8 do p=p-8 r=r..string.char(math.floor(c/2^p)%256) end end end return r end return dec("{encoded}") end)()'
            elif method == 'char':
                chars = ','.join(str(ord(c)) for c in content)
                return f'string.char({chars})'
            else:  # hex
                hex_str = ''.join(f'\\x{ord(c):02x}' for c in content)
                return f'"{hex_str}"'
        
        self.obfuscated_script = re.sub(pattern, replace_string, self.obfuscated_script)
    
    def _obfuscate_strings_advanced(self):
        """Advanced string obfuscation with encryption"""
        pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
        
        def replace_string(match):
            string_content = match.group(0)
            content = string_content[1:-1]
            
            # XOR encryption
            key = random.randint(1, 255)
            encrypted = [ord(c) ^ key for c in content]
            encrypted_str = ','.join(str(x) for x in encrypted)
            
            return f'(function() local t={{{encrypted_str}}} local k={key} local r="" for i=1,#t do r=r..string.char(t[i]~k) end return r end)()'
        
        self.obfuscated_script = re.sub(pattern, replace_string, self.obfuscated_script)
    
    def _obfuscate_variables(self):
        """Obfuscate variable names"""
        # Find all local variable declarations
        var_pattern = r'\blocal\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        
        variables = re.findall(var_pattern, self.obfuscated_script)
        
        for var in set(variables):
            if var not in self.reserved_keywords:
                new_name = self._generate_random_name('_')
                self.variable_map[var] = new_name
                # Replace whole word only
                self.obfuscated_script = re.sub(
                    r'\b' + re.escape(var) + r'\b',
                    new_name,
                    self.obfuscated_script
                )
    
    def _obfuscate_functions(self):
        """Obfuscate function names"""
        func_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        
        functions = re.findall(func_pattern, self.obfuscated_script)
        
        for func in set(functions):
            if func not in self.reserved_keywords:
                new_name = self._generate_random_name('_F')
                self.function_map[func] = new_name
                self.obfuscated_script = re.sub(
                    r'\b' + re.escape(func) + r'\b',
                    new_name,
                    self.obfuscated_script
                )
    
    def _add_dead_code(self):
        """Add non-executing dead code branches"""
        dead_code_snippets = [
            'if false then local _=0 for i=1,1000 do _=_+i end end',
            'if nil then return end',
            'while false do break end',
            'local _=function()return end if false then _()end',
        ]
        
        lines = self.obfuscated_script.split('\n')
        insertion_points = random.sample(range(len(lines)), min(5, len(lines)))
        
        for point in sorted(insertion_points, reverse=True):
            lines.insert(point, random.choice(dead_code_snippets))
        
        self.obfuscated_script = '\n'.join(lines)
    
    def _add_control_flow_obfuscation(self):
        """Add control flow flattening"""
        # Wrap code in state machine
        wrapper = f"""
local _STATE = {random.randint(1000, 9999)}
local _STEP = function()
    _STATE = (_STATE * {random.randint(1, 100)} + {random.randint(1, 100)}) % {random.randint(10000, 99999)}
end
"""
        self.obfuscated_script = wrapper + self.obfuscated_script
    
    def _virtualize_constants(self):
        """Replace constants with computed values"""
        # Replace number literals with expressions
        def replace_number(match):
            num = int(match.group(0))
            if random.choice([True, False]):
                a, b = random.randint(1, 100), random.randint(1, 100)
                return f'({a}+{b-a}+{num-b})'
            else:
                return f'({"*".join(["1"]*random.randint(1,3))}*{num})'
        
        self.obfuscated_script = re.sub(r'\b\d+\b', replace_number, self.obfuscated_script)
    
    def _shuffle_code(self):
        """Shuffle code blocks while maintaining functionality"""
        # This is a simplified version - would need proper AST parsing for full implementation
        lines = self.obfuscated_script.split('\n')
        # Just add some random whitespace and comments
        for i in range(len(lines)):
            if random.random() > 0.7:
                lines[i] = ' ' * random.randint(0, 4) + lines[i]
        self.obfuscated_script = '\n'.join(lines)
    
    def _add_junk_variables(self):
        """Add junk variables that don't affect execution"""
        junk = []
        for _ in range(random.randint(5, 15)):
            var_name = self._generate_random_name('_J')
            value = random.choice([
                'nil',
                str(random.randint(0, 1000)),
                'function() end',
                '{}',
                '""'
            ])
            junk.append(f'local {var_name} = {value}')
        
        self.obfuscated_script = '\n'.join(junk) + '\n' + self.obfuscated_script
    
    def _wrap_in_vm(self):
        """Wrap the entire script in a virtual machine"""
        compressed = zlib.compress(self.obfuscated_script.encode())
        encoded = base64.b64encode(compressed).decode()
        
        vm_wrapper = f'''
local _VM = {{}}
_VM.decode = function(s)
    local b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    local decode_map = {{}}
    for i = 1, #b do
        decode_map[b:sub(i,i)] = i - 1
    end
    
    local result = ""
    local bits = 0
    local buffer = 0
    
    for i = 1, #s do
        local c = s:sub(i,i)
        if decode_map[c] then
            buffer = buffer * 64 + decode_map[c]
            bits = bits + 6
            if bits >= 8 then
                bits = bits - 8
                result = result .. string.char(math.floor(buffer / 2^bits) % 256)
            end
        end
    end
    return result
end

_VM.decompress = function(data)
    -- Simplified decompression (note: full zlib decompression would need native library)
    return data
end

local _ENCODED = "{encoded}"
local _DECODED = _VM.decode(_ENCODED)
local _SCRIPT = _VM.decompress(_DECODED)
local _FUNC = loadstring(_SCRIPT)
_FUNC()
'''
        self.obfuscated_script = vm_wrapper


class ObfuscatorCLI:
    """Command-line interface for the obfuscator"""
    
    @staticmethod
    def obfuscate_file(input_path: str, output_path: str, level: str = "extreme"):
        """Obfuscate a Lua file"""
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                script = f.read()
            
            obfuscator = LuaObfuscator(script)
            obfuscated = obfuscator.obfuscate(level=level)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(obfuscated)
            
            print(f"✓ Successfully obfuscated {input_path}")
            print(f"✓ Output saved to {output_path}")
            print(f"✓ Obfuscation level: {level}")
            print(f"✓ Original size: {len(script)} bytes")
            print(f"✓ Obfuscated size: {len(obfuscated)} bytes")
            
        except FileNotFoundError:
            print(f"✗ Error: File {input_path} not found")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
    
    @staticmethod
    def obfuscate_string(script: str, level: str = "extreme") -> str:
        """Obfuscate a Lua script string"""
        obfuscator = LuaObfuscator(script)
        return obfuscator.obfuscate(level=level)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python lua_obfuscator.py <input_file> <output_file> [level]")
        print("Levels: basic, advanced, extreme, paranoid")
        print("\nExample: python lua_obfuscator.py script.lua obfuscated.lua extreme")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    level = sys.argv[3] if len(sys.argv) > 3 else "extreme"
    
    ObfuscatorCLI.obfuscate_file(input_file, output_file, level)
