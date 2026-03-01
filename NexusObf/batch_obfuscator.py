"""
Batch Lua Obfuscator
Process multiple Lua files at once with various options
"""

import os
import glob
import sys
import time
from pathlib import Path
from lua_obfuscator import LuaObfuscator
from advanced_obfuscator import apply_advanced_obfuscation

class BatchObfuscator:
    def __init__(self):
        self.processed = 0
        self.failed = 0
        self.total_time = 0
        
    def obfuscate_directory(self, input_dir, output_dir=None, level="extreme", 
                           pattern="*.lua", recursive=False, advanced_options=None):
        """
        Obfuscate all Lua files in a directory
        
        Args:
            input_dir: Directory containing Lua files
            output_dir: Output directory (default: input_dir/obfuscated)
            level: Obfuscation level
            pattern: File pattern to match (default: *.lua)
            recursive: Search subdirectories
            advanced_options: Dictionary of advanced options
        """
        # Setup output directory
        if output_dir is None:
            output_dir = os.path.join(input_dir, "obfuscated")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Find all matching files
        if recursive:
            search_pattern = os.path.join(input_dir, "**", pattern)
            lua_files = glob.glob(search_pattern, recursive=True)
        else:
            search_pattern = os.path.join(input_dir, pattern)
            lua_files = glob.glob(search_pattern)
        
        if not lua_files:
            print(f"❌ No files matching '{pattern}' found in {input_dir}")
            return
        
        print(f"🔍 Found {len(lua_files)} file(s) to obfuscate")
        print(f"📁 Output directory: {output_dir}")
        print(f"⚙️  Obfuscation level: {level}")
        print("=" * 60)
        
        # Process each file
        for idx, lua_file in enumerate(lua_files, 1):
            self._process_file(lua_file, output_dir, level, advanced_options, idx, len(lua_files))
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 Batch Processing Summary")
        print("=" * 60)
        print(f"✅ Successfully processed: {self.processed}")
        print(f"❌ Failed: {self.failed}")
        print(f"⏱️  Total time: {self.total_time:.2f}s")
        print(f"⚡ Average time per file: {self.total_time/len(lua_files):.2f}s")
        
    def _process_file(self, input_path, output_dir, level, advanced_options, current, total):
        """Process a single file"""
        try:
            start_time = time.time()
            
            # Read input
            with open(input_path, 'r', encoding='utf-8') as f:
                script = f.read()
            
            original_size = len(script)
            
            # Get relative path for maintaining directory structure
            input_dir = os.path.dirname(input_path)
            rel_path = os.path.basename(input_path)
            
            # Obfuscate
            obfuscator = LuaObfuscator(script)
            obfuscated = obfuscator.obfuscate(level=level)
            
            # Apply advanced techniques if specified
            if advanced_options:
                obfuscated = apply_advanced_obfuscation(obfuscated, advanced_options)
            
            # Generate output filename
            base_name = os.path.splitext(rel_path)[0]
            output_filename = f"{base_name}_obfuscated.lua"
            output_path = os.path.join(output_dir, output_filename)
            
            # Write output
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(obfuscated)
            
            elapsed = time.time() - start_time
            self.total_time += elapsed
            self.processed += 1
            
            obfuscated_size = len(obfuscated)
            size_ratio = obfuscated_size / original_size
            
            print(f"[{current}/{total}] ✅ {os.path.basename(input_path)}")
            print(f"        Size: {original_size:,} → {obfuscated_size:,} bytes ({size_ratio:.2f}x)")
            print(f"        Time: {elapsed:.2f}s")
            
        except Exception as e:
            self.failed += 1
            print(f"[{current}/{total}] ❌ {os.path.basename(input_path)}")
            print(f"        Error: {str(e)}")
    
    def obfuscate_file_list(self, file_list, output_dir, level="extreme", advanced_options=None):
        """
        Obfuscate a specific list of files
        
        Args:
            file_list: List of file paths
            output_dir: Output directory
            level: Obfuscation level
            advanced_options: Dictionary of advanced options
        """
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"🔍 Processing {len(file_list)} file(s)")
        print(f"📁 Output directory: {output_dir}")
        print("=" * 60)
        
        for idx, lua_file in enumerate(file_list, 1):
            self._process_file(lua_file, output_dir, level, advanced_options, idx, len(file_list))
        
        print("\n" + "=" * 60)
        print(f"✅ Processed: {self.processed} | ❌ Failed: {self.failed}")
        print("=" * 60)


def main():
    """CLI interface for batch processing"""
    if len(sys.argv) < 2:
        print("""
🔒 Batch Lua Obfuscator

Usage:
    python batch_obfuscator.py <input_directory> [options]

Options:
    -o, --output <dir>      Output directory (default: input_dir/obfuscated)
    -l, --level <level>     Obfuscation level: basic, advanced, extreme, paranoid
    -r, --recursive         Search subdirectories recursively
    -p, --pattern <pattern> File pattern (default: *.lua)
    --anti-debug            Enable anti-debugging
    --vm-wrapper            Enable VM wrapper
    --control-flow          Enable control flow obfuscation
    --junk-code             Enable junk code injection
    
Examples:
    # Basic usage
    python batch_obfuscator.py ./scripts
    
    # Custom output and level
    python batch_obfuscator.py ./scripts -o ./protected -l paranoid
    
    # Recursive with all advanced options
    python batch_obfuscator.py ./scripts -r --anti-debug --vm-wrapper
        """)
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = None
    level = "extreme"
    pattern = "*.lua"
    recursive = False
    advanced_options = {
        'anti_debug': False,
        'vm_wrapper': False,
        'control_flow': False,
        'junk_code': False
    }
    
    # Parse arguments
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg in ['-o', '--output']:
            output_dir = sys.argv[i + 1]
            i += 2
        elif arg in ['-l', '--level']:
            level = sys.argv[i + 1]
            i += 2
        elif arg in ['-p', '--pattern']:
            pattern = sys.argv[i + 1]
            i += 2
        elif arg in ['-r', '--recursive']:
            recursive = True
            i += 1
        elif arg == '--anti-debug':
            advanced_options['anti_debug'] = True
            i += 1
        elif arg == '--vm-wrapper':
            advanced_options['vm_wrapper'] = True
            i += 1
        elif arg == '--control-flow':
            advanced_options['control_flow'] = True
            i += 1
        elif arg == '--junk-code':
            advanced_options['junk_code'] = True
            i += 1
        else:
            print(f"Unknown argument: {arg}")
            i += 1
    
    # Check if advanced options are enabled
    if not any(advanced_options.values()):
        advanced_options = None
    
    # Run batch obfuscation
    batch = BatchObfuscator()
    batch.obfuscate_directory(
        input_dir=input_dir,
        output_dir=output_dir,
        level=level,
        pattern=pattern,
        recursive=recursive,
        advanced_options=advanced_options
    )


if __name__ == "__main__":
    main()
