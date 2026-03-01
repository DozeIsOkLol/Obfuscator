# 🚀 Quick Start Guide

Get started with the Lua Obfuscator in 5 minutes!

## ⚡ Fastest Way to Obfuscate

### Option 1: GUI (Easiest for Beginners)

1. Run the GUI:
```bash
python obfuscator_gui.py
```

2. Click "Load File" and select your Lua script
3. Choose obfuscation level (recommend "extreme")
4. Click "Obfuscate"
5. Click "Save Output" to save your obfuscated script

**Done!** 🎉

---

### Option 2: Command Line (Fast for Power Users)

```bash
python lua_obfuscator.py input.lua output.lua extreme
```

Replace:
- `input.lua` with your script path
- `output.lua` with desired output path
- `extreme` with desired level (basic/advanced/extreme/paranoid)

---

### Option 3: Test with Sample Script

We've included a test script to try out the obfuscator:

```bash
# Obfuscate the test script
python lua_obfuscator.py test_script.lua test_obfuscated.lua extreme

# Check the results
cat test_obfuscated.lua
```

---

## 🎯 Which Obfuscation Level Should I Use?

| Level | Best For | Speed | Security |
|-------|----------|-------|----------|
| **Basic** | Quick tests, non-critical scripts | ⚡⚡⚡ | ⭐⭐ |
| **Advanced** | Most scripts, general protection | ⚡⚡ | ⭐⭐⭐ |
| **Extreme** | ✅ Recommended for production | ⚡ | ⭐⭐⭐⭐ |
| **Paranoid** | High-value, sensitive scripts | 🐢 | ⭐⭐⭐⭐⭐ |

**For most users: Start with "extreme"**

---

## 💡 Pro Tips

### 1. Always Keep Your Original Source Code
Never obfuscate your only copy! Always keep the original:

```
my_script.lua           ← Keep this safe!
my_script_obf.lua       ← Use this in production
```

### 2. Test Before Deployment
Always test your obfuscated script in Roblox Studio first:

```bash
# 1. Obfuscate
python lua_obfuscator.py script.lua script_obf.lua extreme

# 2. Test script_obf.lua in Roblox Studio
# 3. If works → deploy to game
# 4. If errors → check original script
```

### 3. Batch Process Multiple Files
For projects with many scripts:

```bash
python batch_obfuscator.py ./my_scripts -o ./obfuscated -l extreme
```

---

## 🆘 Common Issues & Solutions

### Issue 1: "Module tkinter not found" (GUI only)

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Windows/Mac: Reinstall Python with tkinter enabled
```

### Issue 2: Obfuscated Script Has Errors in Roblox

**Possible causes:**
1. Original script has syntax errors → Fix original first
2. Using Roblox-specific features the obfuscator doesn't recognize → Report issue
3. Very complex script structure → Try lower obfuscation level

**Solution:**
```bash
# Try with lower level first
python lua_obfuscator.py script.lua script_obf.lua advanced
```

### Issue 3: Obfuscated Script is Too Large

Large files can slow down your game. **Solutions:**

1. Split your script into smaller modules
2. Use "advanced" instead of "paranoid" level
3. Remove unnecessary comments/whitespace from original

---

## 📚 Next Steps

Once you're comfortable with basic obfuscation:

1. **Explore Advanced Options**: Read `README.md` for advanced techniques
2. **API Integration**: Use the Python API for custom workflows
3. **Automation**: Set up batch processing for your entire project
4. **Contribute**: Found a bug? Have an idea? Contribute on GitHub!

---

## 🔗 Useful Commands Cheat Sheet

```bash
# Basic obfuscation
python lua_obfuscator.py input.lua output.lua

# With specific level
python lua_obfuscator.py input.lua output.lua paranoid

# GUI
python obfuscator_gui.py

# Batch processing
python batch_obfuscator.py ./scripts

# Batch with options
python batch_obfuscator.py ./scripts -l paranoid -r --anti-debug

# Run examples
python example_usage.py
```

---

## ✅ Verification Checklist

Before deploying your obfuscated script:

- [ ] Original source code backed up
- [ ] Obfuscated script tested in Roblox Studio
- [ ] All features working as expected
- [ ] Performance is acceptable
- [ ] File size is reasonable
- [ ] No error messages in output window

---

## 🎓 Learn More

- Full documentation: `README.md`
- Example scripts: `example_usage.py`
- Advanced features: `advanced_obfuscator.py`

---

## 🤝 Need Help?

1. Check `README.md` for detailed documentation
2. Run examples: `python example_usage.py`
3. Report issues on GitHub
4. Join the community discussions

---

**Happy obfuscating! 🔒**

Remember: Obfuscation is just one layer of protection. Always use best security practices!
