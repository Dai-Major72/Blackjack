from pathlib import Path
def create_save_file(save_file_path, save_file_title="Save File"):
    global save_file
    save_file = save_file_path
    if Path(save_file_path).is_file() == False:
        with open(save_file_path, "x") as saveCreate:
            saveCreate.write(f"{save_file_title}\n\n")

def save(joueur="Major", *values):
    in_save = False
    with open(save_file, "rt") as save:
        cache = save.read()
        for line in cache.splitlines():
            if joueur == line.split(" =")[0]:
                cache = cache.replace(line, f"{joueur} = {values}\n")
                with open(save_file, "w") as saveW:
                    saveW.write(cache)
                in_save = True
                break

        if not in_save:
            with open(save_file, "a") as saveA:
                saveA.write(f"{joueur} = {values}")
