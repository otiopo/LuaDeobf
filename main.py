import sys

def DeObfuscate(script, output):
  joined = ""
  for line in script.split("\n"):
    if joined == "":
      joined = "l." + line
    else:
      joined = joined + "\nl." + line
  exec("import lua\nl = lua.Lua()\n" + joined)

if len(sys.argv) > 1:
  if len(sys.argv) > 2:
    try:
      with open(sys.argv[1], "r") as file:
        DeObfuscate(file.read(), sys.argv[2])
        file.close()
    except:
      print("Could Not Open File!")
  else:
    print("Enter The Output File!")
else:
  print("Enter The Lua File You Want To DeObfuscate!")