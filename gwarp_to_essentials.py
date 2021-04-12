#minecraft mods warps converter from gwarp data file
#to essentials warp.yml file
#delete visitors in .data file
#copy path to .data file and run


myvars = []
with open("C:\\Users\\Mihai\\Desktop\\New folder\\Warps.data") as myfile:
    for line in myfile:
        name, var = line.partition(":")[::2]
        myvars.append(name.strip().rstrip("\n"))
        myvars.append(var.rstrip("\n"))

myvars = list(filter(None, myvars))

print((myvars))

for counter in range(0,len(myvars),22):
    with open("here\\"+str(myvars[counter+2])+".yml", "w") as output:
        output.write("world: " + myvars[counter+21]+"\n")
        output.write("x: " + myvars[counter+11]+"\n")
        output.write("y: " + myvars[counter+13]+"\n")
        output.write("z: " + myvars[counter+15]+"\n")
        output.write("yaw: " + myvars[counter+19]+"\n")
        output.write("pitch: " + myvars[counter+17]+"\n")
        output.write("name: " + myvars[counter+2]+"\n")
        output.write("lastowner: " + myvars[counter+4]+"\n")

